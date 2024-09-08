import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class DebtSimulator:
    def __init__(self, debt_outgoings, non_debt_outgoings, income):
        """
        Initialize the DebtSimulator with data provided as arrays.
        """
        self.debt_outgoings = pd.DataFrame(debt_outgoings, columns=['Company', 'Minimum Payment', 'Total Owed', 'Current APR', 'Expires', 'New APR on Expiry', 'USD', 'GBP'])
        self.non_debt_outgoings = pd.DataFrame(non_debt_outgoings, columns=['Expense', 'Total Owed'])
        self.income = pd.DataFrame(income, columns=['Source', 'Amount'])
        self.start_date = datetime.now()
        self._convert_numeric_columns()
 
    def _convert_numeric_columns(self):
        """
        Convert specified columns to numeric type.
        """
        numeric_columns = {
            'debt_outgoings': ['Minimum Payment', 'Total Owed', 'Current APR', 'New APR on Expiry'],
            'non_debt_outgoings': ['Total Owed'],
            'income': ['Amount']
        }

        for df_name, columns in numeric_columns.items():
            df = getattr(self, df_name)
            for col in columns:
                if col in df.columns:
                    print(df[col])
                    df[col] = pd.to_numeric(df[col], errors='coerce')
            df.fillna(0, inplace=True)

    def run_simulation(self, method, max_months=1000):
        """
        Run a debt repayment simulation using either the Avalanche or Snowball method.

        Args:
            method (str): Either 'avalanche' or 'snowball'.
            max_months (int): Maximum number of months to simulate.

        Returns:
            tuple: A schedule of debt repayment and detailed payment information.
        """
        schedule = []
        payment_details = []
        total_interest = total_principal = 0
        previous_debt = self.debt_outgoings['Total Owed'].sum()

        for month in range(1, max_months + 1):
            current_date = self.start_date + timedelta(days=30 * month)
            self.debt_outgoings = self._apply_interest(self.debt_outgoings, current_date)
            total_interest += self.debt_outgoings['Interest'].sum()
            available_funds = self._calculate_available_funds()

            self.debt_outgoings, remaining_funds = self._distribute_payments(self.debt_outgoings, available_funds, method)

            total_principal += (available_funds - remaining_funds)
            current_debt = self.debt_outgoings['Total Owed'].sum()

            schedule.append((month, current_debt, total_interest, total_principal))
            payment_details.extend([{
                'Month': month, 'Company': row['Company'], 'Payment': row['Payment'],
                'Extra Payment': row['Extra Payment'], 'Remaining Debt': row['Total Owed']
            } for _, row in self.debt_outgoings.iterrows()])

            if current_debt <= 0 or (current_debt > previous_debt and month > 1):
                break
            previous_debt = current_debt

        return schedule, pd.DataFrame(payment_details)

    def _apply_interest(self, cc_df, current_date):
        """Apply interest to credit card balances."""
        cc_df['Total Owed'] = cc_df['Total Owed'].astype(float)  # Ensure 'Total Owed' is float
        for idx, row in cc_df.iterrows():
            apr = row['Current APR']
            if pd.notna(row['Expires']) and row['Expires'] != 'NA':
                try:
                    expiry_date = datetime.strptime(row['Expires'], '%m/%d/%Y')
                    if current_date >= expiry_date:
                        apr = row['New APR on Expiry']
                except ValueError:
                    pass  # If date parsing fails, keep the current APR

            monthly_rate = apr / 1200
            interest = row['Total Owed'] * monthly_rate
            cc_df.at[idx, 'Interest'] = interest
            cc_df.at[idx, 'Total Owed'] += interest
        return cc_df

    def _calculate_available_funds(self):
        """Calculate available funds for debt repayment."""
        return max(self.income['Amount'].sum() - self.non_debt_outgoings['Total Owed'].sum(), 0)

    def _distribute_payments(self, cc_df, available_funds, method):
        """Distribute payments according to the chosen method (avalanche or snowball)."""
        cc_df = cc_df.sort_values(['Current APR', 'Total Owed'], ascending=[False, True] if method == 'avalanche' else [True, True])
        cc_df['Payment'] = cc_df['Extra Payment'] = 0.0
        cc_df['Total Owed'] = cc_df['Total Owed'].astype(float)  # Ensure 'Total Owed' is float
        cc_df['Minimum Payment'] = cc_df['Minimum Payment'].astype(float)  # Ensure 'Minimum Payment' is float

        for idx, row in cc_df.iterrows():
            payment = min(row['Minimum Payment'], row['Total Owed'], available_funds)
            cc_df.at[idx, 'Payment'] = payment
            available_funds -= payment

        if available_funds > 0:
            idx = cc_df.index[0]
            extra = min(available_funds, cc_df.at[idx, 'Total Owed'] - cc_df.at[idx, 'Payment'])
            cc_df.at[idx, 'Payment'] += extra
            cc_df.at[idx, 'Extra Payment'] = extra
            available_funds -= extra

        cc_df['Total Owed'] -= cc_df['Payment']
        return cc_df[cc_df['Total Owed'] > 0.01], available_funds

    def generate_summary(self, schedule, method):
        final_month = schedule[-1]
        return {
            'method': method,
            'total_months': len(schedule),
            'total_interest_paid': final_month[2],
            'total_amount_paid': final_month[2] + final_month[3]
        }
    
    def _populate_example_data(self, sheet_name):
        """Populate a sheet with example data."""
        example_data = {
            'sample-debt-outgoings': [
                ['Company', 'Minimum Payment', 'Total Owed', 'Current APR', 'Expires', 'New APR on Expiry', 'USD', 'GBP'],
                ['Credit Card A', 50, 5000, 18.99, 'NA', 18.99, True, False],
                ['Credit Card B', 75, 7500, 15.99, '12/31/2024', 21.99, True, False],
                ['Personal Loan', 200, 10000, 8.5, 'NA', 8.5, True, False],
                ['Store Card', 25, 1500, 24.99, 'NA', 24.99, True, False]
            ],
            'sample-non-debt-outgoings': [
                ['Expense', 'Total Owed'],
                ['Rent', 1200],
                ['Utilities', 200],
                ['Groceries', 400],
                ['Transportation', 150],
                ['Insurance', 100]
            ],
            'sample-income': [
                ['Source', 'Amount'],
                ['Primary Job', 3500],
                ['Side Hustle', 500]
            ]
        }
from flask import Flask, jsonify, request
from debt_simulator import DebtSimulator

# Can we have initial loading call the API but further updates use Server Actions?

example_data = {
            'sample-debt-outgoings': [
                ['Credit Card A', 50, 5000, 18.99, 'NA', 18.99, True, False],
                ['Credit Card B', 75, 7500, 15.99, '12/31/2024', 21.99, True, False],
                ['Personal Loan', 200, 10000, 8.5, 'NA', 8.5, True, False],
                ['Store Card', 25, 1500, 24.99, 'NA', 24.99, True, False]
            ],
            'sample-non-debt-outgoings': [
                ['Rent', 1200],
                ['Utilities', 200],
                ['Groceries', 400],
                ['Transportation', 150],
                ['Insurance', 100]
            ],
            'sample-income': [
                ['Primary Job', 3500],
                ['Side Hustle', 500]
            ]
}

app = Flask(__name__)

@app.route('/api/data', methods=['POST', 'GET'])
def hello_data():
    if request.method == 'POST':
        print('Test input:', request.form['debt_method'])
    simulator = DebtSimulator(example_data['sample-debt-outgoings'], example_data['sample-non-debt-outgoings'], example_data['sample-income'])
    # Run the simulation
    schedule, payment_details = simulator.run_simulation('avalanche')

    # Generate the summary
    summary = simulator.generate_summary(schedule, 'avalanche')

    return jsonify({
        'schedule': schedule,
        'payment_details': payment_details.to_dict(orient='records'),
        'summary': summary
    })
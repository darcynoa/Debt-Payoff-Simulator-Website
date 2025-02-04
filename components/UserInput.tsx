import UserInputTable from "@/components/UserInputTable";
// const example_data = {
//   Debt: [
//     ["Credit Card A", 50, 5000, 18.99, "NA", 18.99, true, false],
//     ["Credit Card B", 75, 7500, 15.99, "12/31/2024", 21.99, true, false],
//     ["Personal Loan", 200, 10000, 8.5, "NA", 8.5, true, false],
//     ["Store Card", 25, 1500, 24.99, "NA", 24.99, true, false],
//   ],
//   "Other Expenses": [
//     ["Rent", 1200],
//     ["Utilities", 200],
//     ["Groceries", 400],
//     ["Transportation", 150],
//     ["Insurance", 100],
//   ],
//   Income: [
//     ["Primary Job", 3500],
//     ["Side Hustle", 500],
//   ],
// };

function UserInput() {
  return (
    <div className="fixed bottom-0 h-1/2 w-screen grid grid-cols-[1fr_3fr_1fr]">
      {/* Three Tables */}
      <UserInputTable cols={2} header={"Income"}  />
      <UserInputTable cols={8} header={"Debt"} />
      <UserInputTable
        cols={2}
        header={"Other Expenses"}
      />
    </div>
  );
}

export default UserInput;

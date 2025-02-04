interface Props {
  header: string;
}

const TableHeader = ({ header }: Props) => {
  const cellHeadings: Record<string, string[]> = {
    Income: ["Source", "Amount"],
    Debt: [
      "Company",
      "Min. Payment",
      "Total Owed",
      "Current APR",
      "Expires",
      "New APR on Exp.",
      "USD",
      "GBP",
    ],
    "Other Expenses": ["Expenses", "Total Owed"],
  };
  return (
    <>
      <h2
        className={`border-[1px] border-white text-center col-span-full align-middle leading-[2.5]`}
      >
        {header}
      </h2>
      {cellHeadings[header].map((colHeader) => (
        <h3
          className="text-center border-[1px] border-white leading-[2.5] text-[0.9rem]"
          key={colHeader}
        >
          {colHeader}
        </h3>
      ))}
    </>
  );
};

export default TableHeader;

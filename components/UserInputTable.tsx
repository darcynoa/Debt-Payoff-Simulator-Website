"use client";

import TableHeader from "@/components/TableHeader";
// import TableCell from "./TableCell";

interface Props {
  cols: number;
  header: string;
}

function UserInputTable({ cols, header }: Props) {
  return (
    <div
      className="grid grid-flow-dense grid-rows-[42px_36px_32px]"
      style={{
        gridTemplateColumns: `repeat(${cols}, minmax(0, 1fr))`,
      }}
    >
      <TableHeader header={header} />
      {/* {Array.from({ length: cols }).map((el, index) => (
        <TableCell key={index} />
      ))} */}
    </div>
  );
}

export default UserInputTable;

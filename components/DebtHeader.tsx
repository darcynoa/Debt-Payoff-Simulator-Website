interface Props {
    data: any
}

function DebtHeader(props: Props) {
    const totalAmountPaid = Math.round(props.data.summary.total_amount_paid)
    const totalMonths = props.data.summary.total_months
  return (
    <div className="">
        <h1 className="text-[4rem]">With the {props.data.summary.method} method</h1>
        <p>You will pay off <strong>${totalAmountPaid}</strong> (approximately) over the course of {totalMonths} months</p>
      </div>
  )
}

export default DebtHeader
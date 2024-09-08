
export default async function Home() {
  let data = await fetch('http://127.0.0.1:5000/api/data');
  let debtData = await data.json()

  const totalAmountPaid = Math.round(debtData.summary.total_amount_paid)
  const totalMonths = debtData.summary.total_months

  // DELETE # Can we have initial loading call the API but further updates use Server Actions?
  
  return (
    <div className="">
      <h1 className="text-[4rem]">With the {debtData.summary.method} method</h1>
      <p>You will pay off ${totalAmountPaid} (approximately) over the course of {totalMonths} months</p>
    </div>
  );
}



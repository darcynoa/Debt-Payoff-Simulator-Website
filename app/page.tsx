import { log } from "console";


export default async function Home() {
  let data = await fetch('http://127.0.0.1:5000/api/avalanche');
  let avalanche = await data.json()
  console.log('avalanche :', avalanche)
  data = await fetch('http://127.0.0.1:5000/api/snowball');
  let snowball = await data.json()
  console.log('snowball:', snowball)

  const avalancheTotalAmountPaid = Math.round(avalanche.summary.total_amount_paid)
  const avalancheTotalMonths = avalanche.summary.total_months

  const snowballTotalAmountPaid = Math.round(snowball.summary.total_amount_paid)
  const snowballTotalMonths = snowball.summary.total_months

  return (
    <div className="grid grid-cols-2 gap-6">
      <div className="">
        <h1 className="text-[4rem]">With the {avalanche.summary.method} method</h1>
        <p>You will pay off <strong>${avalancheTotalAmountPaid}</strong> (approximately) over the course of {avalancheTotalMonths} months</p>
      </div>
      <div className="">
        <h1 className="text-[4rem]">With the {snowball.summary.method} method</h1>
        <p>You will pay off <strong>${snowballTotalAmountPaid}</strong> (approximately) over the course of {snowballTotalMonths} months</p>
      </div>
    </div>
  );
}


 
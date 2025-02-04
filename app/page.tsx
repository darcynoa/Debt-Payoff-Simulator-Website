import DebtInfo from "@/components/DebtInfo";
import UserInput from "@/components/UserInput";

export default async function Home() {
  let data = await fetch("http://127.0.0.1:5000/api/avalanche");
  const avalanche = await data.json();
  data = await fetch("http://127.0.0.1:5000/api/snowball");
  const snowball = await data.json();

  return (
    <>
      <DebtInfo avalanche={avalanche} snowball={snowball} />
      <UserInput />
    </>
  );
}

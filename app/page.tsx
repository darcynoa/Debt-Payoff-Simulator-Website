export default async function Home() {
  let data = await fetch('http://127.0.0.1:5000/api/hello');
  let hello = await data.json()
  return (
    <h1>{hello.message}</h1>
  );
}



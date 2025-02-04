import DebtHeader from "@/components/DebtHeader";

interface Props {
  avalanche: Record<any, any>;
  snowball: Record<any, any>;
}

function DebtInfo({ avalanche, snowball }: Props) {
  return (
    <div className="grid grid-cols-2 gap-6">
      <DebtHeader data={avalanche} />
      <DebtHeader data={snowball} />
    </div>
  );
}

export default DebtInfo;

"use client";
import { useKernelClient, useBalance } from "@zerodev/waas";
import truncateEthAddress from "truncate-eth-address";

export default function SmartAccountBlock() {
  const { address } = useKernelClient();
  const { data } = useBalance();
  console.log(address);

  return (
    <>
      <div className="mb-4">Address: {truncateEthAddress(address || "")}</div>
      <div className="mb-4">
        Balance: {data ? `${data.formatted} ${data.symbol}` : ""}
      </div>
    </>
  );
}

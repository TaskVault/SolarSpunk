"use client";

import { Button } from "@/components/button";
import { Checkbox, CheckboxField } from "@/components/checkbox";
import { Divider } from "@/components/divider";
import { Label } from "@/components/fieldset";
import { Heading, Subheading } from "@/components/heading";
import { Input } from "@/components/input";
import { Select } from "@/components/select";
import { Text } from "@/components/text";
import { Textarea } from "@/components/textarea";
import type { Metadata } from "next";
import { useSendUserOperation, useKernelClient } from "@zerodev/waas";
import { parseAbi } from "viem";

const abi = parseAbi([
  "function mint(address _to, uint256 __constantPowerConsumption, uint256 _constantPowerProduction, uint256 _latestPowerConsumption, uint256 _latestPowerProduction) public",
]);

export default function Mint() {
  const { address } = useKernelClient();

  const { write } = useSendUserOperation();

  return (
    <form method="post" className="mx-auto max-w-4xl">
      <Heading>Mint</Heading>
      <Divider className="my-10 mt-6" />

      <section className="grid gap-x-8 gap-y-6 sm:grid-cols-2">
        <div className="space-y-1">
          <Subheading>Address</Subheading>
          <Text>Address to mint the tokens to</Text>
        </div>
        <div>
          <Input aria-label="Address" name="adresss" defaultValue={address} />
        </div>
      </section>

      <Divider className="my-10" soft />

      <section className="grid gap-x-8 gap-y-6 sm:grid-cols-2">
        <div className="space-y-1">
          <Subheading>Constant power consumption</Subheading>
          <Text>
            The constant power consumption of the organization in watts
          </Text>
        </div>
        <div>
          <Input aria-label="Constant power consumption" name="cpc" />
        </div>
      </section>

      <Divider className="my-10" soft />

      <section className="grid gap-x-8 gap-y-6 sm:grid-cols-2">
        <div className="space-y-1">
          <Subheading>Constant power production</Subheading>
          <Text>
            The constant power production of the organization in watts
          </Text>
        </div>
        <div>
          <Input aria-label="Constant power production" name="cpp" />
        </div>
      </section>

      <Divider className="my-10" soft />

      <section className="grid gap-x-8 gap-y-6 sm:grid-cols-2">
        <div className="space-y-1">
          <Subheading>Latest power consumption</Subheading>
          <Text>The latest power consumption of the organization in watts</Text>
        </div>
        <div>
          <Input aria-label="Latest power consumption" name="lpc" />
        </div>
      </section>

      <Divider className="my-10" soft />

      <div className="flex justify-end gap-4">
        <Button
          type="submit"
          onClick={() => {
            const address = document.getElementById("address")!;
            const cpc = document.getElementById("cpc")!;
            const cpp = document.getElementById("cpp")!;
            const lpc = document.getElementById("lpc")!;

            write([
              {
                address: "0x1ddfaf71fc609022cbe0bc3588479b107304f72d",
                abi,
                functionName: "mint",
                // inputs from form
                args: [address, cpc, cpp, lpc],
              },
            ]);
          }}
        >
          Mint
        </Button>
      </div>
    </form>
  );
}

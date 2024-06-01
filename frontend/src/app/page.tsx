"use client";

import { useKernelClient } from "@zerodev/waas";
import { useState, useEffect } from "react";
import ConnectBlock from "@/components/ConnectBlock";
import SmartAccountBlock from "@/components/SmartAccountBlock";

import { Avatar } from "@/components/avatar";
import { Badge } from "@/components/badge";
import { Divider } from "@/components/divider";
import { Heading, Subheading } from "@/components/heading";
import { Select } from "@/components/select";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/table";
import { getHistoricalEnergyProduction } from "@/data";

export function Stat({
  title,
  value,
  change,
}: {
  title: string;
  value: string;
  change: string;
}) {
  return (
    <div>
      <Divider />
      <div className="mt-6 text-lg/6 font-medium sm:text-sm/6">{title}</div>
      <div className="mt-3 text-3xl/8 font-semibold sm:text-2xl/8">{value}</div>
      <div className="mt-3 text-sm/6 sm:text-xs/6">
        <Badge color={change.startsWith("+") ? "lime" : "pink"}>{change}</Badge>{" "}
        <span className="text-zinc-500">from last week</span>
      </div>
    </div>
  );
}

export default function Home() {
  const [data, setData] = useState(null) as any;

  useEffect(() => {
    setData(getHistoricalEnergyProduction());
  }, []);

  return (
    <>
      <Heading>SolarSpunk Energy</Heading>
      <div className="mt-8 flex items-end justify-between">
        <p>Here comes an intro to the project</p>
      </div>
    </>
  );
}

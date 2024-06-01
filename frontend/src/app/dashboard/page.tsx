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
  const rawdata = getHistoricalEnergyProduction();
  const data = rawdata.sort((a, b) => {
    return a.year - b.year || a.month - b.month || a.day - b.day;
  });

  const sums = data.reduce(
    (acc, { wind, solar, hydro }) => {
      acc.wind += wind;
      acc.solar += solar;
      acc.hydro += hydro;
      return acc;
    },
    { wind: 0, solar: 0, hydro: 0 }
  );

  return (
    <>
      <Heading>Energy Dashboard</Heading>
      <div className="mt-8 flex items-end justify-between">
        <Subheading>Total generated</Subheading>
      </div>
      <div className="mt-3 grid gap-8 sm:grid-cols-1 xl:grid-cols-3">
        <Stat
          title="Solar"
          value={sums.solar.toFixed(4).toString()}
          change={"+" + (100 * Math.random()).toFixed(2).toString()}
        />
        <Stat
          title="Wind"
          value={sums.wind.toFixed(4).toString()}
          change={"+" + (100 * Math.random()).toFixed(2).toString()}
        />
        <Stat
          title="Hydro"
          value={sums.hydro.toFixed(4).toString()}
          change={"+" + (100 * Math.random()).toFixed(2).toString()}
        />
      </div>

      <Subheading className="mt-14">Energy generated last 30 Days</Subheading>
      <Table className="mt-4 [--gutter:theme(spacing.6)] lg:[--gutter:theme(spacing.10)]">
        <TableHead>
          <TableRow>
            <TableHeader>Year</TableHeader>
            <TableHeader>Month</TableHeader>
            <TableHeader>Day</TableHeader>
            <TableHeader>Wind</TableHeader>
            <TableHeader>Solar</TableHeader>
            <TableHeader>Hydro</TableHeader>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.map((dataset) => (
            <TableRow
              key={dataset.year + dataset.month + dataset.day}
              title={`Energy production for ${dataset.year}-${dataset.month}-${dataset.day}`}
            >
              <TableCell>{dataset.year}</TableCell>
              <TableCell>{dataset.month}</TableCell>
              <TableCell>{dataset.day}</TableCell>
              <TableCell>{dataset.wind}</TableCell>
              <TableCell>{dataset.solar}</TableCell>
              <TableCell>{dataset.hydro}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </>
  );
}

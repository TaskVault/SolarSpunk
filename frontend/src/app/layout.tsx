import Providers from "@/components/Providers";
import "@mantine/core/styles.css";
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

import { ColorSchemeScript } from "@mantine/core";
import { getEvents } from "@/data";
import { ApplicationLayout } from "./application-layout";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: {
    template: "%s - SolarSpunk",
    default: "SolarSpunk",
  },
  description: "",
};

export default async function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  let events = await getEvents();

  return (
    <html lang="en">
      <head>
        <ColorSchemeScript />
      </head>
      <body className={inter.className}>
        <Providers>
          <ApplicationLayout events={events}>{children}</ApplicationLayout>
        </Providers>
      </body>
    </html>
  );
}

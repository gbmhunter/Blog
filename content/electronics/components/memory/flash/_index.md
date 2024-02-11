---
authors: [ Geoffrey Hunter ]
categories: [ Electronics, Electronic Components ]
date: 2024-02-08
description: NOR, NAND, speeds, applications and more info about flash memory.
draft: false
lastmod: 2024-02-08
tags: [ memory, flash, NOR, NAND ]
title: Flash Memory
type: page
---

## Overview

Flash ICs typically use the SPI communication protocol for communication to the MCU. This includes single lane SPI for slower flash and quad lane (QSPI) for faster flash. Data clock speeds of 80-100MHz are common[^macronix-mx25v5126f-nor-flash-ds].

## NOR Flash

Erase times can vary from approx. 50ms per 4KB sector to over 1s for the full chip[^macronix-mx25v5126f-nor-flash-ds].

{{% figure ref="fig-macronix-mx25v5126f-block-diagram" src="_assets/macronix-mx25v5126f-block-diagram.png" width="700px" caption="The internal block diagram showing the architecture of the MX25V5126F NOR flash IC from Macronix[^macronix-mx25v5126f-nor-flash-ds]." %}}

## NAND Flash

## References

[^macronix-mx25v5126f-nor-flash-ds]: Macronix International Co. (2020, Sep 3). _MX25V5126F - 2.3V-3.6V, 512K-BIT [x 1/x 2] CMOS Serial NOR Flash_ [datasheet]. Retrieved 2024-02-08, from https://www.macronix.com/Lists/Datasheet/Attachments/8750/MX25V5126F,%202.5V,%20512Kb,%20v1.1.pdf.
---
authors: [ Geoffrey Hunter ]
categories: [ Programming, Microcontrollers, Nordic ]
date: 2023-10-03
draft: false
lastmod: 2023-10-03
tags: [ programming, microcontrollers, Nordic, nRF53 ]
title: Getting The MCU RSSI In Firmware
type: page
---

## Overview

When testing the Bluetooth range on a device using the nRF53 SoC it's useful to know what the RSSI is from the perspective of the SoC.

The `hci_pwr_ctrl` example in the `nrfconnect/sdk-zephyr` repo contains example code that reads back the RSSI. See https://github.com/nrfconnect/sdk-zephyr/blob/b9253f60e83c046fa432d49b157e1536af1f1ab2/samples/bluetooth/hci_pwr_ctrl/src/main.c for the core parts of this.
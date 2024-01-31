---
authors: [ Geoffrey Hunter ]
categories: [ Electronics, Electronic Components ]
date: 2024-01-25
draft: false
lastmod: 2024-01-25
tags: [ electronics, electronic components, real time clocks ]
title: Real Time Clock (RTC) ICs
type: page
---

## Overview

_Real-Time Clock_ (RTC) ICs are chips which accurately track calender time. They are generally designed for low-power operation so that they can run of a small battery such as a [coin cell](/electronics/components/batteries/#button-cells-coin-cells). They are normally included on circuits and connected to a microcontroller when the application requires the microcontroller to keep track of time. They are better at keeping track of time than the MCUs internal oscillator due to:

1. Increased time keeping accuracy. Even when the MCU also has a 32.768kHz crystal, a dedicated RTC is normally more accurate due the ability on many RTCs to tune/calibrate the frequency.
1. Very low power operation. When a RTC is powered of a small battery like a coin cell it will continue running for many years and will not lose track of time when the MCU is unpowered.

RTCs normally keep track of either UNIX time (or any arbitrary start point you choose) and/or calender based time variables, which are also referred to as _broken-down time_[^zephyr-peripherals-rtc]. The broken-down time is normally represented by:

* Second of minute (a value in the range `[0-59]`)
* Minute of hour (a value in the range `[0-59]`)
* Hour of day (a value in the range `[0-23]`)
* Day of month (a value in the range `[0-31]`)
* Day of the week (e.g. `Sunday`, `Monday`, ..., normally represented by an integer in the range `[0, 6]`)
* Month (a value in the range `[1-12]`)
* Year (e.g. `2023`, `2024`, ...)

It is called broken-down time due to the time not being a single monotonic count of some unit like UNIX time (which is the number of seconds elapsed since 00:00:00 UTC on Jan 1st, 1970), but broken down into days/months/years.

## Code Examples

### Conversion Between UNIX Time and Calender Time

The following C code shows how to convert to/from UNIX time and calender time, which can be useful when dealing with RTCs in firmware:

```c
#include <stdio.h>
#include <time.h>

int main(void) {
  // UNIX time for Thu Jan 25 01:00:33 2024 UTC
  time_t unixTime = 1706144433;
  printf("Starting with UNIX time of %ld\n", unixTime);

  // Storage to hold converter calender time
  struct tm utcCalenderTime;

  // Do the conversion
  gmtime_r(&unixTime, &utcCalenderTime);

  // Print conversion. asctime() converts the calender time into a string for us
  printf("Converted calender time: %s", asctime(&utcCalenderTime));

  // Convert back from calender time to UNIX time just for fun
  time_t unixTime2 = mktime(&utcCalenderTime);
  printf("Converted UNIX time: %ld\n", unixTime2);

  return 0;
}
```

You can run this example at https://replit.com/@gbmhunter/c-unix-time-to-calender-time.

## Examples

### NXP PCF85263A

The NXP PCF85263A is a low-power [I2C](/electronics/communication-protocols/i2c-communication-protocol/) controlled RTC[^nxp-pcf85263a-rtc-ds]. It has separate pins for system power supply `VDD` and battery `VBAT`, switching over to `VBAT` automatically when system power is lost.

{{% ref "fig-nxp-pcf85263a-block-diagram" %}} shows the block diagram for this IC. You can see the pins that connect to an external [32.768kHz oscillator](/electronics/components/crystals-and-oscillators/#32678khz-crystals) in the bottom left corner.

{{% figure ref="fig-nxp-pcf85263a-block-diagram" src="_assets/nxp-pcf85263a-block-diagram.png" width="700px" caption="The block diagram for the NXP PCF85263A RTC[^nxp-pcf85263a-rtc-ds]." %}}

The time-based values (100ths of a second, seconds, minutes, hours, days, months, years) are all stored in Binary Coded Decimal (BCD) format (each group of 4 bits represents a number in the range [0, 9]). To prevent time values updating mid-read and producing inconsistent results, all time registers are frozen during reads over the I2C.

It automatically handles leap years correctly (which are deterministic and apply to all time zones). It does not handle day light saving (depends on the time zone), nor leap seconds (not deterministic).

The PCF85263A has an offset register that can be used to dynamically make small adjustments to the period of a second, so it can be used for things such as tuning/calibration and temperature compensation. It also supports a number of different quartz crystal types, including crystals that need a load capacitance of 6.0pF, 7.0pF, and 12.5pF.

## References

[^nxp-pcf85263a-rtc-ds]: NXP (2023, Nov 22). _PCF85263A - Tiny RTC/calendar with alarm function, battery switch-over, time stamp input, and I2C-bus_ [datasheet]. Retrieved 2024-01-25, from https://www.nxp.com/docs/en/data-sheet/PCF85263A.pdf.
[^zephyr-peripherals-rtc]: Zephyr (2024, Jan 25). _Real-Time Clock (RTC)_ [API documentation]. Retrieved 2024-01-25, from https://docs.zephyrproject.org/latest/hardware/peripherals/rtc.html.
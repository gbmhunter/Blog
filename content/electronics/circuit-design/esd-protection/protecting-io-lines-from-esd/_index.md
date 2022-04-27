---
authors: [ Geoffrey Hunter ]
categories: [ Electronics, Circuit Design ]
date: 2022-04-27
draft: false
lastmod: 2022-04-27
tags: [ ESD, diodes, electrostatic discharge, series resistance, steering diodes ]
title: Protecting IO Lines From ESD
type: page
---

## Overview

This page explains some of the ways you can go about protecting IO lines on a PCB from ESD events. This page assumes a basic scenario, you are wanting to protect an IO line that comes from an external connector and then connects to a GPIO pin on a MCU. However, the examples also apply to pretty much any IO line that connects to some sort of sensitive IC circuitry, e.g. enable pins on PSU ICs, communication lines, e.t.c.

## A Simple Resistor

One of the simplest ways of protecting an I/O line from ESD is to add a series resistor.

{{% img src="io-protection-with-resistor.png" width="600px" caption="Simple IO protection with a series resistor." %}}

One thing to be aware of is that this will limit the maximum frequency that can be used through this IO line (more so that other ESD techniques, such as steering diodes as discussed below). The series resistor will form a low-pass RC filter with the parasitic capacitance on the line after the resistor. For short PCB traces, most of this parasitic capacitance will be from the input capacitance of the GPIO pin on the MCU. Something in the region of `\(10pF\)` can be expected, which with a `\(1k\Omega\)` resistor will form a low-pass filter with a cut-off frequency of `\(16MHz\)`.

## Resistor With Capacitor

To improve on the simple series resistor, a capacitor can be added to further improve ESD protection. The capacitor is between the I/O line (once it has past through the resistor) and ground. This forms a low-pass filter which will help quench short (high frequency) ESD spikes.

{{% img src="io-protection-with-resistor-capacitor.png" width="600px" caption="Simple IO protection with a series resistor." %}}

## Steering Diodes

Arguably a better option than just a simple resistor and capacitor is the use of steering diodes. Steering diodes are connected between the I/O line and two voltage rails, typically `\(V_{CC}\)` and `\(GND\)`. You normally want to use Schottky diodes, as they have a lower forward voltage drop of around 0.3V compared to the standard PN junction diode forward voltage drop of 0.7V. This means your more robust external steering diodes will conduct and shunt more of the ESD energy away before the internal ESD protection diodes connected to the GPIO port in the MCU port do. 

TODO: Add schematic.

## Steering Diodes And TVS

As we learnt above, steering diodes dump the ESD energy into the voltage rails. This can be o.k. in the following conditions:

* ESD energy is low
* ESD event is short
* There is some capacitance on your voltage rails (decoupling caps and PSU output capacitors count!).
* The circuits connected to your voltage rail consume a "bit" of power, i.e. are not ultra-low power design circuits which only draw 10uA. 

You start to run into problems if the ESD energy is high, and the ESD event continues for some time, and your voltage rail can no longer "absorb" the ESD (by consuming the energy with running circuits, or dumping it into capacitance). The voltage rail may start to climb. If you are using a SMPS or series linear regulator to power this rail, there is nothing that these devices can do to stop the voltage from climbing (remember they can only source current, not sink it -- shunt regulators are the exception!). The rail voltage may climb to dangerously high levels which causes damage to the ICs running of it.

To add further protection, a TVS diode can be added to the voltage rail, to help clamp the voltage if it starts rising, as shown in the schematic below:

TODO: Add schematic.

Some ESD diode arrays incorporate steering diodes and a TVS diode to do just this. For example, the Bourns CDDFN10-0506N features 6 steering diode pairs connected to a single TVS. It is designed for high-speed signals and presents an input capacitance of only 0.25-0.35pF to the signal line, as well as "feed-through" routing design to minimize impedance changes[^bib-bourns-cddfn10-0506n-ds].

## References

[^bib-bourns-cddfn10-0506n-ds]: Bourns. _CDDFN10-0506N - TVS/Steering Diode Array (datasheet)_. Retrieved 2022-04-27 from https://www.bourns.com/docs/Product-Datasheets/CDDFN10-0506N.pdf.
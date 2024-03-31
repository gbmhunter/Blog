---
authors: [Geoffrey Hunter]
date: 2024-03-28
description: Workings, on GMR, IMR type magnetic rotary position sensors.
draft: false
lastmod: 2024-03-31
tags: [magnetism, magnetics, rotation, rotary, sensors, GMR]
title: Magnetic Rotary Position Sensors
type: page
---

{{% warning-is-notes %}}

## Overview

The benefits over a standard resistive potentiometer are that:

* Supports continuous rotation with no end stops.
* There is no resistive track/wiper that wears out.
* It's more resistant to contamination.

{{% figure src="_assets/ams-osram-as5600-in-knob-diagram.png" width="600px" caption="Diagram showing how the ams AS5600 rotary position sensor can be embedded into a standard dial (along with a magnet at the end of the shaft) for rotary position detection[^ams-osram-as5600-position-sensor-blog]." %}}

Most of the ICs include a processor to convert the raw magnetic readings into rotational data that can be read back over a communications bus to a microcontroller.

## Uses

* Sensing the rotor angle in BLDC and PMSM motors (which you need to know so that you can turn on the correct inverter MOSFETs).
* Sensing the rotation of the steering wheel in vehicles[^allegro-future-of-automotive-wheel-sensing-with-gmr].

## Giant Magnetoresistive (GMR) Sensors

Giant magnetoresistive (GMR) sensors are based on a quantum phenomenon called giant magnetoresistance. 

GMR sensors can give a much better SNR than more traditional hall-effect based sensors: 

> Our GMR design produces more than 50 times the voltage of a Hall element when a magnetic field is applied, which translates to a monumental boost in signal-to-noise ratio (SNR)[^allegro-future-of-automotive-wheel-sensing-with-gmr].

Gaps of 4-8mm between the magnet and sensing IC can be achieved with standard sized devices.[^allegro-future-of-automotive-wheel-sensing-with-gmr].

### History

Giant magnetoresistance was first discovered in 1988[^wikipedia-giant-magnetoresistance] [^nve-application-notes-for-gmr-sensors]. It is an effect that can be measured with nanometer-thick films of magnetic layers separated by similar thickness non-magnetic layers.

It is called "giant" because the multiple layers significantly increases the resistance change due to a magnetic field (can be a 50% change at very low temperatures) over standard "anisotropic" magnetoresistance (which is typically only a few percent)[^nve-how-gmr-works].

GMR is used in hard-drive read heads to detect read bits of the hard drive platters.

### Examples

#### Infineon TLE5014

{{% figure src="_assets/tle5014sp16d-3d-render-of-ic.png" width="200px" caption="A 3D render of the TLE5014SP16D IC[^infineon-tle5014sp16d-ds]." %}}

Integrated sensor, EEPROM. 

There are variants of the TLE5014 for different communication protocols. Supported is the SPC, PWM or the SENT interface for data transfer.

The TLE5014 has variants with fully redundant dual sensors for safety critical applications. To further aide with fault detection, the magnetic sensors are flipped w.r.t. to each other to create inverted outputs, as shown in {{% ref "fig-tle5014-dual-sensor-angle-output-graph" %}}.

{{% figure ref="fig-tle5014-dual-sensor-angle-output-graph" src="_assets/tle5014-dual-sensor-angle-output-graph.png" width="600px" caption="Graph showing the output angle from the TLE5014 variant which has dual sensors[^infineon-tle5014sp16d-ds]. The second sensor is flipped w.r.t. to the first one giving outputs which are the inverse of each other. This can be useful in safety critical applications." %}}


### Tunneling Magnetoresistive (TMR) Sensors

TMR: Tunneling Magneto Resistive technology (Infineon). High sensing sensitivty and high output voltage, no need for internal amplifier.

Tunnel magnetoresistance is an extension of spin-valve GMR[^wikipedia-giant-magnetoresistance].

## Further Reading

If you are interested in dirt-cheap, basic rotation sensors for things like user interface knobs, you might want to use a [potentiometer](/electronics/components/potentiometers-and-rheostats/). Another way of measuring rotation is an [optical encoder](/electronics/components/encoders/).

## References

[^ams-osram-as5600-position-sensor-blog]: AMS-Osram. _Reliability to switch on: Small position sensor keeps consumer products running_ [blog post]. Retrieved 2024-03-28, from https://ams-osram.com/news/blog/magnetic-rotary-position-sensor.
[^wikipedia-giant-magnetoresistance]: Wikipedia (2024, Jan 4). _Giant magnetoresistance_. Retrieved 2024-03-29, from https://en.wikipedia.org/wiki/Giant_magnetoresistance.
[^nve-application-notes-for-gmr-sensors]: NVE Corporation. _Application Notes for GMR Sensors_. Retrieved 2024-03-29, from https://www.nve.com/Downloads/apps.pdf.
[^infineon-tle5014sp16d-ds]: Infineon (2019, May 9). _TLE5014SP16D_ [datasheet]. Retrieved 2024-03-29, from https://www.infineon.com/dgdl/Infineon-TLE5014SP16D%20E0002-DataSheet-v01_00-EN.pdf?fileId=5546d46270c4f93e0170c92e1bc10212.
[^allegro-future-of-automotive-wheel-sensing-with-gmr]: Allegro Microsystems (2022, Feb 23). _The Future of Automotive Wheel Sensing with GMR_. Retrieved 2024-03-29, from https://www.allegromicro.com/en/insights-and-innovations/technical-documents/p0083-future-of-wheel-sensing-gmr.
[^nve-how-gmr-works]: NVE Corporation. _How GMR Works_. Retrieved 2024-03-31, from https://www2.nve.com/gmrsensors/gmr-operation.htm.
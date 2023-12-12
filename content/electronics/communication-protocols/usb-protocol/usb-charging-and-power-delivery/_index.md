---
authors: [ Geoffrey Hunter ]
categories: [ Electronics, Communication Protocols, USB ]
date: 2023-07-07
description: Data and power roles, standards, communication protocols, schematics and more info about USB power delivery (PD).
draft: false
lastmod: 2023-07-26
tags: [ USB, power delivery, PD, sinks, sources, e-marker, Type-C, USB-IF, batteries, charging, STMicroelectronics, Analog Devices ]
title: USB Charging and Power Delivery
type: page
---

{{% warning-is-notes %}}

## Overview

As more and more devices communicate over USB, the same devices are also being designed to be powered/charged over USB (removing the need for a second cable!). It started of with low power devices drawing power from the bus voltage, and has progressed to specific standards being implement to address the issue of charging power hungry devices (e.g. laptops) over the same USB cables. Many companies have implemented "quick charge" capabilities over USB cables, but the USB Implementers Forum (USB-IF) hopes to standardize charging with the more recent USB Power Delivery standard.

USB _power delivery_ (PD) is a **communication protocol and power transfer service designed to work with the USB Type-C connector**. Without PD, USB Type-C connectors can provide 5V at 3A (15W). PD allows a power source and sink to communicate with each other and negotiate a **higher voltage and/or current, up to maximum of 20V at 5A (240W)**[^usb-org-usb-pd]. Using Type-C cables to power things is becoming increasingly popular, and the EU has mandated that from 2024 most personal electronic equipment must come with a Type-C charging port[^consumer-org-eus-charging-port-rules]. And 2 years after that in 2026, laptops must also be chargeable from USB Type-C connectors.

{{% ref "table-summary-usb-specs" %}} shows a summary of USB specifications and maximum voltages, currents and powers.

<table ref="table-summary-usb-specs">
<caption>

Summary of USB maximum voltages, currents and powers for each standard[^ti-primer-on-usb-pd].</caption>
<thead>
<tr>
<th>Specification</th>
<th>Max. Voltage</th>
<th>Max. Current</th>
<th>Max. Power</th>
</tr>
</thead>
<tbody>
<tr>
<td>USB 2.0</td>
<td>5V</td>
<td>500mA</td>
<td>2.5W</td>
</tr>
<tr>
<td>USB 3.0/3.1</td>
<td>5V</td>
<td>900mA</td>
<td>4.5W</td>
</tr>
<tr>
<td>USB BC 1.2</td>
<td>5V</td>
<td>1.5A</td>
<td>7.5W</td>
</tr>
<tr>
<td>USB Type-C 1.2</td>
<td>5V</td>
<td>3A</td>
<td>15W</td>
</tr>
<tr>
<td>USB PD 3.0</td>
<td>20V</td>
<td>5A</td>
<td>150W</td>
</tr>
</tbody>
</table>

{{% aside type="info" %}}
According to the specification, all **USB type-C cables must be able to carry at least 3A** (at up to 20V, i.e. 60W). USB type-C cables supporting more than this (i.e. up to 5A) must contain e-marker chips, which identify the cable and it's current handling capabilities[^wikipedia-usb-c].
{{% /aside %}}

## Data and Power Roles

In USB terminology, it is important to understand the _data_ and _power_ roles.

There are three _data_ roles:

1. **Down-stream facing port (DFP)**: Sends data downstream, e.g. a USB port on your computer (which is acting as a host) or one of the many on a USB hub.
1. **Up-steam facing port (UFP)**: Sends data upstream, e.g. a USB mouse, keyboard or camera. UFPs typically acts a power _sinks_.
1. **Dual-role data (DRD) port**: Can act as either a DFP or UFP. 

Similarly, there are also three _power_ roles:

1. **Source**: A device capable of providing power onto VBUS, e.g. a USB hub or the host controller that provides the USB ports on your computer.
1. **Sink**: A device which consumes power from VBUS, e.g. a USB mouse or fan.
1. **Dual-role power**: A device that can act as either a source or a sink. A common example is a computers USB C port. When you plug a mouse into it, it powers the mouse, acting as a sink. However, many laptops support charing themselves over the same port. If you plug in a USB C charger, the computer acts as a sink.

## Standards

### USB Battery Charger Rev 1.2

The _USB Battery Charger Rev 1.2_ (BC 1.2) was a major upgrade to the specifications in revision 1.0 and 1.1[^usb-org-battery-charging-v1.2-spec]. It allows devices to draw up to 1.5A on a fixed 5V (7.5W)[^eaton-usb-charging-and-power-delivery]. It was developed to satisfy the need for higher currents than the default 100mA/500mA provided by USB 1.0 and 2.0. Today, it is largely superseded by USB PD (which I would recommend using instead of BC 1.2) for new designs.

There are some standard definitions in the battery charger spec:

* **Portable Device (PD)**: The USB device that is generally portable and is going to receive (sink) current from the USB hub or host.
* **Standard Downstream Port (SDP)**: Complies with the definition of a hub or host as defined in USB 2.0[^usb-org-battery-charging-v1.2-spec]. Maximum sourced current is 2.5mA when suspended, 100mA when connected, and 500mA when negotiated.
* **Dedicated Charging Port (DCP)**: A port that does not communicate any data, but is solely for providing power for charing (and/or operating). It has provide between 0.5 and 5A[^usb-org-battery-charging-v1.2-spec]. The DCP shorts out the D+ and D- lines, which the device at the other end of the cable can detect.
* **Charging Downstream Port (CDP)**: A mixture of the above two, it both can communicate and provide power at the same levels (1.5A at 5V) as a DCP. Has to provide between 1.5 and 5A[^usb-org-battery-charging-v1.2-spec].

{{% ref "fig-battery-charging-spec-rev-1.2-different-types-of-ports" %}} show the basic electrical wiring for the SDP, DCP and CDP ports defined by the BC 1.2 specification.

{{% figure ref="fig-battery-charging-spec-rev-1.2-different-types-of-ports" src="battery-charging-spec-rev-1.2-different-types-of-ports.webp" width="800px" caption="Diagram showing the basic electrical wiring for the various ports specified by BC 1.2." %}}

It's also important to distinguish between the following terms:

* **Attach**: The physical process of plugging in a USB cable between two ports.
* **Connect**: When the PD connects a `\(1.5k\Omega\)` pull-up resistor to either the D+ or D- line.
* **Enumerate**: The initial data exchange between the two ports across the data lines.

The PD needs to determine how much current it can draw from the upstream USB port.

{{% ref "fig-battery-charging-spec-rev-1.2-charging-downstream-port" %}} shows the internal circuitry in a Charging Downstream Port (CDP).

{{% figure ref="fig-battery-charging-spec-rev-1.2-charging-downstream-port" src="battery-charging-spec-rev-1.2-charging-downstream-port.webp" width="800px" caption="The internal circuitry connected to the D+ and D- lines in a Charging Downstream Port (CDP). Numerical values are nominal values, the USB standard instead specifies ranges[^usb-org-battery-charging-v1.2-spec]." %}}

### USB Power Delivery 1.0

_USB Power Delivery 1.0_ was released by the USB-IF in July 2012[^renesas-usb-power-delivery] which offered 5 fixed power profiles. {{% ref "usb-pd-1.0" %}} shows the voltages, currents and powers that each profile provides.

<table ref="usb-pd-1.0">
  <caption>
  
The 5 power profiles offered by USB PD 1.0[^manhatten-usb-c-power-delivery].</caption>
  <thead>
    <tr>
      <th>Profile</th>
      <th>Voltage</th>
      <th>Current</th>
      <th>Power</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>5V</td>
      <td>2A</td>
      <td>10W</td>
    </tr>
    <tr>
      <td>2</td>
      <td>12V</td>
      <td>1.5A</td>
      <td>18W</td>
    </tr>
    <tr>
      <td>3</td>
      <td>12V</td>
      <td>3A</td>
      <td>36W</td>
    </tr>
    <tr>
      <td>4</td>
      <td>20V</td>
      <td>3A</td>
      <td>60W</td>
    </tr>
    <tr>
      <td>5</td>
      <td>20V</td>
      <td>5A</td>
      <td>100W</td>
    </tr>
  </tbody>
</table>

### USB Power Delivery 2.0

### USB Power Delivery 3.0

_USB Power Delivery 3.0_ made no changes to the maximum power compared to PD 2.0/1.0 (still 100W), but did improve by adding more charging information exchange between the two ports. Information about battery charging status, failures, over-voltages, battery temperatures can be exchanged[^the-phone-talks-usb-pd-2.0-3.0-3.1].

### USB Power Delivery 3.1 

_USB PD Revision 3.1_ was released by the USB-IF in May 2021[^usb-promoter-group-pd-rev-3.1]. It increased the **max. power available from a USB port from 100W to 240W**. It keeps the original spec as per PD 3.0 as part of it's _Standard Power Range_ (SPR). Added was the _Extended Power Range_ (EPR) with new fixed voltages of 28V (140W), 36V (180W) and 48V (240W). Also added is an adjustable voltage mode that allows the device being powered to request intermediate voltages (with a 100mV resolution[^usb-promoter-group-pd-rev-3.1]) between 15V and the max. supported voltage of the charger[^usb-org-usb-pd]. The power direction was made flexible, allowing hosts and peripherals to both be sources and sinks[^usb-org-usb-pd].

## Communication Protocol

USB PD uses the two CC lines provided in the Type-C connector to perform negotiation between source and sink. The VBUS lines on the Type-C cablue plugged into a host/source remain unpowered until a device/sink is plugged in and the CC lines are pulled-down. At this point, VBUS rises to 5V. To get above 5V, more complex digital communications needs to occur between the source and sink over the CC lines.

{{% ref "usb-type-c-plug-photo" %}} is a photo of a USB Type-C plug on the end of a white cable.

{{% figure ref="usb-type-c-plug-photo" src="usb-type-c-plug-photo.jpg" width="600px" caption="Photo of a USB Type-C plug on the end of a cable." %}}

{{% ref usb-type-c-connector-pinout %}} shows the pinout for both the USB Type-C plug and the receptacle.

{{% figure ref="usb-type-c-connector-pinout" src="usb-type-c-connector-pinout.webp" width="800px" caption="Pinout for both the USB Type-C plug and receptacle[^wikipedia-usb-c]." %}}

### USB 2.0 Without PD

Before we dive into PD, let's cover what happens without PD. The most basic powering scenario with Type-C connectors is simple pull-down of the CC lines, leading to 5V being provided on VBUS at either 1.5A or 3A.

{{% ref "usb2.0-without-pd" %}} shows the basic connections on the CC lines when using USB 2.0 over a Type-C connector.

{{% figure ref="usb2.0-without-pd" src="usb2.0-without-pd.webp" width="800px" caption="Basic connection scheme for USB 2.0 without PD over a Type-C connector." %}}

The value of `\(R_p\)` is how the source/DFP advertises it's current capability. The sink/UFP always has a fixed value for `\(R_d\)` of `\(5.1k\Omega\)`. When connected together, they form a voltage-divider. The sink can measure the voltage at the center point and determine the current capability of the source. {{% ref "rp-requirements" %}} shows the requirements for `\(R_p\)`.

<table ref="rp-requirements">
  <caption>
  
The requirements for `\(R_p\)` on the source side of the cable.[^st-overview-usb-type-c-pd]</caption>
  <thead>
    <tr>
      <th>Source Current Capability</th>
      <th>Current Source to 1.7-5.5V</th>
      <th>\(R_p\) pull-up to 3.3V ±5%</th>
      <th>\(R_p\) pull-up to 4.75-5.5V</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Default USB power</td>
      <td>80µA ±20%</td>
      <td>36kΩ ±20%</td>
      <td>56kΩ ±20%</td>
    </tr>
    <tr>
      <td>1.5A @5V</td>
      <td>180µA ±8%</td>
      <td>12kΩ ±5%</td>
      <td>22kΩ ±5%</td>
    </tr>
    <tr>
      <td>3.0A @5V</td>
      <td>330µA ±8%</td>
      <td>4.7kΩ ±5%</td>
      <td>10kΩ ±5%</td>
    </tr>
  </tbody>
</table>

The Type-C cable needs to provide a pull-down resistor `\(R_a\)` on it's `VCONN` pin to signal to the source that it needs power. `\(R_a\)` must be between `\(0.8{-}1.2k\Omega\)`[^infineon-termination-resistors-for-type-c]. With this resistance, the source can easily tell the difference between which CC pin is connected to the sink and which is the `VCONN`. 

## Emarkers

_Emarkers_ are chips embedded in fancier USB Type-C cables which can inform the source or sink about their capabilities. They are typically embedded in one or both of the ends of the cable. They are required for cables that are designed to go over the standard 3A and provide up to 5A of current.

The Emarker requires power, at it uses one of the CC lines to do so. One of the CC lines is used for communication (which one depends on which way around the Type-C connector is plugged in), and the other is called `\(VCONN\)` and is used to power the Emarker.

It's a manufacturing choice about whether a cable is provided with just one Emarker at one of the cable or one at both ends. In the case of just one at one end, a separate `VCONN` wire must be run the entire length of the cable to bring power to the E-marker from the other end of the cable.

## Non-standard Implementations

### Qualcomm Quick Charge

Quick charge is designed to work with a number of different connectors, including[^qualcomm-quick-charge-faq]:

* USB Type-A
* USB Micro
* USB Type-C
* Proprietary connectors

## Example Circuits

### Getting Power From a USB Type-C Connector Without Complicated Circuitry

A typical use case when designing an electronic device is that you want it to be powered from a USB Type-C connector, acting as an UFP and power sink. You may not want the cost or complexity of adding a USB PD IC to your circuit design. What options do you have?

The simplest thing to do is to just connect `\(5.1k\Omega\)` resistors from each CC line to GND. This will allow you to draw 500mA from VBUS without any extra work. In the case where a USB Type A to Type C cable is plugged in, and the DFP is a simple USB 1.0/2.0 device, VBUS will be powered automatically and you should be able to draw 500mA without any issues. If a Type C to Type C cable is plugged in, the CC resistors will indicate to the connected DFP to power the VBUS. You can again take 500mA without any issues.

Even though USB 3.0 allows more than 500mA, with just two resistors you can't tell what is connected at the other end of the cable, and so have to design for the limiting case of the DFP being a USB1.0/2.0 device capable of only 500mA.

### USB Powered Battery Charger with the MAX14747

The Analog Devices MAX14747 is a IC which can detect a number of different USB charger types and charge a battery from the USB power source. It supports USB Battery Charger Detection Rev 1.2 but not USB PD. `\(V_{BAT}\)` can range from 0-5.5V so single Li-Po cells are supported. It can be controlled from a MCU via I2C lines.

{{% figure ref="fig-max14747-typical-application-circuit" src="max14747-typical-application-circuit.png" width="800px" caption="Typical application circuit for the Analog Devices MAX14747 IC[^analog-devices-max14747-usb-charging-ic]." %}}

### Standalone USB PD Sink Controller with the STUSB4500

The _STMicroelectronics STUSB4500_ is a USB PD standalone sink controller. Standalone refers to the fact that it has non-volatile programmable memory that is used to configure the device, meaning the STUSB4500 can run by itself without the need for a MCU to be connected to it. {{% ref "fig-stmicroelectronics-stusb4500-3d-render-wlcsp-25" %}} shows a 3D render of it in the WLCSP-25 package.

{{% figure ref="fig-stmicroelectronics-stusb4500-3d-render-wlcsp-25" src="stmicroelectronics-stusb4500-3d-render-wlcsp-25.png" width="200px" caption="The STUSB4500 in the WLCSP-25 package[^st-microelectronics-stusb4500-standalone-pd-sink]." %}}

{{% ref "fig-stmicroelectronics-stusb4500-minimal-application-schematic" %}} shows a minimal application schematic using the IC act as a USB PD power sink without any connected MCU.

{{% figure ref="fig-stmicroelectronics-stusb4500-minimal-application-schematic" src="stmicroelectronics-stusb4500-minimal-application-schematic.png" width="900px" caption="Minimal application circuit for the STMicroelectronics STUSB4500 IC. Note that it is operated as a standalone controller and there is no MCU present[^st-microelectronics-stusb4500-standalone-pd-sink]." %}}

### USB Charger Adapter Using The MAX14630

The Analog Devices MAX14630 

TODO: Finish this off.

## Connectors

Some USB Type-C connectors do not have all 24 pins available, but just enough to perform charging (basic or PD).

One example is the Molex 2171750001, as shown in {{% ref "fig-molex-2171750001-type-c-6-lead-connector-photo-and-diagram" %}}.

{{% figure ref="fig-molex-2171750001-type-c-6-lead-connector-photo-and-diagram" src="molex-2171750001-type-c-6-lead-connector-photo-and-diagram.webp" width="600px" caption="Photo and diagram of the Molex 2171750001 USB Type-C (6+18 Dummy) connector[^molex-2171750001-type-c-6-plus-18-dummy-connector-ds]." %}}

It has a description in [DigiKey](https://www.digikey.com/en/products/detail/molex/2171750001/13913745) of: "USB-C (USB TYPE-C) USB 2.0 Receptacle Connector 24 (6+18 Dummy) Position Surface Mount, Right Angle; Through Hole". The "6+18 Dummy" means only 6 of the 24 contacts are actually provided as SMD leads to the PCB. These are:

* `A9`, `B9`: VBUS
* `A5`: CC1
* `B5`: CC2
* `A12`, `B12`: GND

Having VBUS, the CC lines and GND gives you all the leads you need to perform either basic power draw or negotiate higher voltages/currents via the CC lines.

## References

[^ti-primer-on-usb-pd]: Nate Enos, Brian Gosselin. _A Primer on USB Type-C® and USB Power Delivery Applications and Requirements_ [PDF]. Texas Instruments. Retrieved 2023-07-07, from https://www.ti.com/lit/wp/slyy109b/slyy109b.pdf.
[^wikipedia-usb-c]: Wikipedia (2023, Jun 29). _USB-C_ [Web Page]. Retrieved 2023-07-07, from https://en.wikipedia.org/wiki/USB-C.
[^usb-org-usb-pd]: usb.org. _USB Charger (USB Power Delivery)_ [Web Page]. Retrieved 2023-07-07, from https://www.usb.org/usb-charger-pd.
[^usb-promoter-group-pd-rev-3.1]: USB Promoter Group. _USB Promoter Group Announces USB Power Delivery Specification Revision 3.1 - Specification defines delivering up to 240W of power over USB Type-C_ [PDF]. Retrieved 2023-07-07, from https://www.usb.org/sites/default/files/2021-05/USB%20PG%20USB%20PD%203.1%20DevUpdate%20Announcement_FINAL.pdf. 
[^st-overview-usb-type-c-pd]: STMicroelectronics. _TA0357 - Overview of USB Type-C and Power Delivery technologies_. Retrieved 2023-07-08, from https://www.st.com/resource/en/technical_article/ta0357-overview-of-usb-typec-and-power-delivery-technologies-stmicroelectronics.pdf.
[^infineon-termination-resistors-for-type-c]: Infineon (2015, Apr 17). _Termination Resistors Required for the USB Type-C Connector – KBA97180_ [Forum Post]. Retrieved 2023-07-08, from https://community.infineon.com/t5/Knowledge-Base-Articles/Termination-Resistors-Required-for-the-USB-Type-C-Connector-KBA97180/ta-p/253544.
[^consumer-org-eus-charging-port-rules]: Nick Gelling (2022, Jun). _Europe's new universal charging port rules: how will they affect us?_ [News Article]. consumer. Retrieved 2023-07-09, from https://www.consumer.org.nz/articles/europes-new-universal-charging-port-rules-how-will-they-affect-us. 
[^renesas-usb-power-delivery]: Renesas. _USB Power Delivery: Enhanced Convenience in USB Charging_ [Web Page]. Retrieved 2023-07-09, from https://www.renesas.com/us/en/support/engineer-school/usb-power-delivery-01-usb-type-c.
[^manhatten-usb-c-power-delivery]: manhatten. _USB-C Power Delivery_ [Web Page]. Retrieved 2023-07-09, from https://manhattanproducts.eu/pages/usb-c-pd-charging-everything-you-need-to-know.
[^qualcomm-quick-charge-faq]: Qualcomm. _Qualcomm Quick Charge FAQs_ [Web Page]. Retrieved 2023-07-09, from https://www.qualcomm.com/products/features/quick-charge/faq.
[^the-phone-talks-usb-pd-2.0-3.0-3.1]: The Phone Talks. _USB PD 2.0 vs 3.0 vs 3.1 Comparison - How Far Have We Come?_ [Web Page]. Retrieved 2023-07-09, from https://www.thephonetalks.com/usb-pd-2-0-vs-3-0-vs-3-1/.
[^analog-devices-max14747-usb-charging-ic]: Maxim (now Analog Devices) (2017, Nov). _MAX14746/MAX14747 - USB Detection with Smart Power Selector Li+ Chargers_ [Datasheet]. Retrieved 2023-07-26, from https://www.analog.com/media/en/technical-documentation/data-sheets/MAX14746-MAX14747.pdf. 
[^st-microelectronics-stusb4500-standalone-pd-sink]: STMicroelectronics (2022, Nov). _STUSB4500 - Standalone USB PD sink controller with short-to-VBUS protections_ [Datasheet]. Retrieved 2023-07-26, from https://www.st.com/resource/en/datasheet/stusb4500.pdf. 
[^eaton-usb-charging-and-power-delivery]: Eaton (2023). _USB Charing and Power Delivery_. Retrieved 2023-07-28, from https://tripplite.eaton.com/products/usb-charging.
[^usb-org-battery-charging-v1.2-spec]: usb.org (2012, Mar 15). _Battery Charging Specification (Including errata and ECNs through March 15, 2012) - Revision 1.2_. Retrieved 2023-07-29, from https://www.usb.org/document-library/battery-charging-v12-spec-and-adopters-agreement.
[^molex-2171750001-type-c-6-plus-18-dummy-connector-ds]: Molex. _TYPE C 6 PIN TOP MOUNT SMT - Product Customer Drawing_ [Mechanical Drawing]. Retrieved 2023-08-02, from https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/salesdrawingpdf/217/217175/2171750001_sd.pdf.
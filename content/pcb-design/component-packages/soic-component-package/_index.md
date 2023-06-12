---
authors: [ "Geoffrey Hunter" ]
categories: [ "Electronics", "PCB Design", "Component Packages" ]
date: 2015-01-21
description: "Synonyms, variants, pitches, pin numbering, mechanical drawings, recommend footprints and more info about the SOIC range of component packages."
draft: false
lastmod: 2022-03-08
tags: [ "component packages", "PCB design", "SOIC", "R-PSDO", "S8", "WSON", "S8E", "SO-4", "SOIC-4", "optical isolators" ]
title: "SOIC Component Package"
type: "page"
---

## Overview

<table>
    <thead>
        <tr>
            <th width="100px">Name</th>
            <th width="600px">SOIC (Small Outline Integrated Package)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Synonyms</td>
            <td>

* 11-4M1S (Toshiba SO-4, 4.55mm wide body)[^bib-toshiba-tlp185-ds]
* 751EP (onsemi SOIC4 W[^bib-on-semiconductor-bridge-rectifier])
* R-PDSO (JEDEC wide body SOIC, 7.5mm width, 0.65mm pitch)
* S8 (SOIC-8, Analog Devices)
* S8E (Linear Technologies, SOIC-8 with exposed pad)
* SO (ST Microelectronics)
* SOIC8E (SOIC-8N with exposed pad, Monolithic Power Solutions[^bib-mps-mp2497-a-ds])
* SOT162-1 (SOIC-16W, NXP[^bib-nxp-sot162-1])
* SSOP4/LSOP04 (onsemi, SO-4, 7.5mm wide body)[^bib-onsemi-fodm1009-ds]
* WSON (SST, this is a package which shares the same footprint as a SOIC but has a smaller height, not to be confused with the different SON package)
</td>
        </tr>
        <tr>
            <td>Similar To</td>
            <td>

[SOJ](../soj-soijc-component-package)
            </td>
        </tr>
        <tr>
            <td>Variants</td>
            <td>The SOIC family contains packages with a varying number of pins. There are also two width’s for SOIC packages, narrow width (3.9mm wide body, SOICx_N) and wide width (7.5mm wide body, SOICx_W). The width is usually expressed by the addition of _N or _W to the end of the package name. If the width is not mentioned, it is most likely going to be narrow width.</td>
        </tr>
        <tr>
            <td>Mounting</td>
            <td>SMD</td>
        </tr>
        <tr>
            <td>Pin Count</td>
            <td>8, 14, 16, 18, 20, 24, 28, 32</td>
        </tr>
        <tr>
            <td>Pitch</td>
            <td>

* 0.65mm (e.g. R-PDSO)
* 1.27mm (50mill)
</td>
        </tr>
        <tr>
            <td>Solderability</td>
            <td>Relatively easy to hand solder compared to other SMD packages.</td>
        </tr>
        <tr>
            <td>Thermal Resistance</td>
            <td>Depends on variant, see below.</td>
        </tr>
        <tr>
            <td>Package LxWxH</td>
            <td>Length and width depends on variant, height is usually between 1.50-2.54mm.</td>
        </tr>
        <tr>
            <td>Typical PCB Land Area</td>
            <td>Depends on variant, see below.</td>
        </tr>
        <tr>
            <td>3D Models</td>
            <td>
n/a
</td>
        </tr>
        <tr>
            <td>Common Uses</td>
            <td>

* Linear regulators.
* Drivers/buffers.
* High-power MOSFETs (normally in a SOIC-8N, with one pin for the gate, and either 3 or 4 pins for the drain and source).
</td>
        </tr>
    </tbody>
</table>

## Overview

{{% aside type="warning" %}}
There are are three different widths of SOIC packages, all which can be referred to as just SOIC by manufacturers in component datasheets! When designing a PCB, make sure to double-check the exact package width matches the PCB footprint/land pattern you've chosen.

1. Package body width of 3.80mm (0.150"). JEDEC standard, commonly used for SOIC packages with a small pin count (16 or less).
1. Package body width of 5.30mm (0.208"). EIAJ standard[^bib-dexpcb-soic], used for SOIC packages with higher pin counts (>16) or for isolated ICs (e.g. Maxim package `SOIC [W8]`[^bib-maxim-soic-w8]).
1. Package body width of 7.52mm (0.300"). JEDEC standard, commonly called SOIC Wide or `SOIC-W` (e.g. Maxim package `SOIC (W)` variant `W20+6`)[^bib-maxim-soicw-20-28].

More on these different width SOIC packages below.
{{% /aside %}}

## SOIC (JEDEC, 0.150" Package Body Width)

The JEDEC version of the `SOIC` (a.k.a `SOIC-xN` (SOIC narrow)) family of packages is governed by the JEDEC MS-012-AA standard. There are non-exposed (normally just referred to as SOIC-x or SOIC-xN) and exposed pad versions (which are normally indicated with an "E" in the package name[^bib-mps-mp2497-a-ds]). 

The dimensions for the `SOIC-8N` package are shown below:

{{% figure src="soic-8-component-package-dimensions.png" width="555px" caption="The dimensions for the SOIC-8N component package." %}}

The dimensions for the `SOIC-16N` component package are shown below:

{{% figure src="soic-16-component-package-dimensions.jpg" width="575px" caption="The dimensions for the SOIC-16N component package." %}}

Land area:

* SOIC-8: 29.4mm2

Thermal resistance:

* SOIC-8: 70.6K/W (pads only, no copper fill)
* SOIC-8: 55K/W (6cm2 of copper, ground pins attached internally to die)
* SOIC-8: 33.5K/W (1 square inch of copper surrounding package, connected to ground)

## SOIC (EIAJ, 0.208" Package Body Width)

Confusingly, the EIAJ standard defines a different body width of 5.3mm (0.208") for the `SOIC`` package, compared to the 3.8mm body width as defined in the JEDEC standard[^bib-dexpcb-soic]. Generally used for ICs with a larger number of pins (>16).

## SOIC-W (JEDEC, 0.300" Package Body Width)

The `SOIC-W` (SOIC wide) family of packages is governed by the JEDEC MS-013 and IEC 075E03 standards. NXP's `SOT-162-1` package is a SOIC-16W[^bib-nxp-sot162-1].

| Package Name | Land Area
|--------------|-----------------------------------
| SOIC-16W     | 136.3mm² (11.9x11.45mm)[^bib-nxp-sot162-1]
| SOIC-28W     | 186.4mm² (10.3x18.1mm)

## Pitch

Most `SOIC` packages have a pitch of 1.27mm (50mil) and usually have Gullwing leads. When used for regulators, sometimes the many ground pins are connected internally to the die attach flag, providing better heat sinking capabilities. SOIC packages use _leadframe_ technology.

The `SOIC` package `R-PDSO` defined by JEDEC has a non-standard pitch of 0.65mm (and the standard wide body width of 7.5mm).

## Pin Numbering

Pin numbering is the same as a `DIP` package, in that pin 1 is at the top left, and then pins are numbered sequentially down the left-hand side, then up the right hand-side.

## Polarity Marks

There are three ways of indicating the polarity on a `SOIC` package. The first two, a dot or a notch, indicate pin 1 or the top of the chip. The third way is not so obvious, and features a bevelled edge along the side that pin 1 is on (so for `SOIC-8`, the bevelled edge would be on the side with pins 1 to 4).

## Related Packages

The `WSON` package by SST is lower in height than a standard `SOIC` package, but is designed to use the same PCB footprint.

## Adapter PCBs

Adapter PCBs for the `SOIC` family of packages are widely available due to the popularity of the package.

SparkFun makes a `SOIC-8` to `DIP-8-300` adapter PCB.

{{% figure src="soic-8-component-package-sparkfun-breakout-board.jpg" width="272px" caption="A SOIC-8 to DIP-8-300 adapter PCB by SparkFun." %}}

## Thermal Resistance And Power Dissipation

This graph shows the maximum power dissipation for the `SOIC-8N` component package, for various PCB copper areas.

{{% figure src="maximum-power-dissapation-graphs-so-8.png" width="701px" caption="Maximum power dissipation graphs for the SOIC-8N component package." %}}

## Standard Pinout For MOSFETs

The `SOIC-8` component package is commonly used for medium-power N and P-channel MOSFETs. Most of these MOSFETs have the exact same pinout (both N and P-Channels!), as shown in the below diagram.

{{% aside type="note" %}}
As far I'm aware, this is not specified in any standard, but is just an industry default. Also, this only applies to `SOIC-8` packages with 1 MOSFET inside them.
{{% /aside %}}

{{% figure src="soic-8-component-package-standard-mosfet-pinout.png" width="334px" caption="The standard pinout for a single MOSFET (N or P-channel) in a SOIC-8 package." %}}

Examples that follow this pinout include the [ST STS25NH3LL (N-channel)](https://www.sparkfun.com/datasheets/Robotics/sts25nh3ll.pdf), the [International Rectifier IRF8721PbF-1 (N-channel)](http://www.irf.com/product-info/datasheets/data/irf8721pbf-1.pdf), and the [Vishay SI9407BDY-T1-GE3 (P-channel)](http://www.vishay.com/docs/69902/si9407bd.pdf).

## SOIC-4 (SO-4)

The `SO-4` package is quite unique from other `SO` packages. It typically has the same mechanical dimensions as a `SO-6` package, but has the two middle pins on either side removed. Typically the `SO-6` pin numbering is also kept, such that the remaining pins are numbered 1, 3, 4 and 6. Due to the large clearances between the pins and on the package, this `SO-4` package is used for optical isolators.

The `SO-4` package is different to the `SOIC-4` package, even though these two different names refer to the same package at higher pin counts.

ON Semiconductor uses the case code `751EP` for the `SOIC-4W` package[^bib-on-semiconductor-bridge-rectifier].

## References

[^bib-on-semiconductor-bridge-rectifier]: On Semiconductor (now onsemi) (2019, Sep). _Bridge Rectifiers, 0.5 A: MB10S (datasheet)_. Retrieved 2022-03-08, from https://www.mouser.com/datasheet/2/308/1/MB10S_D-2314909.pdf.
[^bib-toshiba-tlp185-ds]: Retrieved 2021-12-08, from https://media.digikey.com/pdf/Data%20Sheets/Toshiba%20PDFs/TLP185_04-27-17.pdf.
[^bib-onsemi-fodm1009-ds]: Retrieved 2021-12-08, from https://nz.mouser.com/datasheet/2/308/1/FODM1009_D-2313636.pdf.
[^bib-mps-mp2497-a-ds]: Monolithic Power Solutions (2012, May 30). _MP2497-A: 3A, 50V, 100kHz Step-Down Converter with Programmable Output OVP Threshold_. Retrieved 2022-01-20 from https://www.monolithicpower.com/en/documentview/productdocument/index/version/2/document_type/Datasheet/lang/en/sku/MP2497A/document_id/1972.
[^bib-nxp-sot162-1]: NXP (2016, Feb 8). _SOT162-1: Plastic small outline package; 16 leads; body width 7.5 mm (package information)_. Retrieved 2022-01-25, from https://www.nxp.com/docs/en/package-information/SOT162-1.pdf.
[^bib-maxim-soicw-20-28]: Maxim (2013, Jan 17). _Package Outline: 20L, 28L SOIC .300"_. Retrieved 2022-03-08, from https://pdfserv.maximintegrated.com/package_dwgs/21-0703.PDF.
[^bib-maxim-soic-w8]: Maxim. _Package Land Pattern: [W8] 0.208" SOIC, 8 Leads_. Retrieved 2022-03-08, from https://pdfserv.maximintegrated.com/land_patterns/90-0258.PDF.
[^bib-dexpcb-soic]: DEX PCB. _Device Overview > SOIC_. Retrieved 2022-03-08, from https://dexpcb.com/manual/device_overview.htm.
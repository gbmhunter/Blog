---
authors: [ "Geoffrey Hunter" ]
categories: [ "Electronics", "PCB Design", "Component Packages" ]
date: 2015-04-27
draft: false
lastmod: 2024-04-19
tags: [ "component packages", "PCB design", "SOT-723", "small-outline", "transistor" ]
title: SOT-723 Component Package
type: page
---

## Overview

{{% figure src="_assets/sot-723-component-package-3d-render.jpg" width="200px" float="right" caption="A 3D render of the SOT-723 component package."  %}}

SOT-723 (Small Transistor Outline 723) is a 3-lead SMD component package. SOT-723 is used for things such as MOSFETs, digital transistors (BRTs), small-signal switching diodes, low power rectifiers and ESD diodes.

## Synonyms

* VMT3: Rohm Semiconductor's name[^rohm-semi-rsm002n06-mosfet-ds].
* Case 631AA: onsemi's name[^onsemi-esd7c-szesd7c-series-esd-diode].
* SC-105AA: Rohm Semiconductor's name[^rohm-semi-rsm002n06-mosfet-ds].
* SOT-723
* SOT-723-3

## Dimensions

Here are the dimensions and a recommended footprint for the SOT-723 component package.

{{% figure src="_assets/sot-723-component-package-dimensions-and-footprint.png" width="686px" caption="Dimensions and a recommended footprint for the SOT-723 component package. Image from http://www.onsemi.com/pub_link/Collateral/ESD7C3.3D-D.PDF."  %}}

The major dimensions from the above diagram are as follows:

| Dimension Name         | Dimension Letter | Value  |
|------------------------|------------------|--------|
| Body length            | \(D\)            | 1.20mm |
| Body width             | \(E\)            | 0.80mm |
| Body width incl. leads | \(H_e\)          | 1.20mm |
| Pitch                  | \(e\)            | 0.80mm |

## Recommended Land Pattern

{{% figure src="_assets/sot-723-recommended-land-pattern-onsemi.png" width="800px" caption="The recommended land pattern for the SOT-723 component package from onsemi[^onsemi-esd7c-szesd7c-series-esd-diode]." %}}

PCB Land Area (package only) = \(1.44mm^2\)  
PCB Land Area (incl. recommended footprint) = \(1.88mm^2\)

## Similar To

* [SOT-23](/pcb-design/component-packages/sot-23-component-package/)
* [SOT-523F](/pcb-design/component-packages/sot-523f-component-package/)

## References

[^onsemi-esd7c-szesd7c-series-esd-diode]: onsemi. _ESD Protection Diode - Micro−Packaged Diodes for ESD Protection - ESD7C, SZESD7C SERIES_ [datasheet]. Retrieved 2024-04-19, from https://www.onsemi.com/pdf/datasheet/esd7c3.3d-d.pdf.
[^rohm-semi-rsm002n06-mosfet-ds]: Rohm Semiconductor (2016). _RSM002N06 - Nch 60V 250mA Small Signal MOSFET_ [datasheet]. Retrieved 2024-04-19, from https://fscdn.rohm.com/en/products/databook/datasheet/discrete/transistor/mosfet/rsm002n06-e.pdf.
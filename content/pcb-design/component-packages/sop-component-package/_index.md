---
authors: [Geoffrey Hunter]
categories: [Electronics, PCB Design, Component Packages]
date: 2015-04-06
description: Dimensions, variants, recommended footprints, typical applications and more info about the SOP component package.
draft: false
lastmod: 2024-04-15
tags: [electronics, component packages, PCB design, SOP, SOP-4, relays, DUB, SOP-8, Texas Instruments]
title: SOP Component Package
type: page
---

## Overview

{{% figure src="sop-4-component-package-3d-model.jpg" width="200px" float="right" caption="A 3D model of the SOP-4 component package. Image from www.digikey.com." %}}

SOP (Small Outline Package) is a SMD component package. The `SOP` is the SMD equivalent of the `DIP` component package, and has the same pitch of 2.54mm (100mil).

## Synonyms

* 11-5H1S: Toshiba's package code for it's 2.54SOP4[^toshiba-2.54sop4].
* 2.54SOP4: Toshiba variant of the SOP-4[^toshiba-2.54sop4].
* DUB: TI SOP-8[^ti-iso1050-ds]

## Similar To

* SSOP (Shrink Small Outline Package): A smaller version of the SOP package.

## SOP-4

The `SOP-4` is an easy to solder, medium sized, 4-pin SMD package. Commonly used for small solid-state relays (Vishay makes quite a few of them). Related to `SOP-4L`, which is the same width, but longer.

{{% figure src="sop-4-component-package-photo.jpg" width="356px" caption="A photo of the SOP-4 component package." %}}

### Dimensions

{{% figure src="sop-4-component-package-dimensions-and-land-pattern.png" width="500px" caption="The dimensions and recommended land pattern for the SOP-4 component package. Image from http://www.everlight.com/datasheets/EL452-G.pdf." %}}

## 2.54SOP4

The 2.54SOP4 is a SOP-4 variant from Toshiba[^toshiba-2.54sop4]. It has slightly different body dimensions from the SOP-4.

### Dimensions

The 2.54SOP4 body is 4.4mm wide (the edges with the leads) and 3.9mm long. It is 2.1mm high from PCB to top of package[^toshiba-2.54sop4].

## SOP-8

{{% figure src="sop-8-package-dimensions-ti.png" width="600px" caption="The package dimensions for the SOP-8 component package from TI[^ti-iso1050-ds]." %}}

## Common Uses

Common uses:

* Solid-state relays.
* Optocouplers.
* Optically-isolated transceivers.

## References

[^ti-iso1050-ds]: Texas Instruments (2023, Oct). _ISO1050 Isolated CAN Transceiver_ [datasheet[. Retrieved 2024-04-15, from https://www.ti.com/lit/ds/symlink/iso1050.pdf.
[^toshiba-2.54sop4]: Toshiba. 2.54SOP4. _2.54SOP4_. Retrieved 2024-04-15, from https://toshiba.semicon-storage.com/ap-en/semiconductor/design-development/package/detail.2.54SOP4.html.
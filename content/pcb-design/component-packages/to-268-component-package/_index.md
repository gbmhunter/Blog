---
aliases: [
  /pcb-design/component-packages/d3pak-to-268-component-package/ # Moved from this URL 2024-04-08
]
authors: [Geoffrey Hunter]
categories: [Electronics, PCB Design, Component Packages]
date: 2015-04-07
draft: false
lastmod: 2024-04-08
tags: [D3PAK, TO-268, DDDPAK, Decawatt, TO-268AA, TO-268-3, component packages]
title: TO-268 (D3PAK) Component Package
type: page
---

## Overview

{{% figure src="_assets/d3pak-to-268-component-package-photo.jpg" width="150px" float="right" caption="Photo of the D3PAK (TO-268) component package." %}}

The TO-268 (Transistor Outline 268, commonly known as D3PAK) is a SMD component package. It is the third in the series of "DPAK" packages, the first being [TO-252 (DPAK)](/pcb-design/component-packages/to-252-component-package/) and the second being [TO-263 (D2PAK)](/pcb-design/component-packages/to-263-component-package/). The D3PAK name stands for "decawatt 3 package" and has the highest power dissipation rating out of the three. Unlike the TO-263 package, the TO-268 package only comes in one variant with 3 pins (as far as I can tell). This variant can be referred to as TO-268-3.

It is designed to have a really low thermal resistance so that it can be used in high power applications. The larger die also means that MOSFETs in this package can have lower \(R_{DS(ON)}\) values, resulting in less power dissipation for the same current.

I have only ever seen this in the 3-pin variant (called TO-268-3). Common uses include Microsemi power MOSFETs, Microsemi power diodes, and Microsemi power IGBTs.

## Synonyms
  
* TO-268 (Transistor Outline 268)
* D3PAK
* DDDPAK
* Decawatt Package 3
* TO-268AA (TO-268-3)

## Package Dimensions

Shown below are the package dimensions.

{{% figure src="_assets/to-268-3-component-package-dimensions.png" width="800px" caption="Dimensions for the D3PAK (TO-268) component package." %}}

## Thermal Resistances

* \(T_{JC}: 0.24-1.18^{\circ}{\rm C}/W\)
* \(T_{JA}: 40^{\circ}{\rm C}/W\)
* \(T_{JA}: 21.9^{\circ}{\rm C}/W\) (13.5x17.5mm copper pad)
* \(T_{JA}: 18^{\circ}{\rm C}/W\) (19x29.4mm copper pad)

## Solderability

Easy to solder by hand, as long as you have a decent powered soldering iron for the central thermal pad. Easy to solder with infrared and reflow techniques.

## Recommended Land Pattern

Shown below is the recommended land pattern.

{{% figure src="_assets/to-268-component-package-land-pattern.png" width="500px" caption="Recommended land pattern for the D3PAK (TO-268) component package." %}}

## Recommended Stencil

Shown below is the recommended stencil pattern.

{{% figure src="_assets/to-268-component-package-recommended-stencil-pattern.png" width="500px" caption="Recommended stencil pattern for the D3PAK (TO-268) component package." %}}

## Similar To

* [TO-252 (DPAK)](/pcb-design/component-packages/to-252-component-package/)
* [TO-263 (D2PAK)](/pcb-design/component-packages/to-263-component-package/)
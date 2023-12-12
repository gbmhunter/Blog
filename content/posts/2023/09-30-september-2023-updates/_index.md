---
authors: [ Geoffrey Hunter ]
categories: [ Posts, Updates ]
date: 2023-09-30
description: Blog updates during September 2023.
draft: false
images: [ ]
lastmod: 2023-09-30
tags: []
title: September 2023 Updates
type: post
---

* A lot of work was done on [NinjaTerm](https://ninjaterm.mbedded.ninja/)!
    * Migrated from an Electron App to a PWA (Progressive Web App).
    * The homepage needed some love, half the .gifs were broken and showed out-of-date content. I embraced the dark side and [remade the homepage](https://ninjaterm.mbedded.ninja/) with a dark theme that matched the theme of the app. I also migrated it from using GitHub pages to being part of the app itself, meaning only 1 website to deploy, not two.
    {{% figure src="ninjaterm-homepage-old-new-comparison.webp" width="900px" %}}
    * Added support for more ANSI Escape Codes.

* Added info on [stuck (hung) I2C buses and how to recover from them](/electronics/communication-protocols/i2c-communication-protocol/#stuck-i2c-buses).
    {{% figure src="stuck-i2c-buses-screenshot.png" width="600px" %}}

* Added info on [I2C start conditions, address bytes, data bytes and stop conditions](/electronics/communication-protocols/i2c-communication-protocol/#protocol-format).
    {{% figure src="i2c-protocol-format-screenshot.png" width="600px" %}}

* Added info on providing clearance on PCBs for screw heads.

* Added more info to the [Current Sensing page](/electronics/circuit-design/current-sensing/). 

* Added new page on [hall effect sensors](/electronics/components/hall-effect-sensors/).
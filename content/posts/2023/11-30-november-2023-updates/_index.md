---
authors: [ Geoffrey Hunter ]
categories: [ Posts, Updates ]
date: 2023-11-30
description: Blog updates during November 2023.
draft: false
images: []
lastmod: 2023-11-30
tags: []
title: November 2023 Updates
type: post
---

* Just like last month, this month I was (almost) solely focused on [NinjaTerm](https://ninjaterm.mbedded.ninja/) development. We went from `v4.7.0` through to `v4.12.0` in the month of November. Updates to NinjaTerm are highlighted below.

* Added glyphs to the Unicode PUA range of the NinjaTerm font to show control characters and hex codes.
    {{% figure src="control-char-and-hex-code-glyphs.gif" width="700px" %}}

* Added logging functionality.
    {{% figure src="logging.gif" width="700px" %}}

* Last serial port details and connection state are remembered across App reloads, and NinjaTerm can automatically reconnect to previously used serial port.

* Added ability for NinjaTerm to reopen serial port (when available) after unexpected closure.

* Added ability to filter rows of terminal text.
    {{% figure src="filtering.gif" width="700px" %}}

* Miscellaneous bug fixes.

* One change with this blog is that I started playing around with the idea of adding ads. I personally don't like ads but they might help pay for the upkeep of this site (domain registration, DNS, hosting, and software licenses for designing things like the diagrams). I have enabled Google AdSense. In it's current form the ads are pretty horrible (e.g. disruptive pop-ups), so I'll be tuning them and making sure they are not so invasive in the near future. If they don't end up making much money, I might remove them altogether.
    {{% figure src="google-adsense.png" width="700px" %}}
    
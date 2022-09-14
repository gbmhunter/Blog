---
authors: [ "Geoffrey Hunter" ]
categories: [ "Posts", "Updates" ]
date: 2022-09-30
description: "Blog updates during September 2022."
draft: false
images: [ ]
lastmod: 2022-09-30
tags: []
title: "September 2022 Updates"
type: "post"
---

## Updates This Month

* Create a new page for the BJT common-collector amplifier.

* Updates to the Kalman Filter page.

* Upgraded the Netlify build image from Ubuntu Xenial 16.04 (which is deprecated and was going to be unsupported in November 2022) to Ubuntu Focal 20.04. This initially caused a hugo build failure, which was resolved by adding `GEM_PATH` to the `security: exec: osEnv:` section of the `config.yaml`.
    {{% figure src="adding-gem-path-to-config-yaml.png" width="400px" %}}
---
title: Unstable release SDAPS 1.9.12
type: post
date: 2023-03-19
---

This release contains an urgent bugfix for the detection code. In addition to
this, the build system has been moved to use meson, as the old build system is
deprecated and got harder to maintain in the long run.

See the README for build instructions. To enable the LaTeX class build and
installation, pass -Dlatex=true to meson setup.

<!--more-->

Important changes:

 - Fix checkbox position detection
 - Change build system to meson
 - Move LaTeX translations into sdaps-class repository

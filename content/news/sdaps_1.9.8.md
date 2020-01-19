---
title: Unstable release SDAPS 1.9.8
type: post
date: 2020-01-19
---

This release breaks backward compatibility in a few small ways. For example
the "style" parameter of the LaTeX class was renamed to "sdaps_style".

Also unrelated to this release but still noteworthy is that the LaTeX class
has been uploaded to CTAN and has also been added to TeX Live. There will
be a few more related changes to this so that SDAPS will pick up the system
version of the LaTeX class by default.

<!--more-->

Important changes:

 - LaTeX: Class now takes sdaps_style as argumen instead of style
 - LaTeX: Class will now always report the correct page count (#192)
 - LaTeX: Improve spacing of multiline choicequestion items
 - LaTeX: Disable header repetition in rangearray/markgroup questions (#21)
 - Fix issue with SQL schema (#189)
 - Fix issues with transformation matrix calculation (#195)
 - Allow adjusting corner marks in GUI (#194)
 - Allow running box recognition from GUI

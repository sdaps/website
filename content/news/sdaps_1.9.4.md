---
title: Unstable release SDAPS 1.9.4
type: post
date: 2018-11-07
---

This release brings some larger changes to the LaTeX class making it able to
layout languages that are written from right to left. This change is
quite invasive, as it required modifying the metadata writing to
include further numbering to ensure the correct order of information.

The layout of the choicequestion environment was also changed slightly.

<!--more-->

Important changes:

 - Ensure box IDs are unique (#142)
 - Fix variable name handling of the single choice questions (#141)
 - Make "verified" a property of each image, all images need to be marked as verified
 - Add support for right to left languages:

   - Implement RTL switching in LaTeX
   - Make metadata file line numbered
   - Fix anotation line length (and indentation for RTL languages)
   - Rework choicequestion layout

New and updated languages:
 - Romanian
 - Sinhala
 - Spanish

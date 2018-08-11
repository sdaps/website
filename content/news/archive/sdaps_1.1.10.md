---
title: Overview of Changes in SDAPS 1.1.10
date: 2015-05-19
---
Again, mostly a bugfix release. One thing to note is that if you are using small fields (i.e. choiceitemtext) is that single characters/digits can sometimes be detected as only dirty. So if you want to use fields with only a single character, then it is likely a good idea to fine tune the minimum size of writing and other aspects of freeform field recognition.
<!--more-->

Important changes:

- latex: Fix search paths (#63)
- latex report: Fix formatting issues
- gui: Fix broken display in some corner cases (#67)
- gui: Ensure dialogs are on top of the main window (#66)
- csv: Options to export recognition quality
- Allow filtering based on string replacements for freeform fields (#69)
- latex: Fix encoding issues for some special characters (#70)
- latex: Allow smaller choiceitemtext elements (#68)

New and updated languages:

- French
- German
- Portuguese (Brazil)
- Dutch
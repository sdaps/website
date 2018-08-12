---
title: Overview of Changes in SDAPS 1.1.2
date: 2013-10-27
---
This release brings a lot of small improvements, but also some new features. The main new feature is the addition of a "convert" module, which can be used to convert non-monochrome scans into monochrome images for later processing. This module is also able to apply 3D-transformations as they are neccessary when the source image was done using a camera.
 This new module requires OpenCV. Note that using a feed scanner is still prefered to this method.
<!--more-->

Other changes include:

- LaTeX: Fix compilation of large documents (by suppressing position output)
- LaTeX: Fix multicolumn items and cline at the start of choicequestions
- ODT: Custom styling in answers and question is now possible.
- Various improvements and fixes in the corner mark detection code
- New "custom" style which can be used when customizing the behaviour of SDAPS
- A PDF with annotations will now be created if there was an error during setup
- An issue in the base dir search code that affected OSX has been fixed

New and updated translations:

- Arabic

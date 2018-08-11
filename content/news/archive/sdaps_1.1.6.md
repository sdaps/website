---
title: Overview of Changes in SDAPS 1.1.6
date: 2014-10-25
---
This release adds support to use QR code instead of Code-128. The main advantage is that QR-Code contains redundancy so that recognition should be more reliable even with bad scans. Another important change is that it is now possible to select different modes for checkbox detection without modifying the source code. This should simplify the usage of SDAPS in certain cases.
Feedback for optimizing the different modes is of course welcome. The thresholds have not been tested extensively.
<!--more-->

Important changes:

- Support for QR-Code based IDs has been added ("qr" style)
- csv export: Allow export of freeform textboxes as images
- Updated example and testcase for newer multicol versions
- tex: Fix writing sdaps file for all macros.
- Allow selection of different checkbox detection modes.

New and updated languages:

- Portoguese (copy of Portoguese (Brazil))
- German

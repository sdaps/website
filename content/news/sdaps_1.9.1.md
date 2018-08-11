---
title: Unstable release SDAPS 1.9.1
date: 2017-08-20
---
This is a new unstable release pulling in a lot of fixes. Please note that
it is incompatible to the previous 1.9.0 release as the fixes to the class
will result in the survey IDs to become different.
<!--more-->

Important changes:

* Fix repetition of questionnaires
* Fixes to make class work with TeXlive 2017-08-08
* Fix build to not install the TeX class in the users home directory
* Fix LaTeX report generation (#108)
* Fixes and tests of CSV import and exporter
* Improve CSV export to include more information about sheets
* Change default style to QR code
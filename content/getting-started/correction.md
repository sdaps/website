---
title: Manual error correction
layout: single
---

### Manual correction

Sometimes the computer might not correctly identify the state of a checkbox
(SDAPS sometimes has some trouble because of the feature to uncheck a box by
filling it out).

To correct any errors we can use the graphical user interface. We start it using

``` bash
$ sdaps gui /tmp/project
----------------------------------
- SDAPS -- gui
----------------------------------
```

There is a much more [complete section](/documentation/gui) about it. You can quickly go trough
all images and correct any errors using the mouse. When the view is focused
you can go forward/backward using `Enter` and `Shift`+`Enter`.

There is an estimation for the quality of the recognition. You can sort the
data using this estimation and only go trough the first couple of pages. The
amount of time to spend on this will depend on the required accuracy.

# Overview

![](/images/sdaps-steps-0005.png)

The following topics are covered:

 * [Designing the Questionnaire](../design)
 * [Creating a SDAPS Project](../setup) (this page)
 * [Printing and Scanning](../print-scan)
 * [Adding Scans to a Project](../add)
 * [Running the optical mark recognition](../recognize)
 * [Manual error correction](../correction)
 * [Creating a report and exporting data](../export)
 * [Other things to try](../more) (this page)


---
title: Running the optical mark recognition
layout: single
---

The next step is to run the optical mark recognition. This works using the
`recognize` command. So from the command line again we run:

``` bash
$ sdaps recognize /tmp/project
-------------------------------------------------
- SDAPS -- recognize
-------------------------------------------------
3 sheets
|#################################| 100% 00:00:02
0.887902 seconds per sheet
```

This step takes longer as the recognition algorithm needs to do its work for
each image. The progress bar shows how much time it is expected to take.
Usually it will take less than a second for a two page questionnaire.


# Overview

![](/images/sdaps-steps-0004.png)

The following topics are covered:

 * [Designing the Questionnaire](../design)
 * [Creating a SDAPS Project](../setup)
 * [Printing and Scanning](../print-scan)
 * [Adding Scans to a Project](../add)
 * [Running the optical mark recognition](../recognize) (this page)
 * [Manual error correction](../correction)
 * [Creating a report and exporting data](../export)
 * [Other things to try](../more)


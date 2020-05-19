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



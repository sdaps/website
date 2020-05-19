---
title: Exporting Data from a Project
layout: single
---

## Creating a PDF report

To create a PDF report with the results simply run:

``` bash
$ sdaps report reportlab /tmp/project
----------------------------------
- SDAPS -- report
----------------------------------
```

It creates a PDF file `report_1.pdf`. Have a look at the file; you can also
[download the report](/files/example_report.pdf) that will be created
for the example data.

Note that we can also do partial reports by using filters. Just a quick
example (please refer to the rest of the documentation for an explanation):

``` bash
$ sdaps report tex /tmp/project -f '_1_2_3 == 5'
--------------------------------------------
- SDAPS -- report_tex
--------------------------------------------
```

This filters for question 1.2.3 (ease of use of LaTeX) and the rightmost
choice "easy".

## CSV export

Obviously sometimes it might be necessary to feed the data into another
program. For this the CSV export command was created:

``` bash
$ sdaps export csv /tmp/project
--------------------------------------------
- SDAPS -- csvdata_export
--------------------------------------------
```

A file called `data_1.csv` will be created in the project directory.


## LaTeX based report

You can create a report that is rendered using LaTeX.

```bash
$ sdaps report tex /tmp/project
```

{{< warning title="Attention" >}}This command requires the siunitx LaTeX
package to work properly.{{< /warning >}}

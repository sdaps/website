---
title: Setting up a SDAPS Project
layout: single
---

{{< warning title="Attention" >}}It is best to use the `example.tex` from this page and not a
modified version! If you modify the document the example scan will not work
later on!{{< /warning >}}

Once we are happy with the questionnaire, we can create the survey directory
that SDAPS uses to store all the data that belongs to the project.

This is the first time that we need to run an SDAPS command. The syntax for
the command is generally the following:

```bash
$ sdaps COMMAND PROJECT_DIR [arguments]
```

Where `PROJECT_DIR` is the directory for the survey, and command is the
SDAPS command that is executed. Most commands will require some arguments.
You can always get a help by running:

```bash
$ sdaps COMMAND PROJECT_DIR --help
```

So we create the project using the provided `example.tex`. The tutorial
assumes that the LaTeX file is in the current directory.

```bash
$ sdaps setup tex /tmp/project example.tex
------------------------------------------------------------------------------
- SDAPS -- setup_tex
------------------------------------------------------------------------------
Running pdflatex now twice to generate the questionnaire.
This is pdfTeX, Version 3.1415926-2.4-1.40.13 (TeX Live 2012/Debian)
 restricted \write18 enabled.
entering extended mode
This is pdfTeX, Version 3.1415926-2.4-1.40.13 (TeX Live 2012/Debian)
 restricted \write18 enabled.
entering extended mode
Running pdflatex now twice to generate the questionnaire.
This is pdfTeX, Version 3.1415926-2.4-1.40.13 (TeX Live 2012/Debian)
 restricted \write18 enabled.
entering extended mode
This is pdfTeX, Version 3.1415926-2.4-1.40.13 (TeX Live 2012/Debian)
 restricted \write18 enabled.
entering extended mode
The Title
Date: 10.03.2013
Author: The Author
Questionnaire
1(Head) Range Questions
1.1(Mark) How often do you use SDAPS? {1}
        never - daily
        0(Checkbox)  87.8  78.4   3.5   3.5
[SNIP]
```

Now, what does the output tell us? First the document is compiled four times.
After the first two compiles SDAPS reads all the metadata and calculates the
"Survey-ID" using the box positions and sizes and some other metadata. After
that, the document is recompiled again using the correct "Survey-ID".

The rest of the output is a textual representation of the questionnaire. We
can ignore it, especially because the "annotate" command creates a much nicer
view of everything.

# Overview

![](/images/sdaps-steps-0002.png)

The following topics are covered:

 * [Designing the Questionnaire](../design)
 * [Creating a SDAPS Project](../setup) (this page)
 * [Printing and Scanning](../print-scan)
 * [Adding Scans to a Project](../add)
 * [Running the optical mark recognition](../recognize)
 * [Manual error correction](../correction)
 * [Creating a report and exporting data](../export)
 * [Other things to try](../more)


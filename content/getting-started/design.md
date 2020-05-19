---
title: Designing the Questionnaire
layout: single
---


The first step to conduct a survey is to design the questionnaire itself.
You'll need to take some time to first figure out what questions to ask
before designing the questionnaire.

We are going to use the example questionnaire in the source code repository
in ["`examples/example.tex`"](https://github.com/sdaps/sdaps/blob/master/examples/example.tex)
which looks like this [PDF](/files/example.pdf) after rendering.

## Render a draft

{{< note >}}
These steps will become simpler in the near future as SDAPS is now
[available in CTAN](https://ctan.org/pkg/sdaps) and will be included in TeX Live.
Once that happens, you can compile your SDAPS using LaTeX document in the same way as any other one.
{{< /note >}}

It makes sense to setup an environment where you can compile the LaTeX document
normally. To do so, it is recommended creating a directory and then copying in
the support files. You can then store the `example.tex` into the same folder,
the following shell commands will accomplish these steps:
```bash
$ mkdir project_draft
$ cd project_draft
$ wget https://github.com/sdaps/sdaps/raw/master/examples/example.tex
$ cp -R /usr/share/sdaps/tex/* .
```

Now you have a directory with a copy of `example.tex`, which you can edit as
you wish. Take a look at the [LaTeX class documentation](/class-doc)
for available options, question types and other features. Also note that
most normal LaTeX options to modify document properties such as paper size or
duplex/simplex printing (twoside/oneside) work as usual.

Try rendering the PDF using:
```bash
$ pdflatex example.tex
```
SDAPS requires running pdflatex multiple times. It is recommended to run it
for three times or to use other tools (such as many LaTeX editors) which will
automatically detect the number of runs necessary.

You can familiarize yourself with the LaTeX-Document and the resulting
PDF-file. Notice that the PDF has a "draft" text overlayed. This is because
the barcode at the bottom is just an example and it will change once the
project is created.

# Overview

![](/images/sdaps-steps-0001.png)

The following topics are covered:

 * [Designing the Questionnaire](../design) (this page)
 * [Creating a SDAPS Project](../setup)
 * [Printing and Scanning](../print-scan)
 * [Adding Scans to a Project](../add)
 * [Running the optical mark recognition](../recognize)
 * [Manual error correction](../correction)
 * [Creating a report and exporting data](../export)
 * [Other things to try](../more)


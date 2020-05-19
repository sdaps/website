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

If you would like to play around a bit with it, you can compile the LaTeX
document yourself (this assumes, that you are currently in the git repo of
sdaps source code):
```bash
$ mkdir project_draft && cp examples/example.tex project_draft/
```
Now you have a project directory with a copy of `example.tex`, which you can
 edit as you wish. Take a look at the [LaTeX class documentation](/class-doc)
 for elements you can use or changing paper size.
We need the LaTeX class `sdapsclassic`, if you installed and build sdaps from
source you can copy all files from `tex/class/build/local`:
```bash
$ cp -R tex/class/build/local/* project_draft/
$ cd project_draft
```
Render the pdf.
```bash
$ pdflatex example.tex
```
Sometimes you have to run that last command more than once.

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


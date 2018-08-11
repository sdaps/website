---
title: Examinations
layout: single
menu:
  main:
    parent: Documentation
    idenitifier: examinations
    weight: 30
---

## Examinations using SDAPS

Examinations seem to be relatively common theme for SDAPS users. There are a
lot of different ways that examinations can be done, but a couple of
important problems are common for all examinations.

{{% warning title="Attention" %}}Please also have a look at the
[FAQ](/documentation/#faq){{% /warning %}}

## Multipage Answer Sheets

If you don't have a single (duplex) answer sheet, then it is important to
keep the paper for one student together. SDAPS can help you by printing a
"Questionnaire-ID" on every page. If the sole purpose is to keep all the
pages together, then the ID can be random. You can also assign an ID for
your own purposes (see "Identifying Students" section). See the "``stamp``"
command for more details.

Note that by default SDAPS assumes that all pages for one student are
scanned in a batch and the page count is correct. If for whatever reason
pages may have gotten shuffled around before scanning (or additional
scratch paper may be inserted) then you will need to use the "``--force``"
options for the "``add``" command (wrong page count) and then use the
"``reorder``" command so that the data is interpreted correctly!

The above is important, or else the answers of one student may get
assigned to another student!

## Identifying Students

In general there are different ways to identify students:

* Ask for a student ID/name on the first page
  * Use a freeform text field, and manually replace it with the number/name
  using the SDAPS GUI.
  * Use a matrix of choice questions to ask for a student ID digit by digit
* Field to place a barcode sticker, and hand out barcodes separately
(not implemented, see [issue #2](https://github.com/sdaps/sdaps/issues/2)).
* Use a student specific Questionnaire-ID. If you want to, use a hack to
print e.g. the students name to other places on the paper (see
[issue #11](https://github.com/sdaps/sdaps/issues/11)).

### Freeform Text Field

This method is very simple for the students, as they just need to write
down their name/ID into a single field. Not much can go wrong here.
However, you need to manually transcribe the ID at a later point
(using the GUI or some custom method).

LaTeX code might look like

```latex
\textbox*{2cm}{Enter your student ID below.}
```
or (requires unstable release)

``` latex
\begin{choicequestion}[1]{}
   \choiceitemtext{1.2cm}{1}{Student ID:}
\end{choicequestion}
```

### Matrix of boxes to enter student ID

The idea is to use a large matrix, for the student to enter the ID. SDAPS
only tells you which of the large number of fields is checked, you need
to calculate the ID (and ensure it is correct) yourself.

There are two ways to do this currently. The easier way is one row per
digit and the harder one one column per digit. The difference is that in
row layout you can use a "mark" question and SDAPS returns which box is
checked (or zero) while in the other case you get the raw data for each
checkbox.

The choiceitem way might look like:

``` latex
\begin{choicegroup}{Please write your student ID into the $\sqcup$
and check the corresponding cross.\\ \textbf{Only check one box in each
column.}}
   \groupaddchoice{\Huge$\sqcup$}
   \groupaddchoice{\Huge$\sqcup$}
   \groupaddchoice{\Huge$\sqcup$}
   \groupaddchoice{\Huge$\sqcup$}
   \groupaddchoice{\Huge$\sqcup$}
   \groupaddchoice{\Huge$\sqcup$}
   \groupaddchoice{\Huge$\sqcup$}
   \groupaddchoice{\Huge$\sqcup$}

   \choiceline{\hfill 1}
   \choiceline{\hfill 2}
   \choiceline{\hfill 3}
   \choiceline{\hfill 4}
   \choiceline{\hfill 5}
   \choiceline{\hfill 6}
   \choiceline{\hfill 7}
   \choiceline{\hfill 8}
   \choiceline{\hfill 9}
   \choiceline{\hfill 0}
\end{choicegroup}
```

The range way (note that we can't put headers with the digit on top):

``` latex
\setcounter{markcheckboxcount}{10}
\begin{markgroup}{Please write your student ID into the $\sqcup$
and check the corresponding cross.\\ \textbf{Only check one box in each
 row.}
   \markline{\hfill \Huge$\sqcup$}{0}{9} % you can only put digits on the left/right like this
   \markline{\hfill \Huge$\sqcup$}{}{}
   \markline{\hfill \Huge$\sqcup$}{}{}
   \markline{\hfill \Huge$\sqcup$}{}{}
   \markline{\hfill \Huge$\sqcup$}{}{}
   \markline{\hfill \Huge$\sqcup$}{}{}
   \markline{\hfill \Huge$\sqcup$}{}{}
   \markline{\hfill \Huge$\sqcup$}{}{}
 \end{markgroup}
\setcounter{markcheckboxcount}{5} % or whatever you want usually
```

### Barcode Sticker

Unfortunately this is not implemented right now. It is not really a huge
thing to implement (basically this is just a special case of a freeform
textfield with a different recognition algorithm).

The biggest part here is to add support to the LaTeX class. Also, a separate
utility to render the barcode stickers might be neat to have. This utility
would likely not be part of the core SDAPS distribution.

In this case you would simply hand out the exam paper, and then you have
plenty of time to give out the correct sticker to each student during the
exam (or assign seats in advance).

### Student specific Questionnaire-ID

As mentioned previously, you will often want a "Questionnaire-ID"
(unique barcode on each printout) anyway. If you do this, then you
simply choose a known ID for each student. You then need to be careful
that each student gets the correct printout.

To create the printout run

``` bash
$ sdaps PROJECT stamp -f STUDENT_IDS
```

where STUDENT_IDS is a file containing the barcode value for each student.

If you want to put the student name somewhere else on the paper, then
please have a look at [issue #11](https://github.com/sdaps/sdaps/issues/2) (if anyone has a nicer example,
please post it here!).

## Checkbox recognition mode

By default SDAPS considers checkboxes to be checked if there is a cross in
it. Once a certain fill level is reached, this is again interpreted as a
correction to uncheck the box again.

This correction feature is a relatively big source for errors, as a thick
pen might already cause the field to be considered unchecked, while a sloppy
fill might still be considered checked.

With newer SDAPS versions (1.1.6 and later) you can choose the recognition
mode. This can either be:

* **checkcorrect**: default, see above
* **check**: the same "check" threshold, but no correction feature
* **fill**: a larger threshold, students should fill in the box/bubble

(Note that the values for "fill" are currently not chosen very carefully.
It is possible to modify the thresholds in defs.py. Any feedback on these
is of course welcome.)

Whatever mode you use, please make sure that the students are aware of it!

## Correction

You might want to manually check that SDAPS correctly detected all the
checkmarks. Please use the [GUI](/doc_gui) for this.

## Data Export

SDAPS provides a CSV export. This export contains the state of each
checkbox for "choice" questions (0/1) and the checkbox number for
"mark" question.

Freeform textfields can be exported in three ways:

* 0/1: whether text was found or not
* 0/replacement: if you entered a replacement text
* 0/filename: if you used ``--images`` and no replacement text was defined.
This way it is possible to grab the image data for freeform textfields from
SDAPS if you need it.

## Creating a printout with marks

It is possible to use the internal SDAPS API to render a PDF with the
original scan in the background and correction information overlayed. There
are different ways that this could be done, the example script uses cairo
to create the PDF which is already used for other purposes inside SDAPS
(e.g. the GUI).

One example of a script can be found in the distribution. A slightly more
advanced version is also [attached here](/files/sdaps-overlay.py).
And the [generated example document](/files/overlay-0001.pdf).

Note that SDAPS does not have any way of knowing the grading mode. So this
would need to be fed to the script in some other way (the example just has
a list of correct answers).

## Randomized Layout

SDAPS does not (and will not) support randomizing the order of questions.
Some other projects do support this (e.g. Auto Multiple Choice).

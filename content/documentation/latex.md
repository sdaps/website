---
title: LaTeX Support
layout: single
menu:
  main:
    parent: Documentation
    idenitifier: latex
    weight: 50
---

With the LaTeX support SDAPS provides an easy way to build questionnaires.
Using this class together with SDAPS you can create and analyse a survey in
a breeze.

This LaTeX class not only makes it less error prone to create surveys for
SDAPS (instead of using LibreOffice or OpenOffice), but also gives you more
features. The features are:

* Create a questionnaire with only a couple of easy LaTeX macros
* Get a preview of what the final version looks like, without running the main SDAPS program
* Translations are supported (english and german are provided currently)
* Creates a complete machine readable description of the questionnaire. This contains exact positions of boxes and questions with answers.

A collection of examples can be found here.

### Basic Example

The following example does not show all features, but can give an impression of
how it all works. And the [resulting PDF](/file/latex_example.pdf)

``` latex
\documentclass[draft,english,pdf,pagemark,stamp]{sdaps}
\usepackage[utf8]{inputenc}

\author{The Author}
\title{The Title}

\begin{document}
  \begin{questionnaire}
    \begin{info}
      Some information here. Nothing special, just adds a line above/below.
    \end{info}

    \section{Section Heading}

    \begin{markgroup}{This is a group of mark questions}
      \markline{first}{lower bound}{upper bound}
      \markline{second}{lower bound}{upper bound}
    \end{markgroup}

    \singlemark{Mark Question}{lower bound}{upper bound}

    \section{Section Heading}

    \begin{choicequestion}[4]{Some choices}
      \choiceitem{first}
      \choiceitem{second}
      \choiceitem{third}
      \choiceitem{fourth}
      \choicemulticolitem{2}{one with a very long text}
      \choiceitemtext{1.2cm}{2}{Other:}
    \end{choicequestion}

    \textbox{5cm}{A Textbox}

  \end{questionnaire}
\end{document}
```

### Getting Started

To create a new questionnaire it makes sense to copy the files from the
``sdaps/tex`` directory into the same directory of the questionnaire.
This way you can compile the document using ``pdflatex`` for testing purposes.

If you installed SDAPS, then the files should be in ``/usr/share/sdaps/tex``
or ``/usr/local/share/sdaps/tex``. If you decided to not install SDAPS then
the translation files need to be copied separately. They are created when
building SDAPS and need to be copied from the ``build/share/sdaps/tex``
subdirectory.

### Documentclass Options

There are a number of options (SDAPS and standard LaTeX) that affect how
SDAPS works. The following table lists these options.

Option(s)             | Default     | Note
----------------------|-------------|---------------------------
a4paper,letterpaper,… |             | Select paper size, normal LaTeX mechanism. Note that the default A4 paper size has a slightly different size than specifying "a4paper" (it is impossible to see, but SDAPS sees this as a form change).
globalid=STRING       | empty       | The global ID. This string is written into a barcode at the bottom center. When the project is generated you can also change this by modifying the ``info`` file and running ``stamp``.<<BR>>The purpose of this barcode is user defined.
print_questionnaire_id| not set     | If specified then a unique Questionnaire-ID is printed on each questionnaire. This ID can be either random or user defined. This can be useful for non-anonymous surveys or for questionnaires with a lot of pages and you want to use the ``reorder`` command.
oneside,twoside       | twoside     | Select simplex or duplex, normal LaTeX mechanism. When selected the barcodes are printed on every page, and you can print the survey in simplex mode. Note that SDAPS assumes a simplex scan, if you scan duplex (scanning an empty page for every page of the questionnaire) then you need to specify the ``--duplex`` option when ``add`` ing the image to the project.
checkmode             | checkcorrect| Select the mode for checkboxes. This can be either ``checkcorrect`` meaning check is selected, filled is again unselected. ``check`` meaning a check selects the box and unselecting is not possible and ``fill`` requiring a proper fill to select a box.
style=STRING          | code128     | Select the style to use. May be ``code128``, ``qr``, ``classic``, or ``custom`` (if you really know what you are doing)
no_print_survey_id    | not set     | Only works in ``classic`` mode. In that case you get marks in every corner identifying the page and its rotation. No further code is added.
pagemark              | not set     | Specify to see corner marks. Always set this option for a more accurate preview.
stamp                 | not set     | Specify to see barcodes. Always set this option for a more accurate preview.


The options ``print_survey_id``, ``print_questionnaire_id`` both have their
counterpart with the ``no_`` prefix to disable the option again. For ``stamp``
and ``pagemark`` it is ``nostamp`` and ``nopagemark`` currently.

### Commands

#### questionnaire environment

Main environment that everything needs to be wrapped in. An optional argument
``[noinfo]`` is supported to suppress the default information message about
filling out the questoinnaire.

#### info environment

Adds a section for information. This is simply surrounded by a line at the
top/bottom.

#### addinfo

Using ``addinfo`` you can add information that SDAPS will later put on the
printed report. The command has to arguments a key and a value.

For example:

``\addinfo{Date}{06.06.2012}``

#### singlemark

The ``singlemark`` can be used for range questions. You pass it a question
and description for the lower and upper bounds.

``\singlemark{What do you think of this LaTeX class?}{nothing}{looks great}``

#### choicequestion environment

This environment is used to create a question with a set of arbitrary answers.
The answers are put into a tabular environment and with a specified amount of
columns.

Inside this environment you add a new choice simply using the ``choiceitem``
macro. If one of the possible answers is too long, you can also use
``choicemulticolitem``. In addition it is possible to add a freeform text box.
This can be accomplished using the ``choiceitemtext`` macro.

#### <u>choiceitem</u>

A possible choice in a choicequestion environment. Only has one argument, that
is the description.

#### <u>choicemulticolitem</u>

The same as ``choiceitem`` but takes an extra argument to specify the number
of columns to use.

#### <u>choiceitemtext</u>

Adds a freeform text field to a choice question. Often it is impossible to
add all the possible answers, so this gives the interviewee the possibility
to add an arbitrary answer.

The command has three arguments. That is the height (eg. 1.2cm) then the
width in columns (the textbox is automatically stretched to fill the
horizontal space) and a description string for the box as the last argument.

For example:

``\choiceitemtext{1.2cm}{3}{Other:}``

#### markgroup environment

A markgroup can be used if you have a set of similar "mark" style questions.
This command uses a lot less space on the paper compared to using
``singlemark``. The environment has one argument which is a header for
everything. ``markline`` is then used inside this environment.

#### <u>markline</u>

This command is used in the same way as ``singlemark`` but can only be used
inside a ``markgroup`` environment.

Example of ``markgroup`` and ``markline``:

``` latex
\begin{markgroup}{What do you think about the following aspects of the SDAPS questionnaire LaTeX class?}
  \markline{ease of use}{very easy}{very hard}
  \markline{quality of the generated questionnaire}{good}{bad}
\end{markgroup}
```

#### choicegroup

Similar to ``markgroup`` for ``markline`` there is a ``choicegroup`` command
for the ``choicequestion`` environment. For all of the questions inside
a ``choicegroup`` the answers possible choices need to be the same. Another
difference is that it is not possible to add freeform text fields.

#### <u>groupaddchoice</u>

This command can be used to add choices to a choicegroup. It can only be
used a the start of the environment.

#### <u>choiceline</u>

This command is then used to add a single question.

An example of all this in action would be the following:

``` latex
\begin{choicegroup}{Which program do you prefer for the following tasks?}
  \groupaddchoice{\LaTeX}
  \groupaddchoice{LibreOffice}
  \groupaddchoice{Microsoft Word}

  \choiceline{General text layout}
  \choiceline{Formula typesetting}
  \choiceline{Creating questionnaires}
\end{choicegroup}
```

#### textbox
The ``textbox`` command adds a freeform text box for the interviewee to
fill out. It has two arguments. The first is the minimum height and the
second a description which is printed on top.

The textbox will be expanded automatically to fill all available vertical
space! If you do not want this, you can use the starred version ``\textbox*``.

Example:

```latex
\textbox{5cm}{You can use the following box to write down any additional comments:}
```

#### Other commands

#### <u>checkbox</u>

``\checkbox*`` can be used to place a box that looks exactly like a
checkbox, but will not be used by detected SDAPS. The ``\checkbox``
command is used when typesetting questions and stores the data about
the checkbox position in the description file.

#### <u>checkedbox</u>

``\checkedbox`` renders a box that with a cross drawn inside it. It
can be used for instrucations.

#### <u>correctedbox</u>

``\correctedbox`` draws a filled and checked checkbox for instructions.

### Defines/Counters

These only works in SDAPS 1.1.2 and newer.

Name             | Type    | Default | Purpose
-----------------|---------|---------|---------
markcheckboxcount| counter | 5       | The number of checkboxes in mark questions (singlemark and markgroup).

There are more defines that configure the layout of the corner marks and
barcodes. You should never change these (if you do, then you also need to
modify ``defs.py``)!

### Fonts

Some of the fonts can be customized using the Komascript font setting
routines. You can customize the following fonts:

Font                 | Default                   | Purpose
---------------------|---------------------------|----------------------
barcodefont          | ``\ttfamily\footnotesize``| The text underneath the barcodes. (code128 style)
questionnaireidfont  | ``\ttfamily\textbf``      | The font for the questionnaire ID label (classic style)
surveyidfont         | ``\ttfamily\textbf``      | The font for the questionnaire ID label (classic style)
choicefont           |                           | The font answers
singlemarkchoicefont | choicefont                | Font used in singlemark questions.
marklinequestionfont |                           | Font used for the question with the markline command.
marklinechoicefont   | choicefont                | Font used for the answer with the markline command.
choiceitemfont       | choicefont                | Font for choiceitems
choicegrouplinefont  | choicefont                | Font for the question in choicegroups
choicegroupchoicefont| choicefont                | Font for the answers in choicegroups


### Colors
There are some colors that can be modified if required.

Color            | Default| Purpose
-----------------|--------|-------------
sectionbgcolor   | 80%    | gray The background for section headers
sectionfgcolor   | black  | The text color for section headers
groupevenrowcolor| white  | The background color for even rows in group environments (removed again due to issues with colortbl, see https://github.com/sdaps/sdaps/issues/25)
groupoddrowcolor | white  | The background color for odd rows in group environments (removed again due to issues with colortbl)

## Collection of LaTeX example documents

Feel free to add more examples to this page.

* The example from the [Tutorial](/getting-started#Usage). This example uses most features that SDAPS has.
* [Test document in german]
(http://git.sipsolutions.net/gitweb.cgi?p=sdaps.git;a=blob;f=test/data/tex/questionnaire_with_ids.tex;hb=HEAD).

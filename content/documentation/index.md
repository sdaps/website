---
title: Documentation
layout: single
---

## Interface

SDAPS is a command line application. After building the C extension and
documentation (and optionally installing it into the system) you can execute it.

* Run ``sdaps`` if you installed it
* Run ``./sdaps.py`` from the source directory otherwise.

With ``--help`` you can get a list of commands. To get more information about
one of these commands run SDAPS with ``sdaps X command --help``. The X can be
any string, it just needs to be there as SDAPS expects a path to a project
directory.

### Important Commands

* **setup** or **setup_tex**: Creates a new project directory for the given
questionnaire
* **stamp**: Create printable PDF
* **add**: Adds scanned image data. From version 1.1.7 onwards SDAPS will
automatically convert files to the appropriate format if the ``--convert``
option is given. Only use this option if the scan is not already in the
appropriate format for SDAPS (monochrome multipage tiff). See also [Scanning]().
* **recognize**: Runs the optical mark recognition
* **reorder**: Group pages using their (unique) questionnaire ID. (ie. fix
order after pages have been mixed up)
* [gui](): Starts a graphical user interface that can be used to correct
errors in the automatic recognition.
* **report** (and **report_tex**): Creates a report of the results as PDF.
* **csv**: Can be used to export the data to a CSV file.

### Filtering
Some commands can work only on a subset of the data (eg. report, csv export).
With this it is possible to create a PDF report that is for example separated
by the sex of the participant. These filters are python logic expressions.

For the logic expression, every choice question is exported as a list of
checked boxes. The list of boxes is zero based and freeform fields are
included. The mark type question is instead exported as a number between 0
and 5, where zero means "no answer".
As these are python expressions, you can simply combine them with ``and`` and
``or``. It is allowed to combine such a filter with the ``--all-filters``
argument that the report script has.

Example filter:

* ``0 in _1_2``: First checkbox of question 1.2 is checked (others of the same
question may be checked too).
* ``_1_2 == [0]``: Only the first checkbox of question 1.2 is checked.
* ``_2_1 == 1``: Question 2.1 is a mark question, and the leftmost box has
been checked.
* ``_2_1 == 0``: Question 2.1 is a mark question, and is not valid (no box, or
multiple checked boxes).

Other variables that can be queried

* survey_id: The survey ID (will always be the correct one)
* questionnaire_id: The questionnaire ID if a barcode was found.
* global_id: The global ID if a barcode was found.
* valid: Whether the sheet is considered valid (ie. no fatal errors).
* quality: The estimated quality of the recognition (a value between 0 and 1).
* recognized: Whether recognition has been run for the sheet. (new since 1.1.1)
* verified: Whether a verifier has acknowledged the sheet. (new since 1.1.1)
* complete: Whether all pages are scanned and could be identified for the
sheet. (new since 1.1.2)

Example call of the "report" command:
``$ sdaps some_project report --filter "(0 in _1_2 or _2_1 == 1) and
global_id=='some name'"``

## SDAPS Project Directory

SDAPS creates a project directory for every survey you create. This directory
is used to store all the data that belongs to the survey. Some special files:

* info: A file containing metadata, this may be modified directly.
* survey: Data storage (pickled python objects)
* \*.tif: The scanned images that have been added to the project

It is also used as the default output directory for commands that create new files.

## FAQ

### SDAPS is hard to install, is there any more documentation?

Unfortunately not. This is an area where contributions would be very much welcome!

### Can the Survey ID (lower right barcode) be changed?

No. This ID identifies the questionnaire uniquely and it is reproducible
(i.e. if you recreate the survey using ``setup`` or ``setup_tex``
it will be the same[1.]. If you *really* want to you can modify the load
routine in ``model/survey.py``.

### Is it possible to do custom layouts in LaTeX?

Of course it is, however you need to write out some metadata manually. That
means using ``\immediate\write\sdapsoutfile{\unexpanded{STRING}}``. Have a
look at the generated ``.sdaps`` file and the LaTeX class. You'll need to
write out the questions and enough answers for the checkboxes.

There is a `small example document
<custom.tex>`__ with the
`resulting questionnaire
<custom.pdf>`__ and
`a document with the metadata that SDAPS detected overlayed
<custom_annotated.pdf>`__.

Tip: You can visually check the assignment of checkboxes to answers/questions
using the  ``annotate`` command. Alternatively read the output of the
``setup_tex`` command.

### SDAPS complains that poppler is not installed, but it is!

Poppler might be installed, but SDAPS needs the python bindings to use it.
You need to install the GObject introspection data and python-gi bindings.
On Debian based distributions these are in ``gir1.2-poppler-0.18`` and
``python-gi``.

Also, you only need this if you want to import PDF files (using ``add
--convert`` or ``convert``. SDAPS will still print the warning even if you
do not use PDF.

### Why is there no barcode on the first page?

By default SDAPS assumes duplex printing. The barcode is only printed on the
back of each sheet of paper and used for both the front and back.

If you switch to simplex mode (``--simplex`` for ODT and ``onside`` document
class option in LaTeX) then SDAPS renders a barcode on every page.

**Tip:** SDAPS automatically detects the case where the questionnaire only has
a single page and switches to simplex mode automatically!

**Attention:** If you use a simplex document then SDAPS needs to know how you
scan it. By default SDAPS assumes a simplex scan! Scanning simplex is usually
not a good idea because some pages **will** be flipped and missed that way. So
if you can then **always scan the document in duplex mode and pass the**
``--duplex`` **option to the** ``add`` **command**!

### Is it possible to put content inside a freeform textbox?

In theory yes[2.], the code below allows this by putting a tikz node into the
center. The node has a text width of exactly the white area, and also a
minimum height of this area. You can use the ``\textwidth`` and ``\textheight``
macros inside to query the size.

This is quite a hack, but it should work fine (just copy it into the header,
and use the command directly after a ``\textbox``).

<pre>
   \makeatletter
   \newcommand{\makenodeinlasttextbox}[1]{%
     \begin{tikzpicture}[remember picture, overlay]%
       \setlength\textheight{\@sdaps@height}
       \advance\textheight by -2pt
       \node[outer sep=1pt, inner sep=0pt, align=center, text width=\@sdaps@width-2pt, minimum height=\textheight, shift={($(\@sdaps@x,\@sdaps@y) + 0.5*(\@sdaps@width, -\@sdaps@height)$)}, anchor=center] at (current page.south west) {%
         #1%
       };
     \end{tikzpicture}
   }
   \makeatother
</pre>

Use the macro to put content into the textbox:

<pre>
   \textbox*{6cm}{Some textbox}
   \makenodeinlasttextbox{This will appear inside the textbox.}
</pre>

**Attention:** If you use questionnaire IDs and would like to stamp multiple
questionnaires at a time, then the above code does not work as is. We need to
layer another hack around it.  This is because the class tries to conserve
memory and breaks the hack at the same time. We need to enable output again,
which needs two steps unfortunately. A new command[3.]:

<pre>
   \makeatletter
   \let\enableoutput\@sdaps@outputtrue
   \makeatother
</pre>

And then use this command to enable the output again. Best to put it all into
braces, so that it will not be enabled for all the other boxes (especially all
the checkboxes)

<pre>
   {
     \enableoutput
     \textbox*{6cm}{Some textbox}
     \makenodeinlasttextbox{This will appear inside the textbox.}
   }
</pre>

### FAQ-Footnotes

1. The only exception is when e.g. a LaTeX package you use is upgraded and changes the layout. But that is the intended behavior as the questionnaire '''has''' changed in that case.
2. Actually, the next major release of SDAPS will natively support this. See
       `Future/LaTeX
       </Future/LaTeX/>`__ and the linked resources for details.
3. This is required to as the parser cannot be reconfigured inside the questionnaire environment.


## More documentation

Have a look at the links in the menu. Quite a lot is not yet documented. There
are some notes about this in the following:

### Stuff that should be described

#### The different configurations

#### <u>"classic" Style</u>

* Maximum of 6 pages
* Does not require a survey ID to be printed
* Does not allow a "global ID"
* Only allows 16 bit numbers for Questionnaire ID.

#### <u>"code128" Style</u>

* Has a Global-ID that can be freely choosen
* Questionnaire ID may contain ASCII (code128 Barcode)
* Requires a Survey ID barcode (for page rotation and page number)

#### <u>"qr" Style</u>

* Same as "code128" but uses a QR-Code with high redundancy for better
reliability.

### Additional Questions

SDAPS has the ability to add data from external sources. This can be useful
if only a few extra data points are coming from an external source (eg. a
webpage). A small step by step howto of how these can be used would be good.

### Same survey, many classes

It often happens that the same questionnaire is used multiple times, and the
results need to be separated in the end. SDAPS doesn't have perfect handling
for this, and there are different ways to do it:

* Use Global ID. This works by using one project, then changing the global ID
multiple times and printing different questionnaires. After everything is
recognized one can reports by filtering according to the global ID.
* Use the same questionnaire and separate project.

To modify the text on the report the "info" file can be modified or the "info"
command can be used.

### Survey ID generation

How it is generated (md5 sum of: checkbox position, paper size, ...).

### Reordering

* Add data (maybe using ``--force`` if pages are missing)
* Run recognition using ``--identify`` (fast method that only reads the codes)
* Run ``reorder`` command.
* Run ``recognize`` normally
* Use GUI to fix errors as usual
* Export data/create report

The only change is that two steps are inserted before the normal recognize
step. The first is the ``recognize --identify`` command, and the second the
reorder command which correctly reorders the data.


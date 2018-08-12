---
title: Ideas for future developments
layout: single
---

If you are interested in helping with any of these developments, then please
write to Benjamin Berg or drop by on IRC.

## Common questionnaire description format

See also [Specification](#specification).

Some people started to work on a description format for questionnaires. Some of
the features that you can expect from such a format:

* Versioning information
* Metadata for question layout
* Metadata for data analysis (e.g. hidden variables)
* Translation support
* Automatic survey creation (both online and offline; e.g. SDAPS and
limesurvey, but it is not specific to these)
* XML based?

This project is not specific to SDAPS. However a close collaboration is planned
so that SDAPS will work with it.

## New/Improved LaTeX class

There are some shortcomings in the current LaTeX class (i.e. the layout is not
flexible enough). There are some ideas for new features and changes:

* Possibility to create LaTeX code from description file (see above)
* Both horizontal and vertical layout of questions
* Single/Multiple answer question types
  * Requires improvements in SDAPS internally
  * Single answer exported as one variable; multiple choice as multiple variables
  * Use circles for single answer and boxes for multiple choice fields (this
  is a metaphor that is familiar from computers)
* Specifying variable names for the export (requires core changes)
* A "no answer" choice for range questions
* Standardized question type names. i.e. probably recycle the names from limesurvey.

## Python 3 Port

The goal is to port SDAPS to python 3.x in the long run. There are some things
that need to happen for this:

* The C module needs to be either ported to the cpython 3 API, or to GLib to
use introspection bindings.
* The LibreOffice importer needs to be rewritten using python-uno.
* The OpenCV based package ("convert", import of other image formats and camera
image deskewing) requires python 3 bindings to become available.

## Specification
{{% warning title="Attention" %}}
The notes here are rather old and parts
of this (and a lot other things) have been implemented. Please see
[sdaps-class](http://github.com/sdaps/sdaps-class) and
[sdaps on gmane](http://article.gmane.org/gmane.comp.statistics.sdaps/203)
for some notes on the new work.
{{% /warning %}}

### Goals

* Matrix Layout of multiple questions
* More complex single question layouts
* Variables/Values (sane naming and values in csv export)
* extended Ranges (i.e. numeric range + another option)
* Split metadata output features and base SDAPS output from questionnaire
creation to ease creating custom classes on top of the existing infrastructure.

### Matrix Layout

All three question types (multiple choice, single choice/option, range) can
be layed out as a matrix, this has the following properties:

* questions on one axis
* field labels on the other axis
* Axis can be swapped (horizontal/vertical layout)
* commands define questions and fields

Nice to have features:

* alternating background colors for rows or columns
* ...

### Layout considerations

The hard part here is the width of the column, and how to handle line
breaking in the different cells. We probably want line breaking to happen
automatically in most cases, and a fixed column width also makes sense.

Layout options:

* **fixed-width**: A specific column width is given. Default could be 0.5\textwidth / COLS (this is what Limesurvey does).
* **max-width**: Similar to **fixed-width** but column size may be decreased if the text fits anyways. (i.e. layout text with fixed-width, measure width and use that width). Default column width same as for fixed-width (or maybe slightly larger, as some space will be saved usually).

### Commands

#### Fields

#### <u>Choice</u>

``` latex
\choice[options]{label}
```

Argument       | Meaning
---------------|--------------------
**var=string** | Suffix to use for variable. Default is just to number them.
**text=string**| Replacement text for metadata (used instead of normal Label)

#### <u>Option</u>

``` latex
\option[options]{label}
```

Command is only valid in Range and Option array. It is almost equivalent to
the "choice".

Argument       | Meaning
---------------|------------
**val=int**    | Value to use
**text=string**| Replacement text for metadata (used instead of normal Label)

#### <u>Range</u>

``` latex
\rangelower{lower bound header}
[...]
\rangeupper{upper bound header}
```

These commands mark the lower and upper bound in a range. Options between
these two commands are considered part of the range, all other options are
not part of the range.

### Questions

```latex
\question[var=string,text=blubber]{question text}

\question[var=string,text=blubber,range lower=blub,range upper=bluber]{question text}{lower label}{upper label}
```

Defines a question as part of a question array. The arguments depend on the
environment it is used in.

Arguments              | Meaning
-----------------------|-----------------
**var=string**         | Prefix for variable (or variable in option/range mode)
**text=string**        | Replacement text for metadata
**lower text=string**  | Replacement text for range lower bound (range only)
**upper text=string**  | Replacement text for range upper bound (range only)
**invalid value=int**  | Variable value if too many checkmarks were found (option/range only)
**no answer value=int**| Variable value if no checkmarks were found (option/range only)

In range question two additional mandatory arguments are used to pass over
the upper and lower label that is part of the matrix itself.

### Environments

We have three environments (they are all pretty much the same, just slightly
different commandos):

* choicearray
* optionarray
* rangearray

Fixed arguments:

* Header

Optional arguments:

Argument      | Meaning
--------------|-------
**text**      | Replacement text for metadata
**horizontal**| Use horizontal layout (questions are rows)
**vertical**  | Use vertical layout (questions are cols)


### Examples

Examples follow here in a bit.

``` latex
\begin{choicearray}[horizontal,var=tool]{Which of these tool do you think is appropriate for the following tasks (multiple answers are allowed)}
  \choice[var=latex,text=LaTeX]{\LaTeX}
  \choice[var=lo]{LibreOffice}
  \choice[var=msword]{Microsoft Word}

  \question[var=letter]{Writing Letters}
  \question[var=scratch]{Printing scratch paper}
  \question[var=papers]{Writing papers}
  \question[var=surveys]{Creating surveys}
\end{choicearray}
```

```
QObject-Head=X.Y Which of these tool do you think is appropriate for the following tasks (multiple answers are allowed)
QObject-Choice=X.Y.Z Writing Letters
Answer[X.Y.Z]=LaTeX
Box[X.Y.Z]=Checkbox, page, xcoord, ycoord, width, height, box, latex,
Answer[X.Y.Z]=LibreOffice
Box[X.Y.Z]=Checkbox, page, xcoord, ycoord, width, height, box, lo,
Answer[X.Y.Z]=Microsoft Word
Box[X.Y.Z]=Checkbox, page, xcoord, ycoord, width, height, box, msword,
```

Note:

* The "[X.Y.Z]" index is a helper, so that it is permissible to output the
boxes for different questions interleaved. (i.e. Question 1, box 1; Question
2, box 1, ... Question 1, box 2, ...)
  * This makes vertical layouts easier, as the checkbox coordinates can be
  written to the file immediately.
* "Box" and "Answer" only need to be in the correct order, they don't need to
be interleaved or anything.
* The last two items in the "checkbox" line are the variable and value for
the box. Usually only one will be given, so the other is simply empty (both
may be empty, and SDAPS will auto assign them).
* The first answer is "LaTeX" instead of "\LaTeX" as there was a replacement
text.
* All aspects of this format can be modified if need be. The important part
is only that the information can be read back in some way.

``` latex
\begin{optionarray}[horizontal]{Which tool would you use for the following tasks (choose one)}
  \option[val=1]{\LaTeX}
  \option[val=2]{LibreOffice}
  \option[val=3]{Microsoft Word}

  \question[var=letter]{Writing Letters}
  \question[var=scratch]{Printing scratch paper}
  \question[var=papers]{Writing papers}
  \question[var=surveys]{Creating surveys}
\end{choicearray}
```

Hmm, do we really want to restrict values to always be integers?

``` latex
\begin{rangearray}[horizontal,var=mathlayout]{How good do you think are the following tools for writing documents containing mathematical formulas?)}
  \rangelower{}
  \option[val=1] {1}
  \option{2} % We use value auto increment here
  \option{3}
  \option{4}
  \option{5}
  \rangeupper{}
  \option[val=0]{not sure}

  \question[var=msword]{Microsoft Word}{bad}{good}
  \question[var=latex]{\LaTeX}{bad}{good}
  \question[var=lo]{LibreOffice}{bad}{good}
\end{choicearray}
```

### Notes
* scrlayer(-scrpage) (at least texlive 2012.03, better higher as it contains bug)
* ``\value{page}`` instead of ``\thepage``?


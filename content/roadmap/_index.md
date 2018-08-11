---
title: Ideas for future developments
layout: single
---

If you are interested in helping with any of these developments, then please
write to Benjamin Berg or drop by on IRC.

## Common questionnaire description format

See also `Future/LaTeX`_.

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

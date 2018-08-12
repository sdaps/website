---
title: Overview of Changes in SDAPS 1.1.3
date: 2014-05-29
---
With this release SDAPS has been restructured internally. There are two reasons for doing this. The first is to improve the API which simplifies the usage of it in custom scripts. Another point is that the old code was incompatible with the import handling of python 3. So doing this change is also a prerequisite for a future port to python 3.x.
<!--more-->

Other changes include:

- GUI: Fix an offset error with new GTK+ versions
- GUI: Improved keyboard navigation (issue #30)
- GUI: Improved mouse handling and overlay drawing
- GUI: Show the questionnaire ID on the right side
- GUI: Sort images by page number
- LaTeX: Improved unicode support
- LaTeX: Fixed precision issues in report generation
- LaTeX: Fixed some whitespace issues in the LaTeX class
- ODT: When stamping a single document, keep forms intact
- reorder: Fix reordering of simplex documents
- recognize: Slight changes in the OMR heuristics.
- Fixed issues in the upgrade routine

New and updated translations:

- German
- Spanish

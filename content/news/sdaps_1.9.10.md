---
title: Unstable release SDAPS 1.9.10
type: post
date: 2022-04-24
---

Please note that the system LaTeX files will be used preferentially. However,
some version of TeXLive may not work correctlue due to changes in LaTeX 3.

As such, distributions should check whether the version provided by
TeXlive/CTAN is working correctly. If not, you should continue to use the
LaTeX files provided in this bundle (pass `--build-tex`/`--install-tex`).

<!--more-->

Important changes:

 - New LaTeX class fixing compatibility and other issues
 - Delete image files on reset
 - Fix an issue after resetting a project
 - Export checkbox data separately for single choice questions
 - Export invalid single choice responses using strings (in new projects)
 - Change logging to be 1 based for pages (rather than 0)
 - Permit modifying the corner mark positions
 - Updates and improvements to examples
 - Fix issue opening old surveys
 - Fix image processing on big endian machines

New and updated languages:

 - German
 - Russian
 - Swedish
 - Spanish
 - Portuguese (Brazil)
 - Polish
 - Portuguese
 - Italian
 - Chinese (Simplified)
 - French

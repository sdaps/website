---
title: Unstable release SDAPS 1.9.2
type: post
date: 2018-03-26
---
This is a new unstable release porting SDAPS to Python 3 and modifying the
data storage format. This release is incompatible to any prior release.
It can be considered the first 2.0 alpha release though.
<!--more-->

Important changes:

- ODT support has been dropped entirely
  (due to missing dependencies for Python 3)
- Data storage has been switched to sqlite storing json serialised objects
- Correctly calculate standard deviation (issue #111)
- Updated LaTeX class with new features and fixes
  - Documentation improvements
  - Add \qid back for querying the current questionnaire ID (Paulo Matias)
  - Requires variable handling and auto numbering
  - Add range specification to choicegroup questions only showing certain choices
  - Improved layouting of sdapsarray
  - Allow setting checkbox count of singlemark questions
- Add a few helpers for packaging

New and updated languages:

- Norwegian bokmål
- Spanish
- Italian
- Ukrainian
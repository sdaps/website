---
title: Overview of Changes in SDAPS 1.1.11
date: 2015-12-27
---
Mostly a bugfix release again. The most important fix (preventing dataloss) is that the data is now written atomically. This means that aborting an SDAPS run should not result in a corrupted database anymore.
<!--more-->

Important changes:

- model: Write survey file atomically (#79)
- image: compatibility with older glib versions
- csv: Import code fixes (#79)
- latex: Work around manual enumeration breaking automatic numbering
- setup: Create nested directories instead of only one leve
- convert: Support landscape questionnaires (#88)

New and updated languages:

- Arabic
---
title: Unstable release SDAPS 1.9.6
type: post
date: 2019-01-20
---

This is the next release to stabilize SDAPS in the run up to a 2.0 release.
There are a number of smaller changes that change behaviour, so again, take
some care when upgrading.

<!--more-->

Important changes:

 - Allow adding review comments on whole sheets and questions (#148)
 - Allow specifying the LaTeX engine used to compile the project (#150)
 - Reorder CSV command parameters to match new layout
 - Fix printing of state when an error occurs during setup (#163)
 - Fix LaTeX class build script hanging when l3build is missing (#166, #153)
 - Default to not align all group environments in a document (sdaps-class#15)
 - Allow disabling all recognition related markings (sdaps-class#14)
 - Add basic support for reading QR codes as part of questions (#2)

New and updated languages:

 - Norwegian Bokmål
 - Portuguese
 - Portuguese (Brazil)

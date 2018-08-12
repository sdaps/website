---
title: Update
date: 2012-06-25
---
# Barcode based stamping

This changes a lot of things, so lets describe it here. We actually still support the old codeboxes as the "classic" style. The new Code-128 barcode based system is the "code128" style.

The style is a new concept that is added to SDAPS. It is simply a string option that is stored, which is then used to select the correct algorithms inside the different scripts.

With the new Code-128 barcode style there are some new features:

- An additional "Global-ID" which can be used by the SDAPS user for tracking of their own. The idea is to identify a larger scale survey which this questionnaire is only a small part of.
- No limitation of page count, except for the limitation that duplex questionnaires need to have a multiple of two pages.

Again the different IDs that are printed in Code-128 style. They are:

### Questionnaire-ID:
  a unique ID for each printed questionnaire. This can be used keep track of each individual questionnaire.
  This is optional.
  This code is printed on the left side.

### Global-ID:
  Entirely choosen by the user. SDAPS does not care about it, it is only read and stored right now. In the future this data should also be exported in some way.
  The purpose of this ID is to track multiple surveys that are part of a larger study.
  This code is printed in the center.

### Survey-ID/Page Number:
  This is the code that is used by SDAPS for tracking.
  It is a pseudo random value that is based on the questionnaires layout, and cannot be changed by the user. It consists of the Survey ID + 4 digit page number.
  This code is printed on the right side.

If combined these three barcodes will uniquely identify every page that exists.
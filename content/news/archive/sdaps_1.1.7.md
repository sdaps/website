---
title: Overview of Changes in SDAPS 1.1.7
date: 2014-11-02
---
The most important change in this release is that the import of image data has been simplified.
SDAPS can now do an image format conversion automatically as part of the "``add``" command, removing the necessity of using "``convert``" or some other external method to preprocess the images. As before, this feature requires OpenCV.
Another change is that SDAPS now imports PDF files directly. If a PDF file contains a full page image (i.e. a scanned document) then this image is used directly to prevent image quality loss due to resampling. This feature requires poppler to be installed.
Overall these changes make it a lot easier to work with different scanners. It is now only neccessary to pass the "``--convert``" option to the "``add``" command to add files that are not already in the expected format.
<!--more-->

Important changes:

- stamp: Fix re-stamping all IDs
- add: Implement conversion feature (``--convert`` option)
- convert: Add support for reading PDF files

New and updated languages:

- German
- Portuguese (Brazil)

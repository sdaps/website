Major Changes
=============

Unstable release SDAPS 1.9.2 -- 2018-03-26
------------------------------------------

This is a new unstable release porting SDAPS to Python 3 and modifying the
data storage format. This release is incompatible to any prior release.
It can be considered the first 2.0 alpha release though.

Important changes:

* ODT support has been dropped entirely
  (due to missing dependencies for Python 3)
* Data storage has been switched to sqlite storing json serialised objects
* Correctly calculate standard deviation (issue #111)
* Updated LaTeX class with new features and fixes

  - Documentation improvements
  - Add \qid back for querying the current questionnaire ID (Paulo Matias)
  - Requires variable handling and auto numbering
  - Add range specification to choicegroup questions only showing certain choices
  - Improved layouting of sdapsarray
  - Allow setting checkbox count of singlemark questions

* Add a few helpers for packaging

New and updated languages:

* Norwegian bokmål
* Spanish
* Italian
* Ukrainian

Overview of Changes in SDAPS 1.2.1 -- 2017-11-19
------------------------------------------------

Important changes:

* Fix regression in questionnaire ID handling

Unstable release SDAPS 1.9.1 -- 2017-08-20
------------------------------------------

This is a new unstable release pulling in a lot of fixes. Please note that
it is incompatible to the previous 1.9.0 release as the fixes to the class
will result in the survey IDs to become different.

Important changes:

* Fix repetition of questionnaires
* Fixes to make class work with TeXlive 2017-08-08
* Fix build to not install the TeX class in the users home directory
* Fix LaTeX report generation (#108)
* Fixes and tests of CSV import and exporter
* Improve CSV export to include more information about sheets
* Change default style to QR code


Unstable release SDAPS 1.9.0 -- 2017-07-16
------------------------------------------

The first release of a new unstable series is now available. This brings a
lot of improvements, primarily with regard to LaTeX:

* Entirely new LaTeX class and package set
* Ability to specify variable names for questions and answers
* New layouting possibilities using the LaTeX class

See also the new `class repository`_ and its `documentation`_.

Overview of Changes in SDAPS 1.2.0 -- 2017-07-16
------------------------------------------------

This is a stable release of the new existing unstable series. As the branch
has long been more stable compared to the old "stable" branch this was a
logical step to move forward. Also, most of the development has moved to a
new branch and beta releases will now be published under the "unstable"
series.

Important changes:

* Allow using LO 5.2, requires filling the background of checkboxes
* Use python2 instead of python (#91)
* Fix non-square checkboxes (#92)
* Update TeX code and example for newer LaTeX versions
* Fix encoding issues (#98)
* Fix a recursion in the GUI

New and updated languages:

* French


Overview of Changes in SDAPS 1.1.11 -- 27.12.2015
-------------------------------------------------

Mostly a bugfix release again. The most important fix (preventing dataloss) is that the data is now written atomically. This means that aborting an SDAPS run should not result in a corrupted database anymore.

Important changes:

* model: Write survey file atomically (#79)

* image: compatibility with older glib versions

* csv: Import code fixes (#79)

* latex: Work around manual enumeration breaking automatic numbering

* setup: Create nested directories instead of only one leve

* convert: Support landscape questionnaires (#88)

New and updated languages:

* Arabic

Overview of Changes in SDAPS 1.1.10 -- 19.05.2015
-------------------------------------------------

Again, mostly a bugfix release. One thing to note is that if you are using small fields (i.e. choiceitemtext) is that single characters/digits can sometimes be detected as only dirty. So if you want to use fields with only a single character, then it is likely a good idea to fine tune the minimum size of writing and other aspects of freeform field recognition.

Important changes:

* latex: Fix search paths (#63)

* latex report: Fix formatting issues

* gui: Fix broken display in some corner cases (#67)

* gui: Ensure dialogs are on top of the main window (#66)

* csv: Options to export recognition quality

* Allow filtering based on string replacements for freeform fields (#69)

* latex: Fix encoding issues for some special characters (#70)

* latex: Allow smaller choiceitemtext elements (#68)

New and updated languages:

* French

* German

* Portuguese (Brazil)

* Dutch

Overview of Changes in SDAPS 1.1.9 -- 22.01.2015
------------------------------------------------

Mostly a bugfix release.

Important changes:

* csv: PNG export for complete questions

* Fix various encoding issues (#59, #61)

* dynamic kfill size for barcode detection

* Fix LaTeX search path regression (see #11)

New and updated languages:

* Spanish

Overview of Changes in SDAPS 1.1.8 -- 07.12.2014
------------------------------------------------

Important changes:

* recognize: prevent division by zero error

* recognize: try barcode detection both with and without kfill

* recognize: ignore data from previous run

* csv: Add support to specify delimiter

* csv, ids: allow output to any file including stdout

* gui: properly escape all strings

New and updated languages:

* German

Overview of Changes in SDAPS 1.1.7 -- 02.11.2014
------------------------------------------------

The most important change in this release is that the import of image data has been simplified.

SDAPS can now do an image format conversion automatically as part of the "``add``" command, removing the necessity of using "``convert``" or some other external method to preprocess the images. As before, this feature requires OpenCV.

Another change is that SDAPS now imports PDF files directly. If a PDF file contains a full page image (i.e. a scanned document) then this image is used directly to prevent image quality loss due to resampling. This feature requires poppler to be installed.

Overall these changes make it a lot easier to work with different scanners. It is now only neccessary to pass the "``--convert``" option to the "``add``" command to add files that are not already in the expected format.

Important changes:

* stamp: Fix re-stamping all IDs

* add: Implement conversion feature (``--convert`` option)

* convert: Add support for reading PDF files

New and updated languages:

* German

* Portuguese (Brazil)

Overview of Changes in SDAPS 1.1.6 -- 25.10.2014
------------------------------------------------

This release adds support to use QR code instead of Code-128. The main advantage is that QR-Code contains redundancy so that recognition should be more reliable even with bad scans. Another important change is that it is now possible to select different modes for checkbox detection without modifying the source code. This should simplify the usage of SDAPS in certain cases.

Feedback for optimizing the different modes is of course welcome. The thresholds have not been tested extensively.

Important changes:

* Support for QR-Code based IDs has been added ("qr" style)

* csv export: Allow export of freeform textboxes as images

* Updated example and testcase for newer multicol versions

* tex: Fix writing sdaps file for all macros.

* Allow selection of different checkbox detection modes.

New and updated languages:

* Portoguese (copy of Portoguese (Brazil))

* German

Overview of Changes in SDAPS 1.1.5 -- 21.09.2014
------------------------------------------------

Important changes:

* report: Fix import of PIL (Florian Rinke)

* odt: Fix annotation on setup failure

* gui: Fix memory leak

* latex: Small improvements to class usability

* translations: Fix LaTeX dictionary names.

New and updated languages:

* Finnish

* German

Overview of Changes in SDAPS 1.1.4 -- 04.08.2014
------------------------------------------------

This is mostly a bugfix and translations release, as there was still some fallout from the refactoring done in the last release. Thanks to everyone who submitted patches to fix these!

Important changes:

* dependency, build, and import fixes (#44, #46, and more)

* fix layout changes in LaTeX and example (introduced in 1.1.2)

* report: fix non A4 paper sizes (issue #41)

New and updated languages:

* Portuguese (Brazil)

* Spanish

* German

Overview of Changes in SDAPS 1.1.3 -- 29.05.2014
------------------------------------------------

With this release SDAPS has been restructured internally. There are two reasons for doing this. The first is to improve the API which simplifies the usage of it in custom scripts. Another point is that the old code was incompatible with the import handling of python 3. So doing this change is also a prerequisite for a future port to python 3.x.

Other changes include:

* GUI: Fix an offset error with new GTK+ versions

* GUI: Improved keyboard navigation (issue #30)

* GUI: Improved mouse handling and overlay drawing

* GUI: Show the questionnaire ID on the right side

* GUI: Sort images by page number

* LaTeX: Improved unicode support

* LaTeX: Fixed precision issues in report generation

* LaTeX: Fixed some whitespace issues in the LaTeX class

* ODT: When stamping a single document, keep forms intact

* reorder: Fix reordering of simplex documents

* recognize: Slight changes in the OMR heuristics.

* Fixed issues in the upgrade routine

New and updated translations:

* German

* Spanish

Overview of Changes in SDAPS 1.1.2  -- 27.10.2013
-------------------------------------------------

This release brings a lot of small improvements, but also some new features. The main new feature is the addition of a "convert" module, which can be used to convert non-monochrome scans into monochrome images for later processing. This module is also able to apply 3D-transformations as they are neccessary when the source image was done using a camera.
 This new module requires OpenCV. Note that using a feed scanner is still prefered to this method.

Other changes include:

* LaTeX: Fix compilation of large documents (by suppressing position output)

* LaTeX: Fix multicolumn items and cline at the start of choicequestions

* ODT: Custom styling in answers and question is now possible.

* Various improvements and fixes in the corner mark detection code

* New "custom" style which can be used when customizing the behaviour of SDAPS

* A PDF with annotations will now be created if there was an error during setup

* An issue in the base dir search code that affected OSX has been fixed

New and updated translations:

* Arabic

Overview of Changes in SDAPS 1.1.1 (from 1.1.0) -- 28.06.2013
-------------------------------------------------------------

Important changes:

* Fix the "min coverage" heuristic

* Export text as UTF-8 in CSV files (issue #23)

* report: Ignore empty sheets

* Add "verified" and "recognized" flags for sheets. Recognition will not be done by default if either flag is set.

* GUI: Pressing "Enter" now sets the "verified" flag

* LaTeX class: Paint inner area of boxes white. This is required to allow background coloring.

* Do not ship python-pdftools anymore. It needs to be installed separately now.

And a couple more small bugfixes and additions.

New and updated translations:

* German

* Dutch

23.06.2013
----------

There is some work going on to create a Django based web frontend for SDAPS. This work is in very early stages and can be seen on github_. Some of the basic parts are already there, but it still requires a lot of work until it is ready. Any contributions in this area are welcome (HTML/JavaScript/Django code/design) and will be essential for the success of the project.

15.06.2013
----------

The repository was moved out of the personal account github account into the newly created "sdaps" project. Anyone using GIT might want to update the references.

Overview of Changes in SDAPS 1.0.5 (from 1.0.4) -- 19.05.2013
-------------------------------------------------------------

This release contains an important bugfix that affected the quality of the OMR engine. It was broken with the introduction of circular checkboxes.

The full list of changes:

* Fix the min coverage heuristic.

* Guard against unknown rotation during report creation.

New and updated translations:

* German

Overview of Changes in SDAPS 1.0.4 (from 1.0.3) - 17.04.2013
------------------------------------------------------------

This is a bugfix release. The following changes happened:

* gui: Do not fail if GLib.unix-signal_add_full does not exist

* stamp: Do not duplicate questionnaire IDs when using --existing

* LaTeX translations using PO files.

* ODT stamping in simplex mode works now (issue #22)

* Include example scripts that use the SDAPS python modules directly

New and updated translations:

* German

Overview of Changes in SDAPS 1.1.0
----------------------------------

This release brings a lot of new goodies. As a development release it may still be a bit rough in a few places, but everyone is invited to play with it and report any issues :-)

Important changes:

* Support for duplex scanning of simplex questionnaires (issue #1)

* Freeform fields can be manually replaced with text (issue #14)

* Mark questions can now have an arbitrary checkbox count (issue #7)

* Correctly pick new questionnaire IDs during stamp (issue #22)

* Report paper size is now locale dependend (issue #9)

* LaTeX: classes are now translatable using PO files

* GUI: Widget based view of the questionnaire

* LaTeX_ report: Allow the generated LaTeX to be stored

New and updated translations:

* German

Overview of Changes in SDAPS 1.0.3
----------------------------------

Bugfix so that the SDAPS class works with older PGF versions.

Overview of Changes in SDAPS 1.0.2
----------------------------------

Bugfix so that the commands work fine without a TTY.

Overview of Changes in SDAPS 1.0.1
----------------------------------

Only depend on distutils and pkg_resources if doing a local run.

Overview of Changes in SDAPS 1.0.0
----------------------------------

This is the first release of SDAPS. It is not fully compatible to older versions. Anyone with existing projects should *not* upgrade.

Important changes:

* LaTeX: Improved spacing

* LaTeX: Fix position extraction code

* LaTeX/core: Support for circular/elliptical checkboxes

* LaTeX: now supports multicolumn layouts

* LaTeX: new command to draw a filled checkbox

New and updated translations:

* German

* Arabic

08. November 2012
-----------------

The command line interface has been udpated. Some of the commands have changed slightly. But there are also some new features like specifying output filenames.

The Code-128 style is now the default style when creating new SDAPS projects.

On the TeX front there are two new stared versions of commands:

* \textbox*: A version of the textbox which will not scale in height (as that may cause some problems)

* \checkbox*: A version of the empty checkbox that can be used for examples. Similar to \checkedbox.

25.06.2012
----------

Barcode based stamping
~~~~~~~~~~~~~~~~~~~~~~

This changes a lot of things, so lets describe it here. We actually still support the old codeboxes as the "classic" style. The new Code-128 barcode based system is the "code128" style.

The style is a new concept that is added to SDAPS. It is simply a string option that is stored, which is then used to select the correct algorithms inside the different scripts.

With the new Code-128 barcode style there are some new features:

* An additional "Global-ID" which can be used by the SDAPS user for tracking of their own. The idea is to identify a larger scale survey which this questionnaire is only a small part of.

* No limitation of page count, except for the limitation that duplex questionnaires need to have a multiple of two pages.

Again the different IDs that are printed in Code-128 style. They are:

* Questionnaire-ID; a unique ID for each printed questionnaire. This can be used keep track of each individual questionnaire.
  This is optional.
  This code is printed on the left side.

* Global-ID: Entirely choosen by the user. SDAPS does not care about it, it is only read and stored right now. In the future this data should also be exported in some way.
  The purpose of this ID is to track multiple surveys that are part of a larger study.
  This code is printed in the center.

* Survey-ID/Page Number: This is the code that is used by SDAPS for tracking.
  It is a pseudo random value that is based on the questionnaires layout, and cannot be changed by the user. It consists of the Survey ID + 4 digit page number.
  This code is printed on the right side.

If combined these three barcodes will uniquely identify every page that exists.

.. ############################################################################

.. _github: http://github.com/sdaps/sdaps_web

.. _LaTeX: /LaTeX

.. _class repository: http://github.com/sdaps/sdaps-class

.. _documentation: http://sdaps.org/class-doc

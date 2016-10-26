Documentation
=============

Interface
---------

SDAPS is a command line application. After building the C extension and documentation (and optionally installing it into the system) you can execute it.

* Run 'sdaps' if you installed it

* Run './sdaps.py' from the source directory otherwise.

With ``--help`` you can get a list of commands. To get more information about one of these commands run SDAPS with ``sdaps X command --help``. The X can be any string, it just needs to be there as SDAPS expects a path to a project directory.

Important Commands
~~~~~~~~~~~~~~~~~~

* **setup** or **setup_tex**: Creates a new project directory for the given questionnaire

* **stamp**: Create printable PDF

* **add**: Adds scanned image data. From version 1.1.7 onwards SDAPS will automatically convert files to the appropriate format if the ``--convert`` option is given. Only use this option if the scan is not already in the appropriate format for SDAPS (monochrome multipage tiff). See also Scanning_.

* **recognize**: Runs the optical mark recognition

* **reorder**: Group pages using their (unique) questionnaire ID. (ie. fix order after pages have been mixed up)

* gui_: Starts a graphical user interface that can be used to correct errors in the automatic recognition.

* **report** (and **report_tex**): Creates a report of the results as PDF.

* **csv**: Can be used to export the data to a CSV file.

Filtering
---------

Some commands can work only on a subset of the data (eg. report, csv export). With this it is possible to create a PDF report that is for example separated by the sex of the participant. These filters are python logic expressions.

For the logic expression, every choice question is exported as a list of checked boxes. The list of boxes is zero based and freeform fields are included. The mark type question is instead exported as a number between 0 and 5, where zero means "no answer".

As these are python expressions, you can simply combine them with ``and`` and ``or``. It is allowed to combine such a filter with the ``--all-filters`` argument that the report script has.

Example filter:

* ``0 in _1_2``: First checkbox of question 1.2 is checked (others of the same question may be checked too).

* ``_1_2 == [0]``: Only the first checkbox of question 1.2 is checked.

* ``_2_1 == 1``: Question 2.1 is a mark question, and the leftmost box has been checked.

* ``_2_1 == 0``: Question 2.1 is a mark question, and is not valid (no box, or multiple checked boxes).

Other variables that can be queried:

* survey_id: The survey ID (will always be the correct one)

* questionnaire_id: The questionnaire ID if a barcode was found.

* global_id: The global ID if a barcode was found.

* valid: Whether the sheet is considered valid (ie. no fatal errors).

* quality: The estimated quality of the recognition (a value between 0 and 1).

* recognized: Whether recognition has been run for the sheet. (new since 1.1.1)

* verified: Whether a verifier has acknowledged the sheet. (new since 1.1.1)

* complete: Whether all pages are scanned and could be identified for the sheet. (new since 1.1.2)

Example call of the "report" command:

::

   $ sdaps some_project report --filter "(0 in _1_2 or _2_1 == 1) and global_id=='some name'"

SDAPS Project Directory
-----------------------

SDAPS creates a project directory for every survey you create. This directory is used to store all the data that belongs to the survey. Some special files:

* info: A file containing metadata, this may be modified directly.

* survey: Data storage (pickled python objects)

* *.tif: The scanned images that have been added to the project

It is also used as the default output directory for commands that create new files.

More documentation
------------------

Have a look at the links in the menu. Quite a lot is not yet documented. There are some notes about this in `Documentation/Missing`_.

.. ############################################################################

.. _Scanning: Scanning

.. _gui: GUI

.. _Documentation/Missing: Missing


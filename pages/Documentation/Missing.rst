Stuff that should be described
==============================

.. contents::

The different configurations
----------------------------

"classic" Style
~~~~~~~~~~~~~~~

* Maximum of 6 pages

* Does not require a survey ID to be printed

* Does not allow a "global ID"

* Only allows 16 bit numbers for Questionnaire ID.

"code128" Style
~~~~~~~~~~~~~~~

* Has a Global-ID that can be freely choosen

* Questionnaire ID may contain ASCII (code128 Barcode)

* Requires a Survey ID barcode (for page rotation and page number)

"qr" Style
~~~~~~~~~~

* Same as "code128" but uses a QR-Code with high redundancy for better reliability.

Additional Questions
--------------------

SDAPS has the ability to add data from external sources. This can be useful if only a few extra data points are coming from an external source (eg. a webpage). A small step by step howto of how these can be used would be good.

Same survey, many classes
-------------------------

It often happens that the same questionnaire is used multiple times, and the results need to be separated in the end. SDAPS doesn't have perfect handling for this, and there are different ways to do it:

* Use Global ID. This works by using one project, then changing the global ID multiple times and printing different questionnaires. After everything is recognized one can reports by filtering according to the global ID.

* Use the same questionnaire and separate project.

To modify the text on the report the "info" file can be modified or the "info" command can be used.

Survey ID generation
--------------------

How it is generated (md5 sum of: checkbox position, paper size, ...).

Reordering
----------

* Add data (maybe using ``--force`` if pages are missing)

* Run recognition using ``--identify`` (fast method that only reads the codes)

* Run ``reorder`` command.

* Run ``recognize`` normally

* Use GUI to fix errors as usual

* Export data/create report

The only change is that two steps are inserted before the normal recognize step. The first is the ``recognize --identify`` command, and the second the reorder command which correctly reorders the data.


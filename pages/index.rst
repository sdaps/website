Scripts for data acquisition with paper-based surveys
=====================================================

.. contents:: :depth: 1

SDAPS is an open source (GPLv3, LPPL) optical mark recognition (OMR) program. It is written in python and has an integrated workflow with both LibreOffice and LaTeX to create questionnaires.

.. image:: sdaps.png

With SDAPS you create the questionnaire using either LibreOffice_ or LaTeX_. After this some processing is done to collect the information about the survey (questions, and answers) and a
`printable PDF`_ is created. The filled out questionnaires only need to be scanned in
(`example
<Documentation/Tutorial/example.tif>`__).



SDAPS will do the optical mark recognition and can create a PDF report
(`example
<example-report.pdf>`__)
or export the data. Optionally it is possible to `manually correct the results`_ using a graphical user interface.

Possible use cases for SDAPS include:

* anonymous surveys

* non-anonymous surveys

* evaluation of lectures

* automated data input

* examinations

If you have any questions or comments related to SDAPS (usage, development, or anything else) then the `mailing list`_ is a good place to post these. Please consider subscribing to this list if you are thinking about using SDAPS in the future or should you need some assistance. You can also look around on irc `#sdaps on freenode`_ (webchat_).

For an introduction of how SDAPS is used and what can be done with it you can look at the Tutorial_ and Documentation_. Should you have any further questions about SDAPS you can use the Contact#Mailing_List|. If you find any issues, please report them in the `Issue Tracker`_.

Should you find SDAPS useful and use it for any survey or similar, then please consider contributing_ to the project. A good first start is to subscribe to the `mailing list`_ or to join the `IRC channel`_.

Features
--------

* Open Source Software; use and modify it as you like (subject to the GPLv3+/LPPLv1.3c+)

* Optical mark recognition (OMR) from scanned data

* Imports most formats including PDF and even photographs (version 1.1.7)

* OpenDocument text (ODT) for creating questionnaires

* LaTeX_ class for creating questionnaires

* Supports any paper size

* Multipage questionnaires, both simplex and duplex printing (up to 9999 pages with "code128" and "qr" style)

* Different kinds of questions:

  * A mark type question (a score)

  * A choice of many, that may also include freeform fields

  * Freeform fields

  * The LaTeX class also supports more compact matrix configurations for these.

* Creation of PDF reports for printout

  * Also supports creating reports of only partial result sets with `arbitrary filters`_

* Export of data to CSV files for further analysis (excluding image data)

* Import of additional results from other sources.
  With this it is for example possible to merge data aquired via a webpage at a later point.

* A GUI application to check the recognition and correct errors

* Written in Python using a modular and extensible design

Similar Tools
-------------

Some similar free software projects in no specific order:

* `Auto Multiple Choice`_ (Perl, supports randomized forms, optimized for examinations)

* `G'n'T Eval`_ (Ruby, used for evaluations in Heidelberg, Germany)

* queXF_ (PHP)

.. ############################################################################

.. _LibreOffice: /Documentation/LibreOffice

.. _LaTeX: /LaTeX

.. _scanned: /Documentation/Scanning

.. _manually correct the results: /Documentation/GUI

.. _mailing list: /Contact#Mailing_List

.. _#sdaps on freenode: irc://freenode.net/sdaps

.. _webchat: http://webchat.freenode.net/?channels=sdaps

.. _Tutorial: /Documentation/Tutorial

.. _Documentation: /Documentation

.. _Issue Tracker: https://github.com/benzea/sdaps/issues

.. _contributing: /Contribute

.. _IRC channel: /Contact#IRC

.. _arbitrary filters: /Documentation#Filtering

.. _Auto Multiple Choice: http://auto-multiple-choice.net/

.. _G'n'T Eval: https://github.com/breunigs/gnt-eval

.. _queXF: http://quexf.sourceforge.net/

.. _printable PDF: Documentation/Tutorial/questionnaire.pdf

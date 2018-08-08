Creating a questionnaire using LibreOffice
==========================================

SDAPS is able to read ODT Documents if they are formatted correctly. To find out everything about the questionnaire, SDAPS needs specially named styles in the document itself, and the PDF file to extract more information. This process is quite error prone unfortunately, so you might want to consider using LaTeX_ instead.

.. attention:: You need to run the "stamp" command of SDAPS to create a printable version of the document!

Examples
--------

* `Test document in german`_.

Styles
------

It is important to understand the SDAPS uses the **style names** to find out what part of the document are questions and answers. The following styles exist:

* QObject-Head: For section headings

* QObject-Choice: For a normal multiple choice question (possibly containing freeform fields)

* QObject-Mark: A rating question (arbitrary checkbox count, usually 5)

* QObject-Text: A question with a single freeform text field

* Answer-Choice: The answer text for a choice item

* Answer-Mark: The bottom/top label for the rating question

* Answer-Text: Style around the single Textbox that is part of a text question (QObject-Text)

* Checkbox: A drawing style for the frame elements to mark them as checkboxes.

* Textbox: A drawing style for frame elements to mark them as freeform text fields.

All text and other elements that are not part of a question or answer need to have some other style.

Creating a questionnaire
~~~~~~~~~~~~~~~~~~~~~~~~

When creating a new questionnaire you need to be careful to always pick the correct style. Usually that means that one of the QObject-X styles is followed by the section with the corresponding Answer-X style and with the checkboxes simply put into it. The text for the checkbox must not have any special formatting. The answers are separated by boxes or paragraphs (and tab characters).

This separation technique means that it is possible to both place a label in front or after a box.

Boxes
~~~~~

Checkboxes und freeform text fields are normal frames that are placed into the document. As said before, they need to have a special frame style.

.. attention:: SDAPS can only handle checkboxes that are exactly 3.5x3.5mm large. Textboxes need to be at least 6cm wide and 6mm heigh.

.. attention:: SDAPS reads the PDF file to find the corresponding boxes. You must not add frames to the file that have the same width of the outline! If you want to add instructions about how to handle checkboxes, than these need to be done for example using images.

Debugging
---------

If something went wrong, then it is likely that the setup will abort. In this case it is important to read the output to figure out where the error was.

For example the (german) test document starts like this:

::

   ------------------------------------------------------------------------------
   - SDAPS -- setup
   ------------------------------------------------------------------------------
   Fachschaft Elektro- und Informationstechnik
   AG Lernverhalten
   Datum: 28.07.2008
   Umfrage: Prüfung ES Sommersemester 2008
   Questionnaire
   1.0(Head) Allgemeines
   1.1(Choice) In welchem Studiengang bist Du immatrikuliert? {1}
           0(Checkbox)  23.0  63.6   3.5   3.5 ETIT
           1(Checkbox)  52.0  63.6   3.5   3.5 Anderer
   1.2(Choice) In welchem Fachsemester bist Du? {1}
           0(Checkbox)  23.0  76.4   3.5   3.5 1 – 2
           1(Checkbox)  52.0  76.4   3.5   3.5 3 – 4

The important part is after the "Questionnaire" as it prints all the detected information. It shows you the text for the questions, and it also shows details about the answers.

The number after the question (``{1}``) is the page number. Then the boxes are listed such as:

::

           0(Checkbox)  23.0  63.6   3.5   3.5 ETIT

This tells us that the first box (0) is a checkbox. Its position (as seen from the top left corner) is at 23.0mm, 63.6mm. The size of the checkbox is 3.5x3.5mm.

So, you get the exact position and size in mm. You can also see the type (Checkbox or Textbox).

To find errors please check the following things:

* **Correct Answers**: If any answer is incorrect, then probably something went wrong with the styles. Please go back into the document and simply re-apply the correct style.

* **checkbox positions**: Look closely at the positions for the checkboxes. It can be very helpful to compare which checkboxes are on the same line according to SDAPS.

Annotate
~~~~~~~~

To help with this the development version of SDAPS (will be in version 1.1.2 and later) creates an annotated PDF if an error occurs. This is a normal feature that SDAPS has, but you could not normally use it as the project is not fully created.

If all the dependencies are there, then a "``ORIG_PDF_annotated.pdf``" should be created next to the original PDF document. This PDF contains the same information as the textual representation, but overlayed on top of the original file. This makes it easier to see where the error has happened.

Examples
--------

Here are a couple of example commands, that might be useful. This section is in some regards similar to the Tutorial (which is specific to LaTeX currently). In some regards this page contains more information than the Tutorial, so both pages should be merged in the future.

Creating an ODT based project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first step is to save the ODT and export it into a PDF document using the normal PDF export feature that LibreOffice has.

With the ODT setup routine, you need to specify quite some options on the command line during setup. This is different to the LaTeX class, where the options are read from the original document instead.

You can get a list of options using the ``--help`` command, ie. run:

::

   $ sdaps X setup --help

where ``X`` is just that, any string to make the command line parser happy.

Important options are:

* ``--print-questoinnaire-id``: Using this option means that SDAPS will print an additional barcode, which is unique for every form. This can be useful for multiple reasons:

  * Identify the person filling out the form

  * Automatically reorder multipage documents if pages might get separated during the scanning procedure. (See the ``reorder`` command in the Tutorial_)

* ``--global-id``: This ID will be the same on every printout [#printout]_. The reason to allow for this barcode is that the "survey-id" (bottom right barcode) will be the same for all projects based on the same ODT file (ie. which have the same box positions). So if you need to hand out the same questionnaire in different places, you can use the "global-id" to organize this.

* ``--simplex``**/**``--duplex``: You need to specify whether you want to print the document in simplex or duplex mode. The main difference is that in duplex mode the barcodes are only printed on the back side. Obviously, if you specify ``--duplex`` it is very important to actually print everything in duplex mode!

To create the project, use a command like the following:

::

   $ sdaps /tmp/project setup --duplex questionnaire.odt questionnaire.pdf

or

::

   $ sdaps /tmp/project setup --duplex --print-questionnaire-id --global-id=Test questionnaire.odt questionnaire.pdf

Stamping the document
~~~~~~~~~~~~~~~~~~~~~

After the setup routine it is necessary to do more processing of the document before it can be printed:

* Corner marks need to be added

* Barcodes (survey-id, global-id and questionnaire-id) need to be rendered on the document

If you specified ``--print-questionnaire-id`` above, then you need to provide SDAPS with IDs or it can create random IDs for you. In the case that you have not specified the option, you can simply run:

::

   $ sdaps /tmp/project stamp

once, and a ``stamp_*.pdf`` will appear in the project directory.

To create a "stamped" document with random IDs, you can simply specify the number of questionnaires to output. For example to generate 10 random IDs, you would run:

::

   $ sdaps /tmp/project stamp -r 10

SDAPS stores the generated IDs, so that there won't be a collision if you use this command multiple times.

You can also specify a custom string if you want to. These are specified in a file with one ID per line. So if you used the file:

::

   Hello
   example
   some ID

Then a document with the questionnaires would be created, one each with "Hello", "example" and "some ID" as the questionnaire ID.

To do this run:

::

   $ sdaps /tmp/project stamp -f ids.txt

If you like to work with pipelines, then you can also use '-'. So running

::

   $ echo "Hello" | sdaps /tmp/project stamp -f -

would create one questionnaire with the ID "Hello". Another example would be creating documents with continuous IDs using the "seq" command on UNIX systems:

::

   $ seq 1 25 | sdaps /tmp/project stamp -f -

.. ############################################################################

.. [#printout] You can modify this ID later on by modifying the {{{info}}} file in the project directory.

.. _LaTeX: /LaTeX/

.. _Test document in german: https://github.com/benzea/sdaps/blob/master/test/data/odt-3/debug.odt?raw=true

.. _Tutorial: ../Tutorial/

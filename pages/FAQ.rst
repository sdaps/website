FAQ
===

.. contents::

|/!/| Please also have a look at `Documentation/Examinations`_ as it contains some tricks that might be relevant!

SDAPS is hard to install, is there any more documentation?
----------------------------------------------------------

Unfortunately not. This is an area where contributions would be very much welcome!

Can the Survey ID (lower right barcode) be changed?
---------------------------------------------------

No. This ID identifies the questionnaire uniquely and it is reproducible (i.e. if you recreate the survey using "``setup``" or "``setup_tex``" it will be the same[1]_.

If you *really* want to you can modify the load routine in ``model/survey.py``.

Is it possible to do custom layouts in LaTeX?
---------------------------------------------

Of course it is, however you need to write out some metadata manually. That means using ``\immediate\write\sdapsoutfile{\unexpanded{STRING}}``. Have a look at the generated ``.sdaps`` file and the LaTeX class. You'll need to write out the questions and enough answers for the checkboxes.

There is a `
small example document
<custom.tex>`__ with the
`resulting questionnaire
<custom.pdf>`__ and
`a document with the metadata that SDAPS detected overlayed
<custom_annotated.pdf>`__.

|{i}| You can visually check the assignment of checkboxes to answers/questions using the  ``annotate`` command. Alternatively read the output of the ``setup_tex`` command.

SDAPS complains that poppler is not installed, but it is!
---------------------------------------------------------

Poppler might be installed, but SDAPS needs the python bindings to use it. You need to install the GObject introspection data and python-gi bindings. On Debian based distributions these are in ``gir1.2-poppler-0.18`` and ``python-gi``.

Also, you only need this if you want to import PDF files (using ``add --convert`` or ``convert``. SDAPS will still print the warning even if you do not use PDF.

Why is there no barcode on the first page?
------------------------------------------

By default SDAPS assumes duplex printing. The barcode is only printed on the back of each sheet of paper and used for both the front and back.

If you switch to simplex mode (``--simplex`` for ODT and ``onside`` document class option in LaTeX) then SDAPS renders a barcode on every page.

|{i}| SDAPS automatically detects the case where the questionnaire only has a single page and switches to simplex mode automatically!

|/!/| If you use a simplex document then SDAPS needs to know how you scan it. By default SDAPS assumes a simplex scan! Scanning simplex is usually not a good idea because some pages **will** be flipped and missed that way. So if you can then **always scan the document in duplex mode and pass the** ``--duplex`` **option to the** ``add`` **command**!

Is it possible to put content inside a freeform textbox?
--------------------------------------------------------

In theory yes[2]_, the code below allows this by putting a tikz node into the center. The node has a text width of exactly the white area, and also a minimum height of this area. You can use the ``\textwidth`` and ``\textheight`` macros inside to query the size.

This is quite a hack, but it should work fine (just copy it into the header, and use the command directly after a ``\textbox``).

::

   \makeatletter
   \newcommand{\makenodeinlasttextbox}[1]{%
     \begin{tikzpicture}[remember picture, overlay]%
       \setlength\textheight{\@sdaps@height}
       \advance\textheight by -2pt
       \node[outer sep=1pt, inner sep=0pt, align=center, text width=\@sdaps@width-2pt, minimum height=\textheight, shift={($(\@sdaps@x,\@sdaps@y) + 0.5*(\@sdaps@width, -\@sdaps@height)$)}, anchor=center] at (current page.south west) {%
         #1%
       };
     \end{tikzpicture}
   }
   \makeatother

Use the macro to put content into the textbox:

::

   \textbox*{6cm}{Some textbox}
   \makenodeinlasttextbox{This will appear inside the textbox.}

|/!/| If you use questionnaire IDs and would like to stamp multiple questionnaires at a time, then the above code does not work as is. We need to layer another hack around it.  This is because the class tries to conserve memory and breaks the hack at the same time. We need to enable output again, which needs two steps unfortunately. A new command[3]_:

::

   \makeatletter
   \let\enableoutput\@sdaps@outputtrue
   \makeatother

And then use this command to enable the output again. Best to put it all into braces, so that it will not be enabled for all the other boxes (especially all the checkboxes)

::

   {
     \enableoutput
     \textbox*{6cm}{Some textbox}
     \makenodeinlasttextbox{This will appear inside the textbox.}
   }

-------------------------



.. ############################################################################

.. [1] The only exception is when e.g. a LaTeX package you use is upgraded and changes the layout. But that is the intended behavior as the questionnaire '''has''' changed in that case.

.. [2] Actually, the next major release of SDAPS will natively support this. See [[Future/LaTeX]] and the linked resources for details.

.. [3] This is required to as the parser cannot be reconfigured inside the questionnaire environment.

.. _Documentation/Examinations: ../Documentation/Examinations


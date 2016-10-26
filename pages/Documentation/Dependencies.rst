Dependencies of SDAPS
=====================

SDAPS has a number of dependencies. In some circumstances not all of them will be needed, but it is probably a good idea to just install everything.

general (including recognize):

* Python 2.7

* distutils and distutils-extra

* python-cairo (including development files)

* libtiff (including development files)

* pkg-config

* python-zbar for "code128" style

* python development files

graphical user interface (gui):

* GTK+ and introspection data

* python-gi

reportlab based reports (report):

* reportlab

* Python Imaging Library (PIL)  

ODT based questionnaires (setup/stamp):

* pdftk or pyPdf (pdftk is much faster if you need questionnaire ids)

* python-pdftools

LaTeX based questionnaires (setup_tex/stamp):

* pdflatex and packages:

  * PGF/TikZ

  * translator (part of beamer)

  * and more

LaTeX based reports:

* siunitx

Import of other image formats (convert, add --convert):

* python-opencv

* Poppler and introspection data

* python-gi

Debug output (annotate):

* Poppler and introspection data

* python-gi

Distributions
-------------

Debian wheezy/jessie
~~~~~~~~~~~~~~~~~~~~

On Debian Wheezy/Jessie you should install the following packages:

* python-distutils-extra

* python-cairo-dev

* libtiff5-dev

* libcairo2-dev

* libglib2.0-dev

* python2.7-dev

* python-zbar

* python-gi

* python-gi-cairo

* gir1.2-gtk-3.0

* pdftk (or python-pypdf)

* python-reportlab

* python-imaging

* gir1.2-poppler-0.18

* python-opencv

for the LaTeX class:

* texlive

* texlive-latex-extra

* texlive-latex-recommended

* pgf

* latex-beamer (used for translations)

Other debian based distributions (Ubuntu, Mint) should have very similar package names. For some packages there are also alternatives:

* libtiff4 development files instead of libtiff5

* python-gobject instead of python-gi

* gir1.0-gtk-3.0 or similar (different GObject Introspection version)

OS X
----

Required macports packages (this list is **not** complete):

* py27-gobject3

* gtk3

* py27-distutils-extra

* poppler

* cairo-devel, cairo, py27-cairo

* opencv (with python27 variant)

* tiff

* py27-reportlab

* py27-Pillow (or py27-pil)

* pdftk

Manually installed packages:

* zbar (there is a bug to get it into MacPorts_ https://trac.macports.org/ticket/45604)


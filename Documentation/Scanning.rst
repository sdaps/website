Scanning for SDAPS
==================

For scanning the documents you should have a fast duplex scanner with a document feeder. Many large printer/copier combinations (MFP) can be used for this. There are also smaller stand alone scanners available.

SDAPS requires a monochrome (no greyscale or color) image in the TIFF file format. Most MFPs can directly produce the correct format, with others scanners a conversion step may be required. New versions of SDAPS can do this conversion for you if OpenCV is installed on the system.

Some notes:

* You do not need to care about rotation of the paper

* Pages should be scanned at 300 dpi (good quality, but still fast processing)

* You need a monochrome TIFF as the final format

* Figure out good quality scan options. The pen marks should be mostly black, while white areas shouldn't contain too much dirt.

Scanners tested so far:

* Konica Minolta Bizhub 750. Directly outputs a correct TIFF.

    Used Option: "Printed Image" (German was "Druckbild")

* Canon DR-2510C
  Scanning can be done with:

  ::

     scanimage -d canon_dr:libusb:002:003  --source "ADF Duplex" --mode Lineart --resolution 300 -l 0 -t 0 -x 210 -y 297 --page-height 297 --batch='out%05d.pnm' --batch-count=10 --threshold 150 --brightness -40

* Sharp MX-M753U. Directly outputs a correct TIFF.

    Format: TIFF
     Color: Mono2 (not Auto)
     Duplex mode: "Book"

* HP 4345

    Format: MTIFF (Multipage TIFF)

* Brother DCP7065-DN, Fujitsu ScanSnap ix500

    Tested using VueScan 9.5.08 (TIFF multipage needs to be set in "Output" tab)

Converting Data that is not in the correct format
-------------------------------------------------

With version 1.1.7 of SDAPS the easiest method is to use the SDAPS ``add`` command. Simply do the following:

::

   $ sdaps PROJECT add --convert FILE1 [FILE2 [...]]

This command requires the OpenCV library (python-opencv) for image file support and monochrome conversion. For more details of how this works, have a look at the ``convert`` command section below.

Other methods and utilities for conversion to the correct format are:

* SDAPS "convert" command: Uses OpenCV to do monochrome level conversion and generates a useable TIFF file. Can also be used to de-skew photographs (version 1.1.2 and later).

* convert (imagemagick): This tool can also convert the image data to monochrome. For example:  ``convert scan-*.tiff -threshold 30% -monochrome -units PixelsPerInch -density 300 -compress none scans.tiff``

* tiffcp: Concatenate many TIFF files into one to pass it to SDAPS.

Conversion using SDAPS internal "convert" command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In newer SDAPS versions (ie. 1.1.2 and more recent) there is a "convert" command, which can also be used. This command does require python-opencv to be installed though.  It can handle TIFF files, PDF files and any input file format that OpenCV supports (i.e. pretty much anything). PDF support is only enabled if poppler is installed though (requires version 1.1.7).

The conversion uses a relative slow method for doing the black/white monochrome conversion. This method might produce better results then a bad conversion done by a scanner (e.g. if the scanner dithers the image). The method was chosen as it even works for photographs.

This "convert" feature also has code to de-skew a 3D transformed image like one that might be produced by a phone camera. This is experimental code, but it should work fine under most conditions.

::

   $ sdaps PROJECT convert input_file1.jpg input_file2.jpg [...] -o output.tif

To enable de-skew, add the ``'--3d-transform'`` option.

::

   $ sdaps PROJECT convert --3d-transform input_file1.jpg input_file2.jpg [...] -o output.tif

Conversion using imagemagic
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another way to convert existing image file into a format that can be processed by SDAPS is to use the "convert" command from imagemagic. This command can work with almost any image format, including JPEG and even PDF files.

Imagemagic can do the following for you:

* Reads almost any file format

* Conversion to monochrome using a threshold (``'-threshold 30% -monochrome'``)

* Setting the resolution of the file

* Specifying the compression (eg. "-compress none")

With convert, the command may look as follows:

::

   $ convert INPUT_FILES -threshold 30% -monochrome output.tif

This will convert the input files into a monochrome TIFF. Note that SDAPS expects any resolution tags in the TIFF file to be correct. Should the information in the image be wrong for whatever reason, then you can explicitly specify it:

::

   $ convert INPUT_FILES -threshold 30% -monochrome -units PixelsPerInch -density 300 output.tif

Converting a PDF file
~~~~~~~~~~~~~~~~~~~~~

Some Scanners with an automatic feeder produce PDF format as output files. The feeder  is very convenient for a large number of filled questionnaires, but PDF has to be converted to TIFF for processing with SDAPS.

You can either use imagemagic to do the conversion, or the SDAPS internal convert command (version 1.1.7 and newer, see below).

To convert such files using imagemagic you need to add some extra options. Without these, the produced TIFF will be of a very low quality. The following command creates a 300dpi TIFF file from the input PDF and converts the data to monochrome at the same time should this be required:

::

   $ convert -density 300 input.pdf -threshold 30% -monochrome output.tif

Putting the "-density 300" to the front means that the PDF file will be read using 300 dpi. When putting the "-density 300" later on the command line it only overrides the stored information and has no effect on the image data itself. The latter case is only relevant if the information that was previously stored in the file is wrong.

TIFF compression
~~~~~~~~~~~~~~~~

It appears that sometimes SDAPS may have trouble with compressed TIFF files. If this is the case, then you can also uncompress the file using imagemagic:

::

   convert INPUT_FILES -compress none output.tif

Other resolutions
-----------------

For some time now (14. December 2012, commit c0fd33d) SDAPS should handle arbitrary resolutions just fine. This support works by estimating the DPI based on the image size. It is therefore possible to use higher resolution scans, which could potentially improve the image and recognition quality. However, a higher resolution also means longer processing times and larger image files (SDAPS is still quite fast).

For now 300dpi is the recommended resolution. Should you test SDAPS at other resolutions, we would be happy to hear from you!


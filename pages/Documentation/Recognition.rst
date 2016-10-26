Recognition
===========

Some notes about how SDAPS handles the recognition part.

Checkboxes
----------

SDAPS considers checkboxes that have a cross to be "checked". Boxes that are filled in are **not** checked. This way errors can be corrected by filling in (see below if you would like to change this).

For checkboxes SDAPS does multiple steps:

* find exact position

* run different analysis

* calculate value and quality

The first step is necessary because both scanners and printers tend to distort the image slightly. You might not see it, but any inaccuracies here would mean that SDAPS would not look at the inner area of the checkbox, but at eg. a corner. Obviously that would be bad.

In the second step different heuristics are applied to the image. These heuristics only consider the inner (white) area of the checkbox. There are currently three heuristics:

* **coverage**: Simply calculates the portion black pixels

* **cov-lines-removed**: Finds a line (hough transformation) and draws it over in white. This is done three times. The portion black pixel is calculated after this.BR_By doing this any normal "check" mark will almost entirely disappear.

* **cov-min-size**: Uh, this one is a bit weird, it finds white areas above a certain threshold.

Now, most people reading this that know more about image analysis algorithms probably wonder why SDAPS does not use other algorithms. The answer is that there is no good reason; it just needs to be implemented :-)

In the last step a list for each of the heuristics is traversed and SDAPS selects the "best" solution.

Errors and Mode of Operation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See also README.

The main source of errors is the correction feature. The trouble is that many people fill in the forms rather sloppy. This means that you get boxes that are crossed multiple times, and some that are not filled in properly. Figuring out what is crossed and what is filled in can be rather impossible.

If you would like to change the way that SDAPS works (or just adjust the definitions), you can modify ``defs.py`` in the source directory.

For example, if you would like to consider any box that has markings in it as "checked" you could put there

::

    checkbox_metrics['coverage'] = \
       [(0, 0, 1.0), (0.02, 0, 0.9), (0.03, 0, 0.5), (0.03, 1, 0.5),
        (0.09, 1, 1.0), (0.4, 1, 1.0), (1.0, 1, 1.0)]
    checkbox_metrics['cov-lines-removed'] = [(0, 0, 0), (1.0, 0, 0)]
    checkbox_metrics['cov-min-size'] = [(0, 0, 0), (1.0, 0, 0)]

instead of what is there already.

Textboxes
---------

Textboxes are searched in chunks for content. This usually works pretty good, but can find dirt. Another thing that can be annoying is that SDAPS will detect simple placeholders (ie. people just put a dash in the box to say they don't have a comment).

How it works
~~~~~~~~~~~~

SDAPS needs to analyse the whole area of the textbox. The first step is again to try and find out the exact location. After that the inner area of the textbox is only considered.

Here a 2x2mm tile is considered at a time. This is done with an overlap of 1mm (yes, most of the area will be scanned four times). The bounding box of all tiles that contain black pixels is calculated.

Any bounding box below a certain size is discarded (probably just a speck of dirt; unfortunately this does not help if there are two specks)

At the end the area is increased a bit more, to make sure that there is nothing small missing (eg. the dot of an i).

All the values that were mentioned here are again in ``defs.py``.

Edge markers
------------

There is a lot of C code that solves this. See also the definitions in ``defs.py``.

Future development
------------------

Ideally all this would be rewritten. My thoughts (Benjamin Berg) would be to use numpy where possible. It is likely that some C code is still useful for a couple of algorithms.

It could also be nice to use libraries like OpenCV; however, I would prefer discussing this before making a large library like this a hard dependency for SDAPS.


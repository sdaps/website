---
title: Other things to try
layout: single
----

#### Questionnaire-ID

If it is required, you can put a unique barcode on every created questionnaire.
This is internally called the "Questionnaire-ID" by SDAPS.

To do this, you need to add the `print_questionnaire_id` to the document
class before running the setup routine. The document will now also contain a
barcode for the "Questionnaire-ID" which will be located in the bottom left
corner of the page.

In this setup it is now necessary to generate the required amount of unique
documents. This is done using the `stamp` command in SDAPS. You have the
choice of either creating numeric random IDs, or supplying a set of IDs
(anything that can be encoded in CODE128 is allowed) in a file.

For example, to create 15 questionnaires with randomized IDs you can run

``` bash
$ sdaps stamp /tmp/project -r 15
```

To specify non-random IDs create a file with one ID per line. It might look
like the following. Lets call it `ids.txt`:

``` plaintext
First ID
Second ID
Some Name
```

Then run the stamp command, with the created file as an argument:

``` bash
$ sdaps stamp /tmp/project -f ids.txt
```

Both commands will create a new `stamp_X.pdf` file (where X is a number)
which can be printed.

#### Global-ID

There is a third ID that SDAPS can have (besides the internal Survey-ID and
Questionnaire-ID), which is called the "Global-ID". This ID is printed in
the center of the page and exists for user defined purposes. It is not used
by SDAPS itself but, will be exported for user defined purposes.

An example use case for the "Global-ID" might be handing out the same
questionnaire in different lectures. You could encode the lecture in the
"Global-ID" and separate everything using this information.

#### Annotate

As mentioned before, you can create a PDF to see if the values read from the
designed questionnaire are all correct (checkbox positions, etc.). To use run:

``` bash
$ sdaps annotate /tmp/project
```

The file `annotated_questionnaire.pdf` is created. Might be a bit ugly,
but one can easily check that everything is good.

{{< warning title="Attention" >}}This command requires the GObject
Introspection binding information for poppler to be installed.
{{< /warning >}}

#### Reorder

To try out this command we need a questionnaire that is printed on multiple
pages, and unique Questionnaire-IDs.

If the questionnaire has multiple pages it can happen that the pages get
mixed before the scan happens. The "reorder" command will sort all pages
so that everything is together again.

First identify all pages ie. read all the barcodes:

```bash
$ sdaps recognize /tmp/project --identify
```

Then reorder the pages:

```bash
$ sdaps reorder /tmp/project
```

And when that is done you can do the normal "recognize" step:

```bash
$ sdaps recognize /tmp/project
```

#### Using a camera for input

It is possible to use a cell phone camera image instead of a scanner. Usually
it is a lot faster to use a feed scanner, but there may be certain cases where
this is useful.

Some example images are in [cellphone.tar](/files/cellphone.tar) or
[cellphone-2.tar](/files/cellphone-2.tar) (the second one is required
if you have a newer version of the multicol package). To try it, extract the
archive (in this example to /tmp/ and then run the following commands:

``` bash
$ sdaps convert /tmp/project --3d-transform /tmp/cellphone/*.jpg --output /tmp/out.tif
$ sdaps add /tmp/project /tmp/out.tif
```

The `--3d-transform` is important as the SDAPS main Program only does a
2D transformation which is not good enough for camera images (as they usually
will not be taken exactly from above).

After this, the normal recognize step is done.

{{< warning title="Attention" >}}This only works if the tolerance is large
enough. You need a version above 1.1.4 or git, or you have to modify
`defs.py` and change the value of `corner_mark_min_length` to
something smaller (e.g. 15).{{< /warning >}}


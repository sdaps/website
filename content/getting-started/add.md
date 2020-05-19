---
title: Adding Scans to a Project
layout: single
---

You can add scans to the survey directory that was created earlier. This is
done using the `add` command. SDAPS uses `.tif` files as default for `add`,
so you need to add the option `--convert`, if your scanner (like most of them)
give you pdfs:

``` bash
$ sdaps add /tmp/project example-scan.pdf --convert
----------------------------------------
- SDAPS -- add
----------------------------------------
Converting input files into a single temporary file.
~/example-scan.pdf: Not a TIFF or MDI file, bad magic number 20517 (0x5025).
Processing /tmp/sdaps-convert-abc123.tif
Done
```

If everything worked fine you will see no further output. The original file is
copied into the project directory as `1.tif`.

You can repeat this step if you have multiple scans.

{{< warning title="Attention" >}}Do **not** remove or modify the copied TIFF
files. SDAPS stores information that references these files (ie. it creates a
record for each page). If you accidentally added a file, you can recreate the
project and start from scratch.{{< /warning >}}

If you run into errors, because of the page count of your pdfs, take a look
at ["Multipage Answer Sheets"](/documentation/examinations).



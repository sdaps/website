---
title: Unstable release SDAPS 1.9.9
type: post
date: 2020-05-02
---

Please note that the system LaTeX files will be used preferentially from
now on. However, upstream TeX Live has a bug and sdapscode128.tex is
installed to the wrong directory, making the class unusable.

As such, distributions should continue to use the LaTeX files provided in
this bundle (pass `--build-tex`/`--install-tex`). Alternatively, it is also
possible to fix the install location of the mentioned file.

Another important change is that the command line arguments have been
restructed. The aim here is to make all commands more consistent by
grouping them based on their purpose. Some commands have become more
verbose or the order of arguments has changed.

<!--more-->

Important changes:

 - LaTeX files are only installed when requested now (#200)
 - Create export, import, setup and report command groups (#210)
 - Add pandas based intermediate export helper (#4)
 - Add feather data export (requires pyarrows)
 - Accept UTF-8 in LaTeX metadata file (#208)
 - Fix incorrect notifications causing a GUI failure (#211)

New and updated languages:

 - Spanish
 - French

---
title: Ideas for future developments
layout: single
---

If you are interested in helping with any of these developments, then please
write to Benjamin Berg or drop by on IRC.

## Common questionnaire description format

See also [Specification](#specification).

Some people started to work on a description format for questionnaires. Some of
the features that you can expect from such a format:

* Versioning information
* Metadata for question layout
* Metadata for data analysis (e.g. hidden variables)
* Translation support
* Automatic survey creation (both online and offline; e.g. SDAPS and
limesurvey, but it is not specific to these)
* XML based?

This project is not specific to SDAPS. However a close collaboration is planned
so that SDAPS will work with it.

## Webservice

Because many people aren't used to use the command line, we wanna provide an
interface that can be used by everyone. Benjamin already created a proof of
concept with the Django webframework for Python, that implements the baseline
of features. It's called [`sdaps_web`](https://github.com/sdaps/sdaps_web )
and you can take a look at an older version [here](https://demo.sdaps.org/ ).


Right now it is heavily worked on. If you want to get envolved, just join our
IRC/Matrix room.

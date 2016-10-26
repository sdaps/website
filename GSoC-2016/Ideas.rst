Project Ideas
-------------

Handwriting Recognition
~~~~~~~~~~~~~~~~~~~~~~~

**Mentors:** Benjamin Berg (SDAPS, integration), Jeremie/Adam? (recognition, neural networks)

In recent years there have been great improvements in deep learning and neural networks. With these new developments and emergence of multiple frameworks to develop deep learning software it is possible to tackle the issue if handwriting recognition from paper forms in new and exciting ways.

Previous attempts were focused on simpler frameworks like Gamera (see `issue 15`_). In this project we would like to move beyond frameworks like Gamera and instead use neural networks in conjunction with deep learning to solve the issue. With this technology a larger neural network should be able to first find the characters in the input image and then output the plain text belonging to the whole image.

The project is split into two parts which are equally important,

1. research deep learning frameworks and build a working handwriting recognition and

#. integration into the core of SDAPS.

Because of scope of the project it would be of advantage if a student applying can demonstrate some basic knowledge about machine learning and or hands on development of free/python based software.

Web fronted for SDAPS
~~~~~~~~~~~~~~~~~~~~~

**Mentors:** Benjamin Berg

For a quite a while now a basic `web fronted for SDAPS`_ does exist (demo_[1]_), however this never got past the proof of concept state.

The goal of this project is to create a usable web fronted for SDAPS. As such it will require working on both the new web frontend and the core of SDAPS (for example `SQLite based storage`_).

.. ############################################################################

.. [1] The demo is quite often down due to bugs, ping on IRC if it is and you want to try it

.. _issue 15: https://github.com/sdaps/sdaps/issues/15

.. _web fronted for SDAPS: https://github.com/sdaps/sdaps_web

.. _demo: http://demo.sdaps.org

.. _SQLite based storage: https://github.com/sdaps/sdaps/issues/3


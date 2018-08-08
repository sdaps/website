Graphical User Interface for manual corrections
===============================================

The graphical user interface is a GTK+ program that can be used to manually correct errors.

.. image:: screenshot.png

Getting started
---------------

The application is started in the same way as other SDAPS commands:

::

   $ sdaps /path/to/project gui

Interface
---------

The interface is quite simple, but has the most important features. Using the toolbar you can switch pages, change the zoom and switch into full screen mode.

There are also some options that are specific to the currently shown page. With this it may be possible to "rescue" broken scans that SDAPS could not work with. It is quite unlikely that you ever need this. The "Sheet Valid" button marks whether  the the current questionnaire should be included in the final report or data export.

Using the "Sort by Quality" button you can sort by the detection quality. This way you can quickly check the questionnaires that are most likely to contain errors.

Modifying the Data
~~~~~~~~~~~~~~~~~~

In the view below you are shown the scanned image with  the detected results already marked. Checkboxes are blue boxes that are filled if they are checked. You can simply click them to toggle the state.

Freeform fields that contain text have a thicker border. You can drag each of the four sides to select the area that contains writing. Again, clicking into the box toggles the state (ie. whether there is text or not). 

The widget will keep its current scroll position when switching pages. This means you can set up the scale and scroll position once to see the whole questionnaire, and then only need to tab forward/backward. Using this feature corrections can be done very quickly.
 It can make sense to change the rotation of the monitor to have a larger screen area.

Keyboard Shortcuts
::::::::::::::::::

Some of these shortcuts only work if the preview window is selected. ie. you need to click on the image before using them.

=========== =========
Tab         Go to next Page
Shift+Tab   Go to previous Page
Enter       Go to next Page and set "Sheet Validated"
Shift+Enter Go to previous Page and set "Sheet Validated"
=========== =========

Mouse Interaction
:::::::::::::::::

============ =======
Middle click Grab and scroll the view
Click        Toggle the state of checkboxes and freeform fields
Click+Drag   Change the size of freeform fields
Right-Click  Focus the corresponding widget on the right (Version 1.1.0 and newer)
============ =======

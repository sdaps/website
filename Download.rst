Download
========

All releases are available from http://sdaps.org/releases/:

* `sdaps-1.1.11.tar.gz`_ (development snapshot)

* `sdaps-1.0.5.tar.gz`_ (latest stable version, it is currently better to use the unstable version)

|/!/| Currently it is a good idea to use the latest development snapshot. This will become 1.2.0 soon and is actually more stable than the older version.

Development Version
-------------------

To get the latest development version you can create a git checkout of the repository using:

::

   git clone https://github.com/sdaps/sdaps.git

You can `browse the repository on github`_ where you can also `download the latest development snapshot`_ as a ZIP file.

See the list of Dependencies_ to get SDAPS running. The main development target are GNU based operating systems (e.g. GNU/Linux).

Ubuntu/Debian Packages
----------------------

There are two launchpad PPA repositories that contain SDAPS. One contains the latest stable version, the other one the latest unstable version.

* stable: https://launchpad.net/~benjamin-sipsolutions/+archive/sdaps-stable/

* unstable: https://launchpad.net/~benjamin-sipsolutions/+archive/sdaps/

The packages are build for Ubuntu 'trusty' (only unstable currently, old ones are for 'precise'). The packages should work on other debian based systems.

Gentoo Overlay
--------------

There is now a Gentoo overlay to simply the installation of SDAPS on this distribution. The overlay is in a `github repository`_. Please refer to the README on github.

OSX
---

It should be possible to get SDAPS to work using MacPorts. However, there are currently some `unresolved issues`_. These should not be hard to fix, and you are welcome to try it.

See Dependencies_ for a list of packages that are required on OSX.

|/!/| There are reports that the correction GUI is very slow on OSX. This is likely a bug in cairo. At least on Linux the GUI is very fast so that page switching is usually not perceptible.

Windows
-------

There is **no** windows version for SDAPS. In theory it should be possible to get it running, but getting all the dependencies to work will be a big task.

It is likely much simpler to install a GNU/Linux distribution on the computer or inside a virtual machine.

.. ############################################################################

.. _sdaps-1.1.11.tar.gz: http://sdaps.org/releases/sdaps-1.1.11.tar.gz

.. _sdaps-1.0.5.tar.gz: http://sdaps.org/releases/sdaps-1.0.5.tar.gz

.. _browse the repository on github: https://github.com/sdaps/sdaps

.. _download the latest development snapshot: https://github.com/sdaps/sdaps/archive/master.zip

.. _Dependencies: ../Documentation/Dependencies

.. _github repository: https://github.com/sdaps/gentoo-overlay

.. _unresolved issues: https://github.com/sdaps/sdaps/issues/12


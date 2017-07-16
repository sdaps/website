Download
========

All releases are available from http://sdaps.org/releases/:

* `sdaps-1.2.0.tar.gz`_ (latest stable version)
* `sdaps-1.9.0.tar.gz`_ (experimental development snapshot for SDAPS 2.0)

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

.. attention:: There are reports that the correction GUI is very slow on OSX. This is likely a bug in cairo. At least on Linux the GUI is very fast so that page switching is usually not perceptible.

Windows
-------

There is **no** windows version for SDAPS. However Windows 10 introduced the `Windows Subsystem for Linux`_ enabling you to run
Linux applications natively on Windows. This means that you can run a full Linux system on Windows without the need
for a virtual machine or similar. Once you have this the installation is almost identical to the Ubuntu one.

First follow the `Bash on Windows Installation Guide`_. Once you have bash working you can run the following commands (as on Ubuntu) to
install SDAPS.

::

   # add-apt-repository ppa:benjamin-sipsolutions/sdaps
   # apt-get update
   # apt-get install sdaps

To use the user interface you will need to install an X server such as Xming separately. If you do so, you will be
able to run the user interface after setting the correct environment variables:

::

   $ export DISPLAY=:0
   $ sdaps test-project gui

.. image:: screenshot-windows.png
   :width: 100%

.. ############################################################################

.. _sdaps-1.9.0.tar.gz: http://sdaps.org/releases/sdaps-1.9.0.tar.gz

.. _sdaps-1.2.0.tar.gz: http://sdaps.org/releases/sdaps-1.2.0.tar.gz

.. _browse the repository on github: https://github.com/sdaps/sdaps

.. _download the latest development snapshot: https://github.com/sdaps/sdaps/archive/master.zip

.. _Dependencies: ../Documentation/Dependencies

.. _github repository: https://github.com/sdaps/gentoo-overlay

.. _unresolved issues: https://github.com/sdaps/sdaps/issues/12

.. _Windows Subsystem for Linux: https://blogs.msdn.microsoft.com/wsl/2016/04/22/windows-subsystem-for-linux-overview/

.. _Bash on Windows Installation Guide: https://msdn.microsoft.com/en-us/commandline/wsl/install_guide

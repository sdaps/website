---
title: Installation
layout: single
---


| Ubuntu
| ----------------
| [![](/images/ubuntu.png)](https://launchpad.net/~benjamin-sipsolutions/+archive/sdaps-stable/ )
| [**PPA (stable)**](https://launchpad.net/~benjamin-sipsolutions/+archive/sdaps-stable/ ) or [**PPA (unstable)**](https://launchpad.net/~benjamin-sipsolutions/+archive/sdaps/) and other Debian-based Distros like LinuxMint.
| {{< spoiler "Commands" >}}
  `sudo add-apt-repository ppa:benjamin-sipsolutions/sdaps` or `/sdaps-unstable` \
  `sudo apt-get update` \
  `sudo apt-get install sdaps`
  {{< /spoiler >}}

| Debian
| ----------------
| ![](/images/debian.png)
| Install the PPA for **ubuntu** or click on the instructions to build it from source under the tables.

| Fedora
| ----------------
| [![](/images/fedora.png)](https://copr.fedorainfracloud.org/coprs/benzea/sdaps/)
| [**COPR (unstable)**](https://copr.fedorainfracloud.org/coprs/benzea/sdaps/)
| {{< spoiler Commands >}}
  `sudo dnf copr enable benzea/sdaps` \
  `sudo dnf install sdaps`
  {{< /spoiler >}}

| ArchLinux
| ----------------
| [![](/images/arch.png)](https://aur.archlinux.org/packages/sdaps-git)
| [**'sdaps-git' (unstable)**](https://aur.archlinux.org/packages/sdaps-git) latest master branch via [AUR](https://aur.archlinux.org/)
| {{< spoiler Commands >}}
  To install AUR packages we recommend [`yay`](https://github.com/Jguer/yay ).
  Install that and then type

  `yay -S sdaps-git`
  {{< /spoiler >}}

| Gentoo
| ----------------
| [![](/images/gentoo.png)](https://github.com/sdaps/gentoo-overlay)
| [**Gentoo-Overlay (unstable)**](https://github.com/sdaps/gentoo-overlay)
| {{< spoiler Commands >}}
  Install [layman](https://wiki.gentoo.org/wiki/Layman):

  ```
  layman -o \
  https://raw.githubusercontent.com/sdaps/gentoo-overlay/master/overlay.xml \
  -f -a sdaps-overlay
  ```
  {{< /spoiler >}}

| MacOS
| ----------------
| ![](/images/macos.png)
| We'll try to bring it to you via [homebrew](https://brew.sh/). [Github Issue #140](https://github.com/sdaps/sdaps/issues/140)

| From Source
| ----------------
| You can find sdaps tarballs [here](/releases/) and the instructions down below.

{{< spoiler "Open instructions for building from source" >}}

Instructions:

### General Dependencies

SDAPS has a number of dependencies. In some circumstances not all of them will
be needed, but it is probably a good idea to just install everything.

general (including recognize):

* Python 3
* distutils and distutils-extra
* python-cairo (including development files)
* libtiff (including development files)
* pkg-config
* python-zbar for "code128" style
* python development files

graphical user interface (gui):

* GTK+ and introspection data
* python-gi

reportlab based reports (report):

* reportlab
* Python Imaging Library (PIL)

LaTeX based questionnaires (`setup tex`/`stamp`):

* pdflatex and packages:
* PGF/TikZ
* translator (part of beamer)
* and more

LaTeX based reports:

* siunitx

Import of other image formats (convert, use `add PROJECT_DIR --convert`):

* python-opencv
* Poppler and introspection data
* python-gi

Debug output (annotate):

* Poppler and introspection data
* python-gi


#### Debian Wheezy/Jessie

On Debian Wheezy/Jessie you should install the following packages:
```bash
python-distutils-extra python-cairo-dev libtiff5-dev libcairo2-dev \
libglib2.0-dev python2.7-dev python-zbar python-gi python-gi-cairo \
gir1.2-gtk-3.0 python-reportlab python-imaging gir1.2-poppler-0.18 \
python-opencv pdftk # (pdftk or python-pypdf)
```

for the LaTeX class:
```bash
texlive texlive-latex-extra texlive-latex-recommended pgf latex-beamer \
# latex-beamer: (used for translations)
```

Other debian based distributions (Ubuntu, Mint) should have very similar
package names. For some packages there are also alternatives:

* `libtiff4` development files instead of libtiff5
* `python-gobject` instead of python-gi
* `gir1.0-gtk-3.0` or similar (different GObject Introspection version)


### Setup

Clone the repo while installing the submodules with `--recursive`:
```bash
git clone --recursive https://github.com/sdaps/sdaps.git
```

If you want to install sdaps, so you can use it from the general command line,
then change in the cloned repo folder:
```bash
./setup.py install
```
or if you want to run it directly from the cloned folder:
```bash
./setup.py build
```

{{< /spoiler >}}



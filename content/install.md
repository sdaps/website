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
| You may be able to install the PPA for **Ubuntu**, or build from source.

| Fedora
| ----------------
| [![](/images/fedora.png)](https://copr.fedorainfracloud.org/coprs/benzea/sdaps/)
| [**COPR (unstable)**](https://copr.fedorainfracloud.org/coprs/benzea/sdaps/)
| {{< spoiler Commands >}}
  `sudo dnf copr enable benzea/sdaps` \
  `sudo dnf install sdaps`
  {{< /spoiler >}}

<!--
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
| You can find sdaps tarballs [here](/releases/). Please see the included README file for instructions.
-->


### Installing from source

You can find sdaps tarballs [here](/releases/). Please see the included [README file](https://github.com/sdaps/sdaps#installation) for instructions.

To build the current development version, grab it using
```bash
git clone --recursive https://github.com/sdaps/sdaps.git
```

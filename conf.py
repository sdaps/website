# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time
import subprocess, tempfile, os, shutil

def cssmin(infile):
    tmpdir = tempfile.mkdtemp(prefix="johannes")
    tmpfname = os.path.join(tmpdir, os.path.basename(infile))
    try:
        subprocess.check_call('cssmin', stdin=open(infile, 'r'),
                              stdout=open(tmpfname, 'w'))
        shutil.move(tmpfname, infile)
    except Exception:
        raise Exception("cssmin is not installed.")
    finally:
        shutil.rmtree(tmpdir)

def uglifyjs(infile):
    tmpdir = tempfile.mkdtemp(prefix="johannes")
    tmpfname = os.path.join(tmpdir, os.path.basename(infile))
    try:
        subprocess.check_call('uglifyjs', stdin=open(infile, 'r'),
                              stdout=open(tmpfname, 'w'))
        shutil.move(tmpfname, infile)
    except Exception:
        raise Exception("uglifyjs is not installed.")
    finally:
        shutil.rmtree(tmpdir)

BLOG_AUTHOR = "Benjamin Berg"  # (translatable)
BLOG_TITLE = "SDAPS"  # (translatable)
SITE_URL = "http://sdaps.org/"
BLOG_EMAIL = "benjamin@sipsolutions.net"
BLOG_DESCRIPTION = ""  # (translatable)

USE_SLUGIFY = False

DEFAULT_LANG = "en"

TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "de": "./de",
}

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ('/Contribute/', 'Contribute'),
        ('/Contact/', 'Contact'),
        ('/Download/', 'Download'),
        ('/FAQ/', 'FAQ'),
        ('/Support/', 'Support'),
        ('https://github.com/sdaps/sdaps/issues', 'Issue Tracker'),
        ('/NEWS/', 'News'),
        ('/Documentation/Tutorial/', 'Tutorial'),
        ((
          ('/Documentation/Dependencies/', 'Dependencies'),
          ('/LaTeX/', 'LaTeX'),
          ('/Documentation/LibreOffice/', 'LibreOffice'),
          ('/Documentation/Scanning/', 'Scanning'),
          ('/Documentation/GUI/', 'GUI'),
          ('/Documentation/Recognition/', 'Recognition'),
          ('/Documentation/Examinations/', 'Examinations'),
          ('/Documentation/Missing/', 'Missing'),
         ), 'Documentation'),
        ('/References/', 'References'),
        ('/Impressum/', 'Impressum'),
    ),
}

# Name of the theme to use.
THEME = "material-theme"

# Below this point, everything is optional

POSTS = ()
PAGES = (
    ("pages/*.rst", "", "story.tmpl"),
)

COMPILERS = {
    "rest": ('.rst',),
}

WRITE_TAG_CLOUD = False

HIDDEN_TAGS = ['mathjax']

PRETTY_URLS = True

SHOW_SOURCELINK = False
COPY_SOURCES = False

GENERATE_RSS = False
GENERATE_ATOM = False

DISABLED_PLUGINS = ["render_indexes"]

FILTERS = {
  ".css": [cssmin],
  ".js": [uglifyjs],
}

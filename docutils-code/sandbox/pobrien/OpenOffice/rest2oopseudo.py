#!/usr/bin/env python

"""
A minimal front end to the Docutils Publisher, producing pseudo-XML.
"""

__author__ = "Patrick K. O'Brien <pobrien@orbtech.com>"
__cvsid__ = "$Id: rest2oopseudo.py 1777 2003-12-22 21:44:32Z pobrien $"
__revision__ = "$Revision: 1777 $"[11:-2]

import locale
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description

import OOdirectives

description = ('Generates pseudo-XML from standalone reStructuredText '
               'sources (for testing purposes).  ' + default_description)

publish_cmdline(description=description)

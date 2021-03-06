#!/usr/bin/env python

"""Generates the OpenOffice.org content.xml file outside of a .swx zip
file. Useful for debugging the OOwriter."""

__author__ = "Patrick K. O'Brien <pobrien@orbtech.com>"
__cvsid__ = "$Id: rest2ooxml.py 1777 2003-12-22 21:44:32Z pobrien $"
__revision__ = "$Revision: 1777 $"[11:-2]

import locale
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description

from OOwriter import Writer


def main():
    description = ("Generates OpenOffice.org XML.  " + default_description)
    publish_cmdline(writer=Writer(), description=description)


if __name__ == '__main__':
    main()

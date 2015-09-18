#!/usr/bin/env python

"""
:Author: David Goodger
:Contact: goodger@users.sourceforge.net
:Revision: $Revision: 826 $
:Date: $Date: 2002-10-18 01:10:33 -0400 (Fri, 18 Oct 2002) $
:Copyright: This module has been placed in the public domain.

A minimal front-end to the Docutils Publisher, producing HTML.
"""

import locale
locale.setlocale(locale.LC_ALL, '')

from docutils.core import publish_cmdline


usage = '%prog [options] [source [destination]]'
description = ('Generate LaTeX documents from standalone reStructuredText '
               'sources.')

publish_cmdline(writer_name='latex', usage=usage, description=description)

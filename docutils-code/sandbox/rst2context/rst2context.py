#!/usr/bin/env python

# Author: Lalo Martins
# Contact: lalo@laranja.org
# Revision: $Revision: 7311 $
# Date: $Date: 2012-01-09 21:33:33 -0500 (Mon, 09 Jan 2012) $
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing ConTeXt.
"""

import locale, sys
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates ConTeXt documents from standalone reStructuredText '
			   'sources.  ' + default_description)

publish_cmdline(writer_name='context', description=description)

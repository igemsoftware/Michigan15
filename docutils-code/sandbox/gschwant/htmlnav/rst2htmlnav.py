#!/usr/bin/env python

# Author: Gunnar Schwant
# Contact: g.schwant@gmx.de
# Revision: $Revision: 1408 $
# Date: $Date: 2003-06-09 15:30:46 -0400 (Mon, 09 Jun 2003) $
# Copyright: This module has been placed in the public domain.

import locale
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description

description = (default_description)

publish_cmdline(writer_name='htmlnav', description=description)

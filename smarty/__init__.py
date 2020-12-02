#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================
"""How to use smarty
=================

# >>> from smarty import advice
# >>> advice('Die Interviews dauern zwischen 33 und etwa 91 Minuten.')
'dauerten zwischen 30 und 90 Minuten'

class Advice:
    finding: str
    better: str
    readmore: str

# >>> from smarty import bad
# >>> bad('Eine Folge davon kann sein, dass innerfamiliäre Beziehungen'
# ... 'häufig einer großen Belastung ausgesetzt sind.)'
# ['kann sein', 'großen']
"""

import os

from smarty.badwords.judge import badwords_judge
from smarty.badwords.judge import ratio_fat

__version__ = '0.0.0'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PACKAGE = 'smarty'

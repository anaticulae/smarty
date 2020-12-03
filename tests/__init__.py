#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import iamraw
import power
import serializeraw
import words.path


def load_text(source: str) -> iamraw.PageContentTexts:
    source = power.link(source)
    headlines = words.path.headlines(source)
    headlines = serializeraw.load_headlines(headlines)
    text = words.path.text(source)
    text = serializeraw.load_text(text, headlines=headlines)
    return text

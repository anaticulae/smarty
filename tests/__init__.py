#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import iamraw
import power
import serializeraw
import utilatest

import smarty


def load_text(source: str, pages: tuple = None) -> iamraw.PageContentTexts:
    utilatest.fixture_requires(source)
    source = power.link(source)
    headlines = serializeraw.load_headlines(source, pages=pages)
    text = serializeraw.load_text(
        content=source,
        headlines=headlines,
        pages=pages,
    )
    return text


run, fail = utilatest.create_cli_runner(smarty)

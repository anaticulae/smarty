# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import utila

import smarty.badwords

SCIENCELESS = utila.splitlines("""\
beeindruckend
sensationell
""")
PROCESS = smarty.badwords.FromText(tokens=SCIENCELESS)


@utila.cacheme
def scienceless_search(sentence: str):
    return PROCESS.search(sentence)


def scienceless_fromtext(sentences) -> iamraw.TextAdviceDelete:
    return PROCESS.callme(sentences)

# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections

import smarty.utils


def count_words(text) -> dict:
    words = smarty.utils.words_fromtext(text, nomarks=True)
    collected = collections.defaultdict(int)
    for word in words:
        collected[word.lower()] += 1
    result = dict(collected)  # enable KeyError
    return result

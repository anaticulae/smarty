# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections

import smarty.utils


def count_words(text) -> dict:
    wordlist = smarty.utils.words_fromtext(text, nomarks=True)
    collected = collections.defaultdict(int)
    for word in wordlist:
        collected[word.lower()] += 1
    result = dict(collected)  # enable KeyError
    return result


def count_questions(text) -> int:
    result = 0
    for _, sentence in smarty.utils.sentences(text):
        if '?' in sentence[-5:]:
            result += 1
    return result


def ratio_questions_fromtext(text) -> float:
    sentence_count = len(list(smarty.utils.sentences(text)))
    question_count = count_questions(text)
    if not sentence_count:
        return None
    return question_count / sentence_count

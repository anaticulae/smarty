# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import german
import konrad

import smarty.utils


def grams(sentences) -> list:
    threes, fives = [], []
    for page, number, sentence in smarty.utils.sentences(
            sentences,
            numbers=True,
    ):
        words = german.word_tokenize(sentence, validate_sentences=False)
        five = five_gram(words)
        if five:
            fives.append((page, number, five))
        three = three_gram(words)
        if three:
            threes.append((page, number, three))
    return threes, fives


def five_gram(words) -> str:
    result = []
    ngrams = german.ngram(words, length=5)
    for ngram in ngrams:
        minus = ngram[1] == konrad.Mark.HYPHEN
        if not minus:
            continue
        minus &= ngram[3] == konrad.Mark.HYPHEN
        if not minus:
            continue
        ngram = list(ngram)
        try:
            ngram[0] = german.word_normalize(ngram[0]).lower()
            ngram[2] = german.word_normalize(ngram[2]).lower()
            ngram[4] = german.word_normalize(ngram[4]).lower()
        except TypeError:
            continue
        item = german.token_plain(ngram)
        result.append(item)
    return result


def three_gram(words) -> str:
    result = []
    ngrams = german.ngram(words, length=3)
    for ngram in ngrams:
        minus = ngram[1] == konrad.Mark.HYPHEN
        if not minus:
            continue
        ngram = list(ngram)
        try:
            ngram[0] = german.word_normalize(ngram[0]).lower()
            ngram[2] = german.word_normalize(ngram[2]).lower()
        except TypeError:
            continue
        item = german.token_plain(ngram)
        result.append(item)
    return result

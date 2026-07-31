# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections

import configos
import germania
import konradus
import utilo

import smarty.utils

# TODO: MAKE DOCUMENT/MAINPART LENGHT DEPENDENT
FIVE_GRAM_MIN = configos.HV_INT_PLUS(default=5)

THREE_GRAM_MIN = configos.HV_INT_PLUS(default=8)

HyphenError = collections.namedtuple('HypenError', 'page sentence token raw')


def missing(sentences) -> list:  # pylint:disable=R0914
    threes, fives = grams(sentences)
    five_valid = determine_valid(
        fives,
        count_min=FIVE_GRAM_MIN,
    )
    three_valid = determine_valid(
        threes,
        count_min=THREE_GRAM_MIN,
    )
    failures = []
    pattern_three = create_pattern_three(three_valid)
    pattern_five = create_pattern_five(five_valid)
    for page, number, sentence in smarty.utils.sentences(
            sentences,
            numbers=True,
    ):
        tokens = germania.word_tokenize(
            sentence,
            token_normalize=True,
            validate_sentences=False,
        )
        triple_failure = germania.searches(
            patterns=pattern_five,
            sentence=tokens,
            tokens_complex=False,
            verbose=True,
        )
        if triple_failure:
            triple_failure = [
                HyphenError(
                    page=page,
                    sentence=number,
                    token=tokens,
                    raw=tuple(raws),
                ) for tokens, raws, in zip(*triple_failure)
            ]
            failures.extend(triple_failure)
            for failure in triple_failure:
                for index in utilo.rlist(*failure.token):
                    # overwrite failure words to avoid double detection
                    tokens[index] = None
        double_failure = germania.searches(
            patterns=pattern_three,
            sentence=tokens,
            tokens_complex=False,
            verbose=True,
        )
        if double_failure:
            double_failure = [
                HyphenError(
                    page=page,
                    sentence=number,
                    token=tokens,
                    raw=tuple(raws),
                ) for tokens, raws, in zip(*double_failure)
            ]
            failures.extend(double_failure)
    return failures


def grams(sentences) -> list:
    threes, fives = [], []
    for page, number, sentence in smarty.utils.sentences(
            sentences,
            numbers=True,
    ):
        words = germania.word_tokenize(sentence, validate_sentences=False)
        five = five_gram(words)
        if five:
            fives.append((page, number, five))
        three = three_gram(words)
        if three:
            threes.append((page, number, three))
    return threes, fives


def determine_valid(items, count_min: int):
    collected = collections.Counter()
    for detected in items:
        for item in detected[2]:
            collected[item] += 1
    valid = [
        (key, value) for key, value in collected.items() if value >= count_min
    ]
    # put the most common to the front
    valid.sort(key=lambda x: x[1], reverse=True)
    return valid


def five_gram(words) -> str:
    result = []
    ngrams = germania.ngram(words, length=5)
    for ngram in ngrams:
        minus = ngram[1] == konradus.Mark.HYPHEN
        if not minus:
            continue
        minus &= ngram[3] == konradus.Mark.HYPHEN
        if not minus:
            continue
        ngram = list(ngram)
        try:
            ngram[0] = germania.word_normalize(ngram[0]).lower()
            ngram[2] = germania.word_normalize(ngram[2]).lower()
            ngram[4] = germania.word_normalize(ngram[4]).lower()
        except TypeError:
            continue
        item = germania.token_plain(ngram)
        result.append(item)
    return result


def three_gram(words) -> str:
    result = []
    ngrams = germania.ngram(words, length=3)
    for ngram in ngrams:
        minus = ngram[1] == konradus.Mark.HYPHEN
        if not minus:
            continue
        ngram = list(ngram)
        try:
            ngram[0] = germania.word_normalize(ngram[0]).lower()
            ngram[2] = germania.word_normalize(ngram[2]).lower()
        except TypeError:
            continue
        item = germania.token_plain(ngram)
        result.append(item)
    return result


def create_pattern_five(fives) -> tuple:
    fives = [item[0] for item in fives]
    result = []
    for five in fives:
        five = germania.word_tokenize(five, validate_sentences=False)
        result.append(tuple(five[:1] + five[2:]))
        result.append(tuple(five[0:3] + five[4:]))
        result.append((five[0], five[2], five[4]))
    result: tuple = tuple(utilo.unique(result))
    return result


def create_pattern_three(three) -> tuple:
    return tuple(tuple(item[0].split('-')) for item in three)

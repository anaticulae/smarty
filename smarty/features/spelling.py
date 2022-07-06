# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import typing

import iamraw
import serializeraw
import utila

import smarty.pair.guess
import smarty.pair.minus


def work(
    sentences: str,
    pages: tuple = None,
) -> typing.Tuple[str, str]:
    sentences = serializeraw.load_text(
        sentences,
        pages=pages,
    )
    missing = smarty.pair.minus.missing(sentences)
    guesses = smarty.pair.guess.guess(sentences)
    detected_missing = convert(missing)
    detected_guesses = convert(guesses)
    dumped_missing = serializeraw.dump_textadvices(detected_missing)
    dumped_guesses = serializeraw.dump_textadvices(detected_guesses)
    return dumped_missing, dumped_guesses


def convert(failures) -> list:
    # ensure that 2,3,4,5 and five grams are sorted in result correctly.
    failures = sorted(failures, key=lambda x: x.token[0])
    failures.sort(key=lambda x: x.sentence)
    failures.sort(key=lambda x: x.page)
    result = []
    paged = utila.groupby_x(failures, selector=lambda x: x.page)
    for page in paged:
        sentenced = utila.groupby_x(page, selector=lambda x: x.sentence)
        for group in sentenced:
            page, sentence = group[0].page, group[0].sentence
            tokens = [item.token for item in group]
            raws = [item.raw for item in group]
            advice = iamraw.TextAdvice(docref=iamraw.DocRef(
                page=page,
                sentence=sentence,
                marked=tokens,
                raw=raws,
            ))
            result.append(advice)
    return result

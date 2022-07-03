# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import serializeraw
import utila

import smarty.pair.minus


def work(
    sentences: str,
    pages: tuple = None,
) -> str:
    sentences = serializeraw.load_text(
        sentences,
        pages=pages,
    )
    missing = smarty.pair.minus.missing(sentences)
    detected = convert(missing)
    dumped = serializeraw.dump_textadvices(detected)
    return dumped


def convert(failures) -> list:
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

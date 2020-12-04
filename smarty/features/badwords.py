# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools
import typing

import serializeraw
import utila

import smarty.badwords.phrases


def work(
        text: str,
        headlines: str,
        pages: tuple = None,
) -> typing.Tuple[str, str, str]:
    headlines = serializeraw.load_headlines(headlines, pages=pages)
    text = serializeraw.load_text(text, headlines=headlines, pages=pages)

    phrases = functools.partial(smarty.badwords.phrases.phrases_fromtext, text)
    pleonasmen = functools.partial(
        smarty.badwords.pleonasmen.pleonasmen_fromtext,
        text,
    )
    prefix = functools.partial(
        smarty.badwords.prefix.prefix_not_required_fromtext,
        text,
    )
    # run parallel
    done = utila.fork(phrases, pleonasmen, prefix)
    # dump results
    dumped = [smarty.serialize.dump_phrases(item) for item in done]
    return dumped

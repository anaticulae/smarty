# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import serializeraw

import smarty.badwords.pleonasmen


def work(
    sentences: str,
    pages: tuple = None,
) -> str:
    sentences = serializeraw.load_text(sentences, pages=pages)
    detected = smarty.badwords.pleonasmen.pleonasmen_fromtext(sentences)
    dumped = serializeraw.dump_textadvices(detected)
    return dumped

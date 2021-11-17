# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""Improvement
===========

The Improvement detector detects a group of words and give an
replacement to the user.
There can be a optional description why this improvement is required.
"""

import iamraw
import utila

import smarty.utils

# yapf:disable
IMPROVEMENT = smarty.utils.init_table("""\
dynamische Wandlung                 Wandel                              Ist ein statischer Wandel möglich?
höchste exaktheit                   höchste Genauigkeit                 Exaktheit ist nicht steigerbar. Es ist entweder exakt oder nicht.
standart                            Standard                            Meinen Sie wirklich die Art zu stehen?
weltweite globalisierung            Globalisierung                      Global umfasst die ganze Welt.
""", columns=3)
# yapf:enable


class Improvement(smarty.badwords.FromText):

    def __init__(self):
        super().__init__(tokens=IMPROVEMENT)

    def advice(self, docref, raw):
        improvement = self.tokens.get(raw)
        try:
            replacement, hint = improvement
        except TypeError:
            replacement, hint = improvement, ''
        result = iamraw.TextAdviceReplacement(
            docref=docref,
            raw=raw,
            replacement=replacement,
            hint=hint,
        )
        return result


PROCESS = Improvement()


@utila.cacheme
def improvement_search(sentence: str):
    return PROCESS.search(sentence)


def improvement_fromtext(sentences) -> iamraw.TextAdviceReplacement:
    return PROCESS.callme(sentences)

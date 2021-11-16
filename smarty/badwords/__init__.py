# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import german
import iamraw
import utila

import smarty.utils


class FromText:

    def __init__(self, tokens, neighbours_merge: bool = True):
        self.tokens = tokens
        self.neighbours_merge = neighbours_merge

    def callme(self, sentences):
        result = []
        for page, number, sentence in smarty.utils.sentences(
                sentences,
                numbers=True,
        ):
            detected = self.search(sentence)
            if not detected:
                continue
            marked, raw = detected
            raw = self.rawme(raw)
            docref = iamraw.DocRef(
                page=page,
                sentence=number,
                marked=marked,
            )
            item = self.advice(docref=docref, raw=raw)
            result.append(item)
        return result

    @utila.cacheme
    def search(self, sentence):
        matched = german.searches(
            tokenslist=self.tokens,
            sentence=sentence,
            tokens_complex=False,
            neighbours_merge=self.neighbours_merge,
            verbose=True,
        )
        return matched

    def advice(self, docref, raw):  # pylint:disable=R0201
        result = iamraw.TextAdviceDelete(
            docref=docref,
            raw=raw,
        )
        return result

    def rawme(self, raw):  # pylint:disable=R0201
        return ', '.join([' '.join(item) for item in raw])

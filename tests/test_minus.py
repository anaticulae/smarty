# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power

import smarty.pair.minus
import tests


def test_minus_grams_bachelor077():
    source = power.BACHELOR077_PDF
    sentences = tests.load_text(source)
    threes, fives = smarty.pair.minus.grams(sentences)
    assert threes, fives


def test_minus_missing_bachelor077():
    source = power.BACHELOR077_PDF
    sentences = tests.load_text(source)
    missing = smarty.pair.minus.missing(sentences)
    assert len(missing) >= 58

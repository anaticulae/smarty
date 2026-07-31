# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import hoverpower
import serializeraw
import utilotest

import smarty.pair.minus
import smarty.path
import tests


@utilotest.requires(hoverpower.BACHELOR077_PDF)
def test_minus_grams_bachelor077():
    source = hoverpower.BACHELOR077_PDF
    sentences = tests.load_text(source)
    threes, fives = smarty.pair.minus.grams(sentences)
    assert threes, fives


@utilotest.requires(hoverpower.BACHELOR077_PDF)
def test_minus_missing_bachelor077():
    source = hoverpower.BACHELOR077_PDF
    sentences = tests.load_text(source)
    missing = smarty.pair.minus.missing(sentences)
    assert len(missing) >= 56


@utilotest.requires(hoverpower.BACHELOR077_PDF)
def test_cli_spelling_hyphen(td, mp):
    source = hoverpower.link(hoverpower.BACHELOR077_PDF)
    tests.run(f'-i {source} --spelling', mp=mp)
    path = smarty.path.smarty_spelling_hyphen(td.tmpdir)
    loaded = serializeraw.load_textadvices(path)
    assert loaded
    assert len(loaded) >= 54

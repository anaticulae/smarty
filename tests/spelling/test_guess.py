# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import serializeraw
import utilatest

import smarty.path
import tests


@utilatest.requires(power.BACHELOR077_PDF)
def test_cli_spelling_guess(testdir, monkeypatch):
    source = power.link(power.BACHELOR077_PDF)
    tests.run(f'-i {source} --spelling', monkeypatch=monkeypatch)
    path = smarty.path.smarty_spelling_guess(testdir.tmpdir)
    loaded = serializeraw.load_textadvices(path)
    assert loaded
    assert len(loaded) >= 58

# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import pytest
import utilatest

import smarty.path
import smarty.serialize
import tests


def test_help(monkeypatch):
    tests.run('--help', monkeypatch=monkeypatch)


@pytest.mark.parametrize('source', [
    pytest.param(power.MASTER110_PDF, id='master110'),
    pytest.param(power.BACHELOR128_PDF, id='bachelor128'),
])
@utilatest.longrun
def test_cli_badwords(source, testdir, monkeypatch):
    source = power.link(source)
    tests.run(f'-i {source} --badwords', monkeypatch=monkeypatch)
    path = smarty.path.smarty_phrases(testdir.tmpdir)
    loaded = smarty.serialize.load_phrases(path)
    assert loaded

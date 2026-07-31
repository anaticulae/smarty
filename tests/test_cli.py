# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import hoverpower
import pytest
import serializeraw
import utilotest

import smarty.path
import tests


def test_help(mp):
    tests.run('--help', mp=mp)


@pytest.mark.parametrize('source', [
    pytest.param(hoverpower.MASTER110_PDF, id='master110'),
    pytest.param(hoverpower.BACHELOR128_PDF, id='bachelor128'),
])
@utilotest.nightly
def test_cli_badwords(source, td, mp):
    utilotest.fixture_requires(source)
    source = hoverpower.link(source)
    tests.run(f'-i {source}', mp=mp)
    path = smarty.path.smarty_phrases(td.tmpdir)
    loaded = serializeraw.load_textadvices(path)
    assert loaded

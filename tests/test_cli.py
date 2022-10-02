# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import pytest
import serializeraw
import utilatest

import smarty.path
import tests


def test_help(mp):
    tests.run('--help', mp=mp)


@pytest.mark.parametrize('source', [
    pytest.param(power.MASTER110_PDF, id='master110'),
    pytest.param(power.BACHELOR128_PDF, id='bachelor128'),
])
@utilatest.nightly
def test_cli_badwords(source, td, mp):
    utilatest.fixture_requires(source)
    source = power.link(source)
    tests.run(f'-i {source}', mp=mp)
    path = smarty.path.smarty_phrases(td.tmpdir)
    loaded = serializeraw.load_textadvices(path)
    assert loaded

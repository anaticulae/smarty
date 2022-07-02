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
import utila

import smarty
import tests


def test_count_words():
    source = power.MASTER072_PDF
    text = tests.load_text(source)
    result = smarty.count_words(text)
    assert len(result) >= 3000


def test_count_questions():
    source = power.MASTER072_PDF
    text = tests.load_text(source)
    result = smarty.count_questions(text)
    assert result >= 5  # not validated yet


@pytest.mark.parametrize('source, expected', [
    pytest.param(power.MASTER072_PDF, 0.007, id='master72'),
    pytest.param(power.BACHELOR128_PDF, 0.023, id='bachelor128'),
    pytest.param(power.BACHELOR090_PDF, 0.0, id='bachelor90'),
    pytest.param(power.MASTER099_PDF, 0.013, id='master99'),
])
def test_ratio_questions_fromtext(source, expected):
    text = tests.load_text(source)
    ratio = smarty.ratio_questions_fromtext(text)
    assert utila.near(ratio, expected, diff=0.01), str(ratio)

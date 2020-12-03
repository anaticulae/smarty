# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power

import smarty
import tests


def test_count_words():
    source = power.MASTER072_PDF
    text = tests.load_text(source)
    result = smarty.count_words(text)
    assert len(result) >= 3000

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


def test_phrases_fromtext_bachelor128():
    source = power.BACHELOR128_PDF
    text = tests.load_text(source)

    detected = smarty.phrases_fromtext(text)
    assert len(detected) >= 9

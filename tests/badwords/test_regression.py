# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power

import smarty
import tests


def test_bachelor111page26_mark_converter():
    """Mark converter produces an error."""
    text = tests.load_text(power.BACHELOR111_PDF, pages=(26,))
    detected = smarty.pleonasmen_fromtext(text)
    assert len(detected) == 1

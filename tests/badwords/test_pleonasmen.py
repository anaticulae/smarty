# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import hoverpower
import utilotest

import smarty
import tests


@utilotest.longrun
def test_pleonasmen_fromtext_bachelor128():
    text = tests.load_text(hoverpower.BACHELOR128_PDF)
    detected = smarty.pleonasmen_fromtext(text)
    assert len(detected) >= 2

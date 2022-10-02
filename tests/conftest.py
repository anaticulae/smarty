# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import genex
import power
import pytest
from utilatest import mp  # pylint:disable=W0611
from utilatest import td  # pylint:disable=W0611

import smarty

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

PACKAGE = smarty.PROCESS

power.setup(smarty.ROOT)

RESOURCES = [
    (power.BACHELOR111_PDF, '0:30'),
    power.BACHELOR077_PDF,
    power.BACHELOR090_PDF,
    power.BACHELOR128_PDF,
    power.MASTER072_PDF,
    power.MASTER099_PDF,
    power.MASTER110_PDF,
]

WORKER = 4


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    power.run()


def extract(resources):
    genex.extract(
        files=resources,
        caption=True,
        cleanup=True,
        codero=True,
        figureo=True,
        formulero=True,
        groupme=True,
        pagenumber=True,
        headnote=True,
        footnote=True,
        headlines=True,
        lists=True,
        magic=True,
        sections=True,
        tablero=True,
        words=True,
        worker=WORKER,
    )

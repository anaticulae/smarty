# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import gennex
import hoverpower
import pytest
import utilotest
from utilotest import mp  # pylint:disable=W0611
from utilotest import td  # pylint:disable=W0611

import smarty

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

PACKAGE = smarty.PROCESS

hoverpower.setup(smarty.ROOT)

RESOURCES = [
    (hoverpower.BACHELOR111_PDF, '0:30'),
    hoverpower.BACHELOR077_PDF,
    hoverpower.BACHELOR090_PDF,
    hoverpower.BACHELOR128_PDF,
    hoverpower.MASTER072_PDF,
    hoverpower.MASTER099_PDF,
    hoverpower.MASTER110_PDF,
]

WORKER = utilotest.worker_count(4, onci=len(RESOURCES))


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    hoverpower.run()


def extract(resources):
    gennex.extract(
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

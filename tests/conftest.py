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
import utila

import smarty

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

PACKAGE = smarty.PACKAGE

power.setup(smarty.ROOT)

RESOURCES = [
    power.BACHELOR090_PDF,
    power.BACHELOR128_PDF,
    power.MASTER072_PDF,
    power.MASTER099_PDF,
    power.MASTER110_PDF,
    (power.BACHELOR111_PDF, '20:30'),
]

WORKER = 4


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    power.run()


def extract(resources):
    # ensure to handle single file generation or common resource subfolder
    # correctly. To determine the output path it is required to determine
    # the parent path of at least two files. If resources provide only a
    # single file the parental determination is not possible. Therefore we
    # have to add the data root of all test files.
    utila.log(f'root: {power.REPOSITORY}')
    genex.extract(
        files=resources,
        destination=power.generated(),
        groupme=True,
        sections=True,
        words=True,
        magic=True,
        worker=WORKER,
        pages=':',
        base=power.REPOSITORY,
    )

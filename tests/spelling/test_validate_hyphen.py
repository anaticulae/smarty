# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools

import germania
import hoverpower
import pytest
import serializeraw
import utilo
import utilotest

import smarty
import tests
import tests.conftest

ARCHIVE = utilo.join(smarty.ROOT, 'tests/spelling/expected_hyphen', exist=True)


@pytest.mark.parametrize(
    'source',
    utilotest.test_resources(tests.conftest.RESOURCES),
)
@utilotest.nightly
def test_validate_spelling_hyphen(source, td, mp):
    Evaluate(
        source=source,
        workdir=td.tmpdir,
        mp=mp,
    ).evaluate()


class Evaluate(utilotest.BaseLiner):

    def __init__(self, source, workdir, mp):
        super().__init__(
            program=functools.partial(
                tests.run,
                mp=mp,
            ),
            step='spelling',
            pages=hoverpower.ctext(source, default=':'),
            source=hoverpower.link(source),
            workdir=workdir,
            archive=ARCHIVE,
            loader=self.frompath,
            convert_source=False,
        )

    def frompath(self, path):  # pylint:disable=R0201
        path = smarty.path.smarty_spelling_hyphen(path)
        loaded = serializeraw.load_textadvices(path)
        return loaded

    def raw(self, value) -> str:
        result = [rawline(item) for item in value]
        result: str = utilo.NEWLINE.join(result)
        return result


def rawline(item) -> str:
    result = str(item.docref.page).zfill(3) + ' '
    result += str(item.docref.sentence).zfill(2) + ' '
    result += ',     '.join(germania.token_plain(item) for item in item.docref.raw) + ' '  # yapf:disable
    result += ' ' * (85 - len(result))
    result += ' '.join(str(item) for item in item.docref.marked)
    return result

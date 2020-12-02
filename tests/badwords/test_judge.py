# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import german
import power
import pytest
import serializeraw
import utila
import words.path
import words.utils

import smarty

TEXT = german.split_words("""Die Registrierung und Protokollierung
sollte jedoch nicht allzu verzögert erfolgen, um ein möglichst genaues
Ergebnis der Dokumentation zu erhalten.""")


def test_badword_judge():
    judged = smarty.badwords_judge(TEXT, skip_empty=True)
    assert len(judged) == 3


def test_badword_ratio_fat():
    text = [item for item in TEXT if isinstance(item, str)]
    ratio = smarty.ratio_fat(text)
    assert ratio == utila.roundme(3 / len(text))


@pytest.mark.parametrize('source, expected', [
    pytest.param(power.BACHELOR090_PDF, 0.01, id='bachelor90'),
    pytest.param(power.BACHELOR128_PDF, 0.04, id='bachelor128'),
    pytest.param(power.MASTER072_PDF, 0.05, id='master72'),
    pytest.param(power.MASTER099_PDF, 0.02, id='master99'),
    pytest.param(power.MASTER110_PDF, 0.02, id='master110'),
])
def test_document_ratio_fat(source, expected):
    source = power.link(source)
    headlines = words.path.headlines(source)
    headlines = serializeraw.load_headlines(headlines)
    text = words.path.text(source)
    text = serializeraw.load_text(text, headlines=headlines)
    ratio = smarty.ratio_fat_fromtext(text)
    assert utila.near(ratio, expected, diff=0.01), ratio

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
    ratio = smarty.ratio_fat(TEXT)
    assert ratio == utila.roundme(3 / len(TEXT))


def test_master72_ratio_fat():
    source = power.link(power.MASTER072_PDF)
    headlines = words.path.headlines(source)
    headlines = serializeraw.load_headlines(headlines)
    text = words.path.text(source)
    text = serializeraw.load_text(text, headlines=headlines)

    ratio = smarty.ratio_fat_fromtext(text)
    assert utila.near(ratio, 0.04, diff=0.01), ratio

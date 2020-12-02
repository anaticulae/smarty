# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import german
import utila

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

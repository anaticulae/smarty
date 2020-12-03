# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import german
import words.utils

import smarty.utils

NEGATIVE = """\
Blickfeld der Öffentlichkeit
Ideen gesät
Schreckgespenst betrachtet
auf den Punkt gebracht
bereits heute
breites Spektrum
eine immense Zahl
etwas Positives abzugewinnen
etwas abschauen
fruchtbarer Boden
ihnen herrscht
im Stich gelassen
in aller Munde
knapp bemessen
löst Angst und Schrecken aus
macht es Sinn
man kann nur Mutmaßungen anstellen
soziale Kitt
unermesslichen Breite
war durchaus positiv
werden wir auf eine Katastrophe zusteuern
zu entzaubern
äußerst wichtig
öffentlichen Hand
"""
NEGATIVE = smarty.utils.init(NEGATIVE)


def phrases_search(sentence: str):
    matched = german.searches(
        tokenslist=NEGATIVE,
        sentence=sentence,
        tokens_complex=False,
    )
    return matched


def phrases_fromtext(text):
    result = []
    for page, number, sentence in words.utils.sentences(text, numbers=True):
        detected = phrases_search(sentence)
        if not detected:
            continue
        result.append((page, number, detected))
    return result

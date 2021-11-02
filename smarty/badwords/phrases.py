# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import german

import smarty.serialize
import smarty.utils

NEGATIVE = """\
Arbeitswelt
Blickfeld der Öffentlichkeit
Gesamtpaket
Ideen gesät
Leben lassen mussten
Schlüsselfrage
Schreckgespenst betrachtet
auf den Punkt gebracht
bereits heute
beschleunigten Alltagskultur
breites Spektrum
eine immense Zahl
eine wichtige Rolle
einige aufgeführt
enorm
erschreckende Schlagzeilen
erschütternde Zahlen
es spielen
etwas Positives abzugewinnen
etwas abschauen
fruchtbarer Boden
gewinnt im Zuge
heutige Arbeitswelt
heutige Lebenswelt
heutigen Zeit
häufig Mangelware
ihnen herrscht
ihr Leben lassen mussten
im Stich gelassen
immer wieder aufs Neue
in aller Munde
jeder hat schon einmal
knapp bemessen
kostbares Gut
kurz erwähnt
löst Angst und Schrecken aus
macht es Sinn
man kann nur Mutmaßungen anstellen
nicht unerwähnt
nicht unerwähnt bleiben
schwerwiegende Erkenntnis
sehr wichtiger Faktor
solides Grundwissen
soll nicht unerwähnt bleiben
soziale Kitt
spielt im Bereich
umfangreiche Quellen
unermesslichen Breite
war durchaus positiv
werden wir auf eine Katastrophe zusteuern
zu entzaubern
ältesten Disziplinen
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


def phrases_fromtext(text) -> smarty.serialize.Phrases:
    result = []
    for page, number, sentence in smarty.utils.sentences(text, numbers=True):
        detected = phrases_search(sentence)
        if not detected:
            continue
        result.append(
            smarty.serialize.Phrase(
                page=page,
                sentence=number,
                marked=detected,
            ))
    return result

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
arbeitswelt
auf den punkt gebracht
bereits heute
beschleunigten alltagskultur
blickfeld der öffentlichkeit
breites spektrum
eine immense zahl
eine wichtige rolle
einige aufgeführt
enorm
erschreckende schlagzeilen
erschütternde zahlen
es spielen
etwas abschauen
etwas positives abzugewinnen
fruchtbarer boden
gesamtpaket
gewinnt im zuge
heutige arbeitswelt
heutige lebenswelt
heutigen zeit
häufig mangelware
ideen gesät
ihnen herrscht
ihr leben lassen mussten
im stich gelassen
immer wieder aufs neue
in aller munde
jeder hat schon einmal
knapp bemessen
kostbares gut
kurz erwähnt
leben lassen mussten
löst angst und schrecken aus
macht es sinn
man kann nur mutmaßungen anstellen
nicht unerwähnt
nicht unerwähnt bleiben
schlüsselfrage
schreckgespenst betrachtet
schwerwiegende erkenntnis
sehr wichtiger faktor
solides grundwissen
soll nicht unerwähnt bleiben
soziale kitt
spielt im bereich
umfangreiche quellen
unermesslichen breite
war durchaus positiv
werden wir auf eine katastrophe zusteuern
zu entzaubern
ältesten disziplinen
äußerst wichtig
öffentlichen hand
"""
NEGATIVE = smarty.utils.init(NEGATIVE)


def phrases_search(sentence: str):
    matched = german.searches(
        tokenslist=NEGATIVE,
        sentence=sentence,
        tokens_complex=False,
    )
    return matched


def phrases_fromtext(sentences) -> smarty.serialize.Phrases:
    result = []
    for page, number, sentence in smarty.utils.sentences(
            sentences,
            numbers=True,
    ):
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

# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import utila

import smarty.badwords
import smarty.serialize
import smarty.utils

NEGATIVE = utila.splitlines("""\
alles in allem
am puls der zeit
arbeitswelt
auf den punkt gebracht
bereits heute
beschleunigten alltagskultur
bitterer ernst
blickfeld der öffentlichkeit
breites spektrum
das bittere ende
die breite masse
die goldene mitte
eine immense zahl
eine wichtige rolle
einer ausgiebigen betrachtung
einige aufgeführt
enorm
erschreckende schlagzeilen
erschütternde zahlen
es spielen
etwas abschauen
etwas positives abzugewinnen
findet seine einschätzung widerklang
findet widerklang
fruchtbarer boden
gesamtpaket
gewinnt im zuge
grünes licht
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
in die höhe schießen
in irgendeiner weise
jeder hat schon einmal
knapp bemessen
kostbares gut
kurz erwähnt
kurz umrissen werden
kurz und knapp
leben lassen mussten
löst angst und schrecken aus
macht es sinn
man kann nur mutmaßungen anstellen
nadel im heuhaufen
nicht unerwähnt
nicht unerwähnt bleiben
schlüsselfrage
schreckgespenst betrachtet
schwerwiegende erkenntnis
sehr wichtiger faktor
sieht jedenfalls anders aus
solides grundwissen
soll nicht unerwähnt bleiben
soziale kitt
spielt im bereich
spitze des eisbergs
stößt man
suboptimal
umfangreiche quellen
unermesslichen breite
verdacht erhärtet sich
verschwimmt immer mehr
war durchaus positiv
werden wir auf eine katastrophe zusteuern
zu entzaubern
ältesten disziplinen
äußerst wichtig
öffentlichen hand
""")
PROCESS = smarty.badwords.FromText(tokens=NEGATIVE)


@utila.cacheme
def phrases_search(sentence: str):
    return PROCESS.search(sentence)


def phrases_fromtext(sentences) -> iamraw.TextAdviceDelete:
    return PROCESS.callme(sentences)

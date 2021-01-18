# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import german
import words.utils

import smarty.serialize
import smarty.utils

ABBREVIATION = """\
ABM-Maßnahme
ABS-System
ASCII-Code
GIF-Format
GUS-Staaten
HIV-Virus
IP-Protokoll
ISBN-Nummer
ISDN-Netz
LCD-Anzeige
LCD-Screen
PIN-Nummer
RAM-Speicher
SMS-Dienst
"""
ABBREVIATION = smarty.utils.init(ABBREVIATION)

DUPLICATED = """\
angeblich sollen
auseinanderdividieren
durchkalkulieren
herausselektieren
hochstilisieren
in der Mitte halbieren
möglich sein können
nachrecherchieren
reinvestieren
runterreduzieren
wahrscheinlich scheinen
zusammenaddieren
"""
DUPLICATED = smarty.utils.init(DUPLICATED)

NOUN = """\
Attentatsversuch
Ausgangsvoraussetzungen
Auslandsexport
Außenfassade
Düsenjet
Einzelindividuum
Endergebnis
Freitextfeld
Frontlinie
Frühpionier
Fußpedal
Gehbewegung
Gesichtsmimik
Gesprächsaustausch
Glasvitrine
Gratisgeschenk
Grundkonzept
Grundprinzip
Haarfrisur
Heizkamin
Heizofen
Kampfhandlung
Mitbeteiligung
Mitkollegen
Mitkonkurrenten
Musikband
Niederschlagstätigkeit
Pulsschlag
Restrisiko
Rückantwort
Rückerinnerung
Rückerstattung
Rückstau
Standdüne
Subkomponente
Testversuch
Verkehrsaufkommen
Volksdemokratie
Vorderfront
Vorermittlungen
Zukunftsperspektiven
Zukunftspläne
Zukunftsprognosen
Zwangsexekution
der Einzigste
"""
NOUN = smarty.utils.init(NOUN)

WORDHULL = """\
Bankenbereich
Bankenkreis
Bankensektor
Erfahrungsraum
Erziehungsbereich
F&E-Bereich
Industriebereich
Problemkreis
Themenbereich
Unternehmensbereich
Unternehmenskreis
Werbebereich
Wirtschaftsbereich
Wirtschaftskreis
erzieherischer Bereich
im Bereich der Werbung
im Bereich der Wirtschaft
kommunaler Sektor
landwirtschaftlicher Sektor
politischer Raum
sprachlicher Bereich
technischer Bereich
unternehmerischer Bereich
wissenschaftlichen Disziplinen
wissenschaftlicher Bereich
"""
WORDHULL = smarty.utils.init(WORDHULL)


def pleonasmen_search(sentence: str):
    matched = german.searches(
        tokenslist=ABBREVIATION | DUPLICATED | NOUN | WORDHULL,
        sentence=sentence,
        tokens_complex=False,
    )
    return matched


def pleonasmen_fromtext(text) -> smarty.serialize.Phrases:
    result = []
    for page, number, sentence in words.utils.sentences(text, numbers=True):
        detected = pleonasmen_search(sentence)
        if not detected:
            continue
        result.append(
            smarty.serialize.Phrase(
                page=page,
                sentence=number,
                marked=detected,
            ))
    return result

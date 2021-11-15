# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import german
import utila

import smarty.serialize
import smarty.utils

ABBREVIATION = """\
abm-maßnahme                        arbeitsbeschaffungsmaßnahme
abs-system                          anti-blockier-system
ascii-code                          amarican standard code of information exchange
gif-format
gus-staaten
hiv-virus
ip-protokoll
isbn-nummer                         internation standard book number
isdn-netz
lcd-anzeige                         liquid cristal display
lcd-screen                          liquid cristal display
pin-nummer                          persönliche indentifikations nummber
ram-speicher                        random access memory
sms-dienst                          short message service
"""
ABBREVIATION = smarty.utils.init(ABBREVIATION)

DUPLICATED = """\
angeblich sollen                    sollen
auseinanderdividieren
durchkalkulieren                    kalkulieren
herausselektieren                   selektieren
hochstilisieren                     stilisieren
in der mitte halbieren              halbieren
möglich sein können                 sein können
nachrecherchieren                   recharchieren
reinvestieren                       investieren
runterreduzieren                    reduzieren
wahrscheinlich scheinen             scheinen
zusammenaddieren                    addieren
"""
DUPLICATED = smarty.utils.init(DUPLICATED)

NOUN = smarty.utils.init("""\
attentatsversuch                    attentat
ausgangsvoraussetzungen             voraussetzung
auslandsexport                      export
außenfassade                        fassade
der einzigste
düsenjet                            jet
einzelindividuum                    individuum
endergebnis                         ergebnis
freitextfeld                        textfeld
frontlinie                          front
frühpionier                         pionier
fußpedal                            pedal
gehbewegung
gesichtsmimik
gesprächsaustausch
glasvitrine
gratisgeschenk
grundkonzept
grundprinzip
haarfrisur
heizkamin
heizofen
kampfhandlung
mitbeteiligung
mitkollegen
mitkonkurrenten
musikband
niederschlagstätigkeit
pulsschlag
restrisiko
rückantwort
rückerinnerung
rückerstattung
rückstau
standdüne
subkomponente
testversuch
verkehrsaufkommen
volksdemokratie
vorderfront
vorermittlungen
zukunftsperspektiven
zukunftspläne
zukunftsprognosen
zwangsexekution
""")

WORDHULL = utila.splitlines("""\
bankenbereich
bankenkreis
bankensektor
erfahrungsraum
erzieherischer bereich
erziehungsbereich
f&e-bereich
im bereich der werbung
im bereich der wirtschaft
industriebereich
kommunaler sektor
landwirtschaftlicher sektor
politischer raum
problemkreis
sprachlicher bereich
technischer bereich
themenbereich
unternehmensbereich
unternehmenskreis
unternehmerischer bereich
werbebereich
wirtschaftsbereich
wirtschaftskreis
wissenschaftlichen disziplinen
wissenschaftlicher bereich
""")


def pleonasmen_search(sentence: str):
    matched = german.searches(
        tokenslist=ABBREVIATION | DUPLICATED | NOUN | WORDHULL,
        sentence=sentence,
        tokens_complex=False,
    )
    return matched


def pleonasmen_fromtext(sentences) -> smarty.serialize.Phrases:
    result = []
    for page, number, sentence in smarty.utils.sentences(
            sentences,
            numbers=True,
    ):
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

# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import utila

import smarty.badwords
import smarty.serialize
import smarty.utils

ABBREVIATION = smarty.utils.init_table("""\
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
""")

DUPLICATED = smarty.utils.init_table("""\
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
""")

NOUN = smarty.utils.init_table("""\
attentatsversuch                    attentat
ausgangsvoraussetzungen             voraussetzung
auslandsexport                      export
außenfassade                        fassade
der einzigste                       einzige
düsenjet                            jet
einzelindividuum                    individuum
endergebnis                         ergebnis
freitextfeld                        textfeld
frontlinie                          front
frühpionier                         pionier
fußpedal                            pedal
gehbewegung                         bewegung
gesichtsmimik                       mimik
gesprächsaustausch                  gespräch
glasvitrine                         vitrine
gratisgeschenk                      geschenk
grundkonzept                        konzept
grundprinzip                        prinzip
haarfrisur                          frisur
heizkamin                           kamin
heizofen                            ofen
kampfhandlung                       kampf
mitbeteiligung                      beteiligung
mitkollegen                         kollegen
mitkonkurrenten                     konkurrenten
musikband                           band
niederschlagstätigkeit              niederschlag
pulsschlag                          puls
restrisiko                          risiko
rückantwort                         antwort
rückerinnerung                      erinnerung
rückerstattung                      erstattung
rückstau                            stau
standdüne                           düne
subkomponente                       komponente
testversuch                         versuch oder test
verkehrsaufkommen                   verkehr
volksdemokratie                     demokratie
vorderfront                         front
vorermittlungen                     ermittlungen
zukunftsperspektiven                perspektiven
zukunftspläne                       pläne
zukunftsprognosen                   prognose
zwangsexekution                     exekution
""")

WORDHULL = smarty.utils.init_table("""\
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
sicherheitsrelevanten bereichen
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


class Pleonasma(smarty.badwords.FromText):

    def __init__(self):
        super().__init__(tokens=ABBREVIATION | DUPLICATED | NOUN | WORDHULL)
        self.lookup = utila.dicts_united(
            ABBREVIATION,
            DUPLICATED,
            NOUN,
            WORDHULL,
        )

    def advice(self, docref, raw):
        replacement = self.lookup.get(raw, 'NO ADVICE')
        result = iamraw.TextAdviceReplacement(
            docref=docref,
            raw=raw,
            replacement=replacement,
        )
        return result


PROCESS = Pleonasma()


@utila.cacheme
def pleonasmen_search(sentence: str):
    return PROCESS.search(sentence)


def pleonasmen_fromtext(sentences) -> iamraw.TextAdviceReplacement:
    return PROCESS.callme(sentences)

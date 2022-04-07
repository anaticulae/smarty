# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""Improvement
===========

The Improvement detector detects a group of words and give an
replacement to the user.
There can be a optional description why this improvement is required.
"""

import iamraw
import utila

import smarty.badwords
import smarty.utils

# yapf:disable
IMPROVEMENT = smarty.utils.init_table("""\
# Lichtzeichenanlage                Ampel
# literarisches Werk                Buch
ansonsten                           sonst
ausgestalltung                      Gestalltung
beantwortung                        Antwort
dynamischer Wandel                  groß/schnell/stark Wandel                   Wandel ist nie statisch.
dynamische Wandlung                 Wandel                                      Ist ein statischer Wandel möglich?
eine Vielzahl von                   viele
grundbefindlichkeit                 Zustand
hohe Abhängigkeit                   starke Abhängigkeit
hohe Bereitschaft                   große Bereitschaft
hohe Kenntnisse                     fundierte/umfangreiche Kenntnisse
hohe Marktdynamik                   dynamischer Markt
hohe Neigung                        starke Neigung
hohe Nutzung                        intensive Nutzung
hohe Wirkung                        intensive/starke Wirkung
hoher Aufwand                       großer Aufwand
hoher Spielraum                     großer/weiter Spielraum
hoher Zeitaufwand                   großer Zeitaufwand
hohes Bedürfnis                     ausgepgrägtes/starkes Bedürfnis
hohes Marktpotential                erfolgsversprechendes/großes Marktpotential
hohes Risiko                        großes Risiko
hohes Volumen                       großes Volumen
höchste exaktheit                   höchste Genauigkeit                         Exaktheit ist nicht steigerbar. Es ist entweder exakt oder nicht.
in Zusammenhang mit                 bei
in ihrer Gesamtheit                 alle
in vollem Umfang                    ganz
keine Seltenheit                    häufig
kritische Anmerkungen               Kritik
positive Entwicklung                Steigerung
postwertzeichen                     Briefmarke
problematik                         Problem
problemlösungsaktivitäten           Problem lösen
räumlichkeit                        Raum
standart                            Standard                                    Meinen Sie wirklich die Art zu stehen?
strengstes Stillschweigen           schweigen
thematik                            Thema
themenkomplex                       Thema
weltweite globalisierung            Globalisierung                              Global umfasst die ganze Welt.
zielsetzung                         Ziel
zielstellung                        Ziel
zu einem späteren Zeitpunkt         später
zum wiederholten Male               wieder
zwischenfazit                       zwischenstand
""", columns=3)
# yapf:enable


class Improvement(smarty.badwords.FromText):

    def __init__(self):
        super().__init__(tokens=IMPROVEMENT)

    def advice(self, docref, raw):
        improvement = self.fromtable(raw)
        try:
            replacement, hint = improvement
        except (TypeError, ValueError):
            replacement, hint = improvement, ''
        result = iamraw.TextAdviceReplacement(
            docref=docref,
            raw=raw,
            replacement=replacement,
            hint=hint,
        )
        return result


PROCESS = Improvement()


@utila.cacheme
def improvement_search(sentence: str):
    return PROCESS.search(sentence)


def improvement_fromtext(sentences) -> iamraw.TextAdviceReplacement:
    return PROCESS.callme(sentences)

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
import smarty.utils

NOT_REQUIRED = smarty.utils.init_table("""\
abblocken                       blocken
abklären                        klären
abmildern                       mildern
abprüfen                        prüfen
absegnen                        sengen
absenken                        senken
absichern                       sichern
absinken                        sinken
abstoppen                       stoppen
abstützen                       stützen
abtesten                        testen
abzielen                        zielen
anbetreffen                     betreffen
anheben                         heben
ankaufen                        kaufen
anschwellen                     schwellen
ansteigen                       steigen
anwachsen                       wachsen
aufaddieren                     addieren
auffülllen                      füllen
auflisten                       listen
aufoktroyieren                  oktroyieren
aufspalten                      spalten
aufsummieren                    summieren
aufzeigen                       zeigen
ausborgen                       borgen
auseinanderklaffen              klaffen
ausleihen                       leihen
befüllen                        füllen
hochskalieren                   skalieren
losstarten                      starten
mit einbeziehen                 einbeziehen/einschließen
mit einschließen                einschließen
mithelfen                       helfen
verbuchen                       buchen
verfüllen                       füllen
vorankommen
vorwarnen                       warnen
weglöschen                      löschen
zuliefern                       liefen
zuschicken                      schicken
überprüfen                      prüfen
""")


class RemovePrefix(smarty.badwords.FromText):

    def __init__(self, tokens=NOT_REQUIRED):
        super().__init__(tokens=tokens)
        self.lookup = tokens

    def advice(self, docref, raw):
        replacement = self.lookup.get(raw, 'NO ADVICE')
        result = iamraw.TextAdviceReplacement(
            docref=docref,
            raw=raw,
            replacement=replacement,
        )
        return result


PROCESS = RemovePrefix()


@utila.cacheme
def prefix_not_required_search(sentence: str) -> list:
    return PROCESS.search(sentence)


def prefix_not_required_fromtext(sentences) -> iamraw.TextAdviceReplacement:
    return PROCESS.callme(sentences)

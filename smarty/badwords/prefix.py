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

import smarty.utils

NOT_REQUIRED = smarty.utils.init_table("""\
abblocken
abklären
abmildern
abprüfen
absegnen
absenken
absichern
absinken
abstoppen
abstützen
abtesten
abzielen
anbetreffen
anheben
ankaufen
anschwellen
ansteigen
anwachsen
aufaddieren
auffülllen
auflisten
aufoktroyieren
aufspalten
aufsummieren
aufzeigen
ausborgen
auseinanderklaffen
ausleihen
befüllen
hochskalieren
losstarten
mit einbeziehen
mit einschließen
mithelfen
verbuchen
verfüllen
vorankommen
vorwarnen
weglöschen
zuliefern
zuschicken
überprüfen
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

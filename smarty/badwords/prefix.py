# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import german

import smarty.utils

NOT_REQUIRED = """\
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
"""
NOT_REQUIRED = smarty.utils.init(NOT_REQUIRED)


def prefix_not_required_search(sentence: str):
    matched = german.searches(
        tokenslist=NOT_REQUIRED,
        sentence=sentence,
        tokens_complex=False,
    )
    return matched


def prefix_not_required_fromtext(text):
    result = []
    for page, number, sentence in smarty.utils.sentences(text, numbers=True):
        detected = prefix_not_required_search(sentence)
        if not detected:
            continue
        result.append(
            smarty.serialize.Phrase(
                page=page,
                sentence=number,
                marked=detected,
            ))
    return result

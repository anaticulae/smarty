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

# yapf:disable
AVOID = smarty.utils.init_table("""\
eklatant
geflissentlich
hochkarätig
optimal
spektakulär
ungeahnt
unmissverständlich
zukunftsweisend
akzeptierbar                    akzeptabel
bewältigbar                     zu bewältigen
diskutierbar                    diskutabel
leistbar                        zu leisten
unaufhaltbar                    unaufhaltsam
unaufhörbar                     unaufhörlich
unentbehrbar                    unentbehrlich
unertragbar                     unerträglich
einzigste                       einzige                 nicht steigerbar
minimalste                      minimale                nicht steigerbar
maximalste                      maximale                nicht steigerbar
erstklassigsten                 erstklassig             nicht steigerbar
einfallsloseste                 einfallslos             nicht steigerbar
vorurteilsfreiste               vorurteilsfrei          nicht steigerbar
valider                         valide                  nicht steigerbar
reliabler                       reliable                nicht steigerbar
""", columns=3)
# yapf: enable


class AvoidAdjective(smarty.badwords.FromText):

    def __init__(self):
        super().__init__(tokens=AVOID)

    def advice(self, docref, raw):
        replacement = AVOID.get(raw, None)
        if replacement and len(replacement) == 2:
            replacement = replacement[0]
        result = iamraw.TextAdviceDelete(
            docref=docref,
            raw=raw,
            replacement=replacement,
        )
        return result


PROCESS = AvoidAdjective()


@utila.cacheme
def avoid_search(sentence: str) -> list:
    return PROCESS.search(sentence)


def avoid_fromtext(sentences) -> iamraw.TextAdviceReplacement:
    return PROCESS.callme(sentences)

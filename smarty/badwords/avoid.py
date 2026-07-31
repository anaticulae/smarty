# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import iamraw
import utilo

import smarty.badwords
import smarty.utils

# yapf:disable
AVOID = smarty.utils.init_table("""\
akzeptierbar                    akzeptabel
beeindruckend
bewältigbar                     zu bewältigen
diskutierbar                    diskutabel
einfallsloseste                 einfallslos             nicht steigerbar
einzigste                       einzige                 nicht steigerbar
eklatant
erstklassigsten                 erstklassig             nicht steigerbar
geflissentlich
hochkarätig
leistbar                        zu leisten
maximalste                      maximale                nicht steigerbar
minimalste                      minimale                nicht steigerbar
optimal
reliabler                       reliable                nicht steigerbar
spektakulär
unaufhaltbar                    unaufhaltsam
unaufhörbar                     unaufhörlich
unentbehrbar                    unentbehrlich
unertragbar                     unerträglich
ungeahnt
unmissverständlich
valider                         valide                  nicht steigerbar
vorurteilsfreiste               vorurteilsfrei          nicht steigerbar
zukunftsweisend
""", columns=3)
# yapf: enable


class AvoidAdjective(smarty.badwords.FromText):

    def __init__(self):
        super().__init__(tokens=AVOID)

    def advice(self, docref, raw):
        replacement = self.fromtable(raw)
        if replacement and len(replacement) == 2:
            replacement = replacement[0]
        result = iamraw.TextAdviceDelete(
            docref=docref,
            raw=raw,
            replacement=replacement,
        )
        return result


PROCESS = AvoidAdjective()


@utilo.cacheme
def avoid_search(sentence: str) -> list:
    return PROCESS.search(sentence)


def avoid_fromtext(sentences) -> iamraw.TextAdviceReplacement:
    return PROCESS.callme(sentences)

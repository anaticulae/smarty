# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo


def smarty_phrases(path: str, prefix: str = '') -> str:
    return utilo.pathconnector(path, 'smarty', 'phrases_phrases', prefix)


def smarty_pleonasmas(path: str, prefix: str = '') -> str:
    return utilo.pathconnector(path, 'smarty', 'pleonasma_pleonasma', prefix)


def smarty_reduces(path: str, prefix: str = '') -> str:
    return utilo.pathconnector(path, 'smarty', 'reduce_reduce', prefix)


def smarty_spelling_hyphen(path: str, prefix: str = '') -> str:
    return utilo.pathconnector(path, 'smarty', 'spelling_hyphen', prefix)


def smarty_spelling_guess(path: str, prefix: str = '') -> str:
    return utilo.pathconnector(path, 'smarty', 'spelling_guess', prefix)

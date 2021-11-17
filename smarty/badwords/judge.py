# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import enum

import utila

import smarty.badwords.avoid
import smarty.badwords.fat
import smarty.badwords.pleonasmen
import smarty.badwords.prefix
import smarty.utils


class BadWord(enum.Enum):
    AVOID_PREFIX = enum.auto()
    AVOID_ADJECTIVE = enum.auto()
    FAT = enum.auto()
    PLEONASMEN = enum.auto()


def badwords_judge(wordlist: list, skip_empty: bool = False) -> list:
    result = []
    for word in wordlist:
        current = set()
        if word in smarty.badwords.avoid.AVOID:
            current.add(BadWord.AVOID_ADJECTIVE)
        if word in smarty.badwords.fat.FAT:
            current.add(BadWord.FAT)
        if word in smarty.badwords.prefix.NOT_REQUIRED:
            current.add(BadWord.AVOID_PREFIX)
        if word in smarty.badwords.pleonasmen.NOUN:
            current.add(BadWord.PLEONASMEN)
        # do not store no findings if skip_empty is active
        if current or not skip_empty:
            result.append(current)
    return result


def ratio_fat(wordlist: list) -> float:
    """Determine count of `fat` words in list of `wordlist`."""
    if not wordlist:
        return None
    # remove marks etc.
    wordlist = [item for item in wordlist if isinstance(item, str)]
    # judge word list
    bad = badwords_judge(wordlist, skip_empty=True)
    flat = utila.flatten(bad)
    fat = [item for item in flat if item == BadWord.FAT]
    ratio = utila.roundme(len(fat) / len(wordlist))
    return ratio


def ratio_fat_fromtext(text) -> float:
    collected = smarty.utils.words_fromtext(text)
    result = ratio_fat(collected)
    return result

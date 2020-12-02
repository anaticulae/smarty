# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import enum

import utila

import smarty.badwords.adjective
import smarty.badwords.fat
import smarty.badwords.pleonasmen
import smarty.badwords.prefix


class BadWord(enum.Enum):
    AVOID_PREFIX = enum.auto()
    AVOID_ADJECTIVE = enum.auto()
    FAT = enum.auto()
    PLEONASMEN = enum.auto()


def badwords_judge(words: list, skip_empty: bool = False) -> list:
    result = []
    for word in words:
        current = set()
        if word in smarty.badwords.adjective.AVOID:
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


def ratio_fat(words: list) -> float:
    """Determine count of `fat` words in list of `words`."""
    if not words:
        return None
    bad = badwords_judge(words, skip_empty=True)
    flat = utila.flatten(bad)
    fat = [item for item in flat if item == BadWord.FAT]
    ratio = utila.roundme(len(fat) / len(words))
    return ratio

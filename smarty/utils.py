# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import re

import germania
import utilo


def words_fromtext(text, nomarks: bool = False) -> list:
    collected = []
    for _, sentence in sentences(text):
        splitted = germania.split_words(items=sentence,
                                        validate_sentences=False)
        collected.extend(splitted)
    if nomarks:
        collected = [item for item in collected if isinstance(item, str)]
    return collected


def sentences(texts, numbers: bool = False):
    number, current = 0, None
    for chunk in texts:
        for section in chunk.content:
            for page, sentence in zip(section.pages, section.content):
                if not numbers:
                    yield page, sentence
                else:
                    if current != page:
                        number = 0
                        current = page
                    else:
                        number += 1
                    yield page, number, sentence


class AdviceTable(collections.UserDict):

    def __or__(self, value) -> set:
        if isinstance(value, AdviceTable):
            value = value.keys()
        return set(self.keys()) | value

    def __ror__(self, value) -> set:
        if isinstance(value, AdviceTable):
            value = value.keys()
        return set(self.keys()) | value


def init_table(data: str, columns: int = 2) -> AdviceTable:
    r"""\
    >>> result = init_table('''
    ... ausgangsvoraussetzungen             voraussetzung
    ... auslandsexport                      export
    ... \n
    ... no right column
    ... einzelindividuum                    individuum
    ... ''')

    >>> {'einzelindividuum': 'individuum', 'no right column': ''} in result
    """
    # TODO: REPLACE WITH UTILA CODE
    lines = utilo.splitlines(data)
    result = AdviceTable()
    valid = utilo.rtuple(start=1, end=columns + 1)
    for line in lines:
        line = line.strip()
        if line[0] == '#':
            continue
        splitted = re.split(r'\s{5,}', line, maxsplit=columns - 1)
        assert len(splitted) in valid, splitted
        if len(splitted) == 1:
            result[splitted[0]] = ''
        elif len(splitted) == 2:
            result[splitted[0]] = splitted[1]
        else:
            result[splitted[0]] = splitted[1:]
    return result

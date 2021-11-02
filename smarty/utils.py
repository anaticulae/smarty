# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import german


def init(text: str) -> set:
    return {item.lower() for item in text.splitlines() if item}


def words_fromtext(text, nomarks: bool = False) -> list:
    collected = []
    for _, sentence in sentences(text):
        splitted = german.split_words(items=sentence, validate_sentences=False)
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

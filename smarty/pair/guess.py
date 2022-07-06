# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections

import german
import konrad
import utila

import smarty.utils

HyphenGuess = collections.namedtuple('HypenError', 'page sentence token raw')


def guess(sentences) -> list:  # pylint:disable=R0914
    guesses = []
    for page, number, sentence in smarty.utils.sentences(
            sentences,
            numbers=True,
    ):
        tokens = german.word_tokenize(
            sentence,
            validate_sentences=False,
        )
        # skip first word cause sentence starts always with upper cased
        # letter.
        tokens, start = left_strip(tokens)
        for length in (5, 4, 3, 2):
            ngrams = german.ngram(tokens, length=length)
            for index, ngram in enumerate(ngrams, start=start):
                try:
                    if any(not item[0].isupper() for item in ngram):
                        continue
                except TypeError:
                    # Mark inside
                    continue
                hyphen_before = tokens[index - start - 1] == konrad.Mark.HYPHEN
                if hyphen_before:
                    continue
                if any(simple_gramar(item) for item in ngram):
                    continue
                raw = ' '.join(ngram)
                if any(char in raw for char in INVALIDS):
                    continue
                hypen = HyphenGuess(
                    page=page,
                    sentence=number,
                    token=utila.rtuple(index, index + len(ngram)),
                    raw=raw,
                )
                guesses.append(hypen)
                # overwrite word to avoid double detection
                for word in range(length):
                    tokens[index - start + word] = None
    return guesses


def left_strip(tokens):
    """Remove sentence signs and first upper cased word."""
    start = 0
    while tokens and konrad.isspecial(tokens[0]):
        tokens = tokens[1:]
        start += 1
    # remove first upper char
    tokens = tokens[1:]
    if tokens:
        start += 1
    return tokens, start


@utila.cacheme
def simple_gramar(token: str) -> bool:
    if token.lower() in SKIP:
        return True
    if '.' in token:
        # TODO: MAY REMOVE LATER
        # skip vgl.
        return True
    return False


ARTICLES = utila.splititems('DAS DIE DER')

NUMBERS = utila.splititems(
    'EINS ERSTE ERSTER ZWEI ZWEITE ZWEITER DREI DRITTE DRITTER '
    'VIER VIERTER VIERTE FÜNF FÜNFTE FÜNFTER SECHS SECHTE SECHTER '
    'SIEBEN SIEBTE SIEBTER ACHT ACTE ACTER NEUN NEUNTE NEUNTER '
    'ZEHN ELF ZWÖLF DREIZEHN VIERZEHN HUNDERT TAUSEND MILLION MILLIONEN '
    'MILLIARDE MILLIARDEN ')

PRONOMS = utila.splititems('MEIN MEINER DEIN DEINER IHR IHRER SEIN SEINER')

SKIP = ARTICLES | NUMBERS | PRONOMS

INVALIDS = ',;:!?=()[]{}'

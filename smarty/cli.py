#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import utilo
import utilo.cli

import smarty

DESCRIPTION = ''

WORKPLAN = [
    utilo.create_step(
        'avoid',
        inputs=[
            utilo.ResultFile('words', 'sentences_sentences'),
        ],
        output=('avoid',),
    ),
    utilo.create_step(
        'improvement',
        inputs=[
            utilo.ResultFile('words', 'sentences_sentences'),
        ],
        output=('improvement',),
    ),
    utilo.create_step(
        'phrases',
        inputs=[
            utilo.ResultFile('words', 'sentences_sentences'),
        ],
        output=('phrases',),
    ),
    utilo.create_step(
        'pleonasma',
        inputs=[
            utilo.ResultFile('words', 'sentences_sentences'),
        ],
        output=('pleonasma',),
    ),
    utilo.create_step(
        'reduce',
        inputs=[
            utilo.ResultFile('words', 'sentences_sentences'),
        ],
        output=('reduce',),
    ),
    utilo.create_step(
        'spelling',
        inputs=[
            utilo.ResultFile('words', 'sentences_sentences'),
        ],
        output=('hyphen', 'guess'),
    ),
]


def main():
    utilo.featurepack(
        root=smarty.ROOT,
        workplan=WORKPLAN,
        featurepackage='smarty.features',
        config=utilo.FeaturePackConfig(
            description=DESCRIPTION,
            multiprocessed=True,
            name=smarty.PROCESS,
            pages=True,
            version=smarty.__version__,
        ),
    )

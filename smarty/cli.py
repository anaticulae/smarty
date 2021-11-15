#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import utila
import utila.cli

import smarty

DESCRIPTION = ''

WORKPLAN = [
    utila.create_step(
        'badwords',
        inputs=[
            utila.ResultFile('words', 'sentences_sentences'),
        ],
        output=('phrases', 'pleonasms', 'invalid_prefix'),
    ),
]


def main():
    utila.featurepack(
        root=smarty.ROOT,
        workplan=WORKPLAN,
        featurepackage='smarty.features',
        config=utila.FeaturePackConfig(
            description=DESCRIPTION,
            multiprocessed=True,
            name=smarty.PROCESS,
            pages=True,
            version=smarty.__version__,
        ),
    )

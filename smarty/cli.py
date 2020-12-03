#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import utila
import utila.cli

import smarty

COMMANDS = [
    utila.create_step(
        'phrases',
        inputs=[
            utila.ResultFile('words', 'word_result'),
            utila.ResultFile('words', 'headlines_headlines'),
        ],
        output=('detected',),
    ),
]


@utila.saveme
def main():
    parser = utila.cli.create_parser(
        COMMANDS,
        version=smarty.__version__,
        config=utila.ParserConfiguration(
            outputparameter=True,
            inputparameter=True,
            multiprocessed=True,
        ),
    )
    args = utila.parse(parser)
    inputpath, output, _ = utila.sources(args)  # pylint:disable=W0612

    return utila.SUCCESS

# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import docref.serialize

Phrase = docref.serialize.DocRef
Phrases = docref.serialize.DocRefs

dump_phrases = docref.serialize.dump_docref  # pylint:disable=C0103
load_phrases = docref.serialize.load_docref  # pylint:disable=C0103

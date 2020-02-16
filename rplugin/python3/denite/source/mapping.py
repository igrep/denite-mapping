# ============================================================================
# FILE: mapping.py
# AUTHOR: YAMAMOTO Yuji <whosekiteneverfly@gmail.com>
# License: Apache-2.0 license
# ============================================================================
from .base import Base

import re
import codecs

_RE_STAR_AT = re.compile(r'\s+\*@')
_RE_SNR_OR_PLUG = re.compile(r'^[a-z]*\s*<(?:SNR|Plug)>')

def _reject_snr_plug(lines):
    result = []
    for line in lines:
        if not _RE_SNR_OR_PLUG.search(line):
            result.append({ "word": line })
    return result

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'mapping'

    def on_init(self, context):
        pass

    def highlight(self):
        pass

    def define_syntax(self):
        pass

    def gather_candidates(self, context):
        lines = self.vim.command_output('map').splitlines()

        # As unite-mapping does, sort lines by it contains "\s+*@"
        star_at_lines = []
        non_star_at_lines = []
        for line in lines:
            if _RE_STAR_AT.search(line):
                star_at_lines.append(line)
            else:
                non_star_at_lines.append(line)

        candidates = _reject_snr_plug(star_at_lines)
        candidates.extend(_reject_snr_plug(non_star_at_lines))
        return candidates

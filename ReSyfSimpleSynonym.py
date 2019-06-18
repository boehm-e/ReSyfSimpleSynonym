import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import ReSyf

class Synonymes(object):
    """Find synonymes for words."""

    def __init__(self):
        super(Synonymes, self).__init__()
        self.lexicalRes = ReSyf.load(os.path.dirname(os.path.realpath(__file__)))

    def find_simpler(self, word, pos="VER"):
        simpler = None
        try:
            simpler = list(ReSyf.get_more_simple_synonyms(self.lexicalRes, word, pos, None).items())[1][1]["synonyms"][0].get_word()
        except Exception as e:
            pass

        if (simpler != word):
            return simpler
        else:
            return None

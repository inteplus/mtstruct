import mt.base.pyximportcpp as pyximport; pyximport.install(language_level=3)
from .version import VERSION as __version__

import sys
import os.path as _op
_dirpath = _op.dirname(__file__)
sys.path.append(_dirpath)
from .trie import Trie
del sys.path[-1]

from enum import Enum


class NodeTag(Enum):
    """
    To mark visited nodes during DFS.
    """
    WHITE = 0
    GRAY = 1
    BLACK = 2

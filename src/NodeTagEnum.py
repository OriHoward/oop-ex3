from enum import Enum


class NodeTag(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


# examples- how to use
print(NodeTag.GRAY)
print(NodeTag.GRAY.name)
print(NodeTag.GRAY.value)
print(NodeTag.WHITE == NodeTag.BLACK)
print(NodeTag.WHITE == NodeTag.WHITE)
print(NodeTag.WHITE.value == NodeTag.WHITE.value)
print(NodeTag.WHITE.value == NodeTag.GRAY.value)

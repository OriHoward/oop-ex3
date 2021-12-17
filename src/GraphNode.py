from GraphEdge import GraphEdge
from Position import Position


class GraphNode:
    srcMap: dict[int, GraphEdge]
    destMap: dict[int, GraphEdge]
    position: Position
    _id: int
    dist: float

    def __init__(self, position: Position, _id: int):
        self.srcMap = {}
        self.destMap = {}
        self.position = Position()
        self._id = _id

from GraphEdge import GraphEdge
from Position import Position


class GraphNode:
    srcMap: dict[int, GraphEdge]
    destMap: dict[int, GraphEdge]
    position: Position
    _id: int
    dist: float

    def __init__(self, position: Position, _id: int):
        self._srcMap = {}
        self._destMap = {}
        self._position = Position(position.get_x(), position.get_y(), position.get_z())
        self._id = _id

    def get_srcMap(self):
        return self._srcMap

    def get_destMap(self):
        return self._destMap

    def get_key(self):
        return self._id

    def add_dest(self, edge: GraphEdge):
        self._destMap[edge.get_dest()] = edge

    def add_src(self,edge: GraphEdge):
        self._srcMap[edge.get_src()] = edge

    def remove_dest(self, dest: int):
        return self._destMap.pop(dest)

    def remove_src(self, src: int):
        return self._srcMap.pop(src)






from GraphEdge import GraphEdge
from Position import Position


class GraphNode:

    def __init__(self, _id: int, pos: tuple = None):
        self._srcMap = {}
        self._destMap = {}
        if pos is not None:
            self._position = Position(*pos)
        self._id = _id
        self._dist: float = float('inf')

    def get_srcMap(self):
        return self._srcMap

    def get_destMap(self):
        return self._destMap

    def get_key(self):
        return self._id

    def add_dest(self, edge: GraphEdge):
        self._destMap[edge.get_dest()] = edge

    def add_src(self, edge: GraphEdge):
        self._srcMap[edge.get_src()] = edge

    def remove_dest(self, dest: int) -> GraphEdge:
        return self._destMap.pop(dest, None)

    def remove_src(self, src: int) -> GraphEdge:
        return self._srcMap.pop(src, None)

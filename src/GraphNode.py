from GraphEdge import GraphEdge
from Position import Position
from NodeTagEnum import NodeTag


class GraphNode:

    def __init__(self, _id: int, pos: tuple = None):
        self._srcMap = {}
        self._destMap = {}
        if pos is not None:
            self._position = Position(*pos)
        self._id = _id
        self._dist: float = float('inf')
        self._tag = NodeTag.WHITE

    def get_srcMap(self):
        return self._srcMap

    def get_destMap(self):
        return self._destMap

    def get_dist(self):
        return self._dist

    def set_dist(self, dist):
        self._dist = dist

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

    def to_json_dict(self):
        if not hasattr(self, '_position'):
            return {"id": self.get_key()}
        else:
            return {"id": self.get_key(), "pos": self._position.get_json_format_str()}

    def set_tag(self, tag: NodeTag):
        self._tag = tag

    def get_tag(self):
        return self._tag
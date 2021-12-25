from GraphEdge import GraphEdge
from Position import Position
from NodeTagEnum import NodeTag


class GraphNode:

    def __init__(self, _id: int, pos: tuple = None):
        self._srcMap = {}
        self._destMap = {}
        if pos is not None:
            self._position = Position(*pos)
        else:
            self._position = Position()
        self._id = _id
        self._dist: float = float('inf')
        self._tag = NodeTag.WHITE

    def get_srcMap(self):
        return self._srcMap

    def get_destMap(self):
        return self._destMap

    def set_srcMap(self, src_map: dict):
        self._srcMap = src_map

    def set_destMap(self, dest_map: dict):
        self._destMap = dest_map

    def get_dist(self):
        return self._dist

    def set_dist(self, dist: float):
        if type(dist) == int or type(dist) == float:
            self._dist = dist
        else:
            raise ValueError("Bad dist set")

    def get_key(self):
        """Returns node ID"""
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

    def get_pos(self) -> Position:
        return self._position

    def set_tag(self, tag: NodeTag):
        """Set if node was visited (used in DFS)"""
        self._tag = tag

    def get_tag(self):
        """Returns the node tag"""
        return self._tag

    def __lt__(self, other):
        """
        less-than operator.
        """
        return self.get_dist() < other.get_dist()

    def __str__(self):
        return f"Node: ID={self._id}, pos=({self._position})"

    def __repr__(self):
        return f"{self._id}: |edges out| {len(self.get_destMap())} |edges in| {len(self.get_srcMap())}"

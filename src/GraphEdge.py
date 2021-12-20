class GraphEdge:
    src: int
    dest: int
    weight: float

    def __init__(self, src, dest, weight):
        self._src = src
        self._dest = dest
        self._weight = weight

    def get_src(self):
        return self._src

    def get_dest(self):
        return self._dest

    def get_weight(self):
        return self._weight

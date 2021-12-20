class GraphEdge:

    def __init__(self, src, dest, weight):
        self._src: int = src
        self._dest: int = dest
        self._weight: int = weight

    def get_src(self):
        return self._src

    def get_dest(self):
        return self._dest

    def get_weight(self):
        return self._weight


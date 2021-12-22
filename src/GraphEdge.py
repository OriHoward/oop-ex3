class GraphEdge:

    def __init__(self, src, dest, weight):
        self._src: int = int(src)
        self._dest: int = int(dest)
        self._weight: float = float(weight)

    def get_src(self):
        return self._src

    def get_dest(self):
        return self._dest

    def get_weight(self):
        return self._weight

    def set_dest(self, dest: int):
        self._dest = dest

    def set_src(self, src: int):
        self._src = src

    def to_json_dict(self):
        return {
            "src": self._src,
            "w": self._weight,
            "dest": self._dest
        }

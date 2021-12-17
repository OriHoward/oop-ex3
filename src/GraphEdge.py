class GraphEdge:
    src: int
    dest: int
    weight: float

    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

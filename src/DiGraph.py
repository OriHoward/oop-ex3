from GraphInterface import GraphInterface
from GraphNode import GraphNode
from src.GraphEdge import GraphEdge


class DiGraph(GraphInterface):

    def __init__(self):
        self._nodeMap: dict[int, GraphNode] = {}
        self._MCount: int = 0
        self._parsed_edges: list[GraphEdge] = []

    def get_parsed_edges(self) -> list:
        return self._parsed_edges

    def get_nodeMap(self):
        return self._nodeMap

    def get_node(self, key: int) -> GraphNode:
        return self._nodeMap.get(key)

    def get_edge(self, src: int, dest: int):
        node = self._nodeMap.get(src)
        if node is None:
            return None
        if node.get_destMap().get(dest) is None:
            return None
        return node.get_destMap().get(dest)

    def v_size(self) -> int:
        return len(self._nodeMap)

    def e_size(self) -> int:
        return len(self._parsed_edges)

    def get_mc(self) -> int:
        return self._MCount

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        src_node = self._nodeMap.get(id1)
        dest_node = self._nodeMap.get(id2)
        if src_node is None or dest_node is None or src_node == dest_node or weight < 0:
            return False
        edge = GraphEdge(id1, id2, weight)
        old_edge = src_node.get_destMap().get(id2)
        if old_edge is None:
            self._parsed_edges.append(edge)
        else:
            self._parsed_edges.remove(old_edge)
            self._parsed_edges.append(edge)
        src_node.add_dest(edge)
        dest_node.add_src(edge)
        self._MCount += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        try:
            self._nodeMap[node_id] = GraphNode(node_id, pos)
        except Exception as e:
            print(e)
            return False

    def remove_node(self, node_id: int) -> bool:  # todo: finish
        curr_node = self._nodeMap.get(node_id)
        if curr_node is None:
            return False
        src_map = curr_node.get_srcMap()
        for key in src_map.keys():
            curr_father = src_map.get(key)
            removed_edge = curr_father.remove_dest(curr_node.get_key())
        dest_map = curr_node.get_destMap()
        for key in dest_map.keys():
            pass
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        src_node = self._nodeMap.get(node_id1)
        dest_node = self._nodeMap.get(node_id2)
        if src_node is None or dest_node is None:
            return False
        removed_edge = src_node.remove_dest(node_id2)
        if removed_edge is None:
            return False
        dest_node.remove_src(node_id1)
        self._MCount += 1
        self._parsed_edges.remove(removed_edge)
        return True

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """
        return self._nodeMap

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """

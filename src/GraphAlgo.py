import json
from typing import List
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def load_from_json(self, file_name: str) -> bool:
        json_dict = {}
        self.graph = DiGraph()
        with open(file_name, 'r') as f:
            json_dict = json.load(f)
        for node in json_dict["Nodes"]:
            node_id = node.get("id")
            pos: tuple = tuple(node.get("pos", "").split(',')[:-1])
            self.graph.add_node(node_id, pos)

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        return 0, 0

    def plot_graph(self) -> None:
        pass

    def get_graph(self) -> GraphInterface:
        return self.graph

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """

    def __init__(self, graph=None):
        self.graph = graph

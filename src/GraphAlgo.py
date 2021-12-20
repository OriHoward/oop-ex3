import copy
import json
from typing import List

from GraphJSONEncoder import GraphEncoder
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from NodeTagEnum import NodeTag
import heapq
from collections import deque

class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=None):
        self.prev: dict[int, List] = {}
        if graph is None:
            self.graph: DiGraph = DiGraph()
        else:
            self.graph: DiGraph = graph

    def load_nodes(self, nodes) -> bool:
        if nodes is None:
            return False
        for node in nodes:
            node_id = node.get("id")
            pos: tuple = tuple(node.get("pos", "").split(',')[:-1])
            is_added = self.graph.add_node(node_id, pos)
            if not is_added:
                return False
        return True

    def load_edges(self, edges) -> bool:
        if edges is None:
            return False
        for edge in edges:

            is_added = self.graph.add_edge(edge.get('src', None), edge.get('dest', None), edge.get('w', None))
            if not is_added:
                return False
        return True

    def load_from_json(self, file_name: str) -> bool:
        try:
            json_dict = {}
            self.graph = DiGraph()
            with open(file_name, 'r') as f:
                json_dict = json.load(f)

            return self.load_nodes(json_dict["Nodes"]) and self.load_edges(json_dict["Edges"])

        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            to_json = {}
            node_list = list(self.graph.get_all_v().values())
            edge_list = self.graph.get_parsed_edges()
            to_json["Nodes"] = node_list
            to_json["Edges"] = edge_list
            with open(file_name, 'w') as fp:
                json.dump(to_json, fp, cls=GraphEncoder)
            return True
        except Exception as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        return 0, 0

    def plot_graph(self) -> None:
        pass

    def get_graph(self) -> GraphInterface:
        return self.graph

    def is_connected(self):
        pass

    def reset_graph_vars(self, graph: DiGraph):
        self.prev.clear()
        for node in graph.get_nodeMap().values():
            node.set_tag(NodeTag.WHITE)

    def is_connected_dfs(self):
        graph_copy = copy.deepcopy(self.graph)  # deep copy of graph to prevent issues
        if graph_copy is None:
            return False
        scanned_nodes = set()
        first_node = graph_copy.get_nodeMap().get(0)
        self.dfs_traversal(graph_copy, first_node, scanned_nodes)
        if len(scanned_nodes) != len(graph_copy.get_nodeMap()):
            return False
        scanned_nodes.clear()
        self.reset_graph_vars()
        graph_copy.initiate_edge_maps()
        self.dfs_traversal(graph_copy, first_node, scanned_nodes)
        if len(scanned_nodes) != len(graph_copy.get_parsed_edges()):
            return False
        return True

    def dfs_traversal(self, graph_copy, curr_node, scanned_nodes):
        stack = deque()
        stack.append(curr_node)
        while len(stack) > 0:
            pass


    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """

    # def dijkstra_minimize(self, src: int):
    #     curr_node = self.graph.get_node(src)
    #     curr_node.set_dist(0.0)
    #     to_scan = []
    #     for node in self.graph.get_nodeMap().values():
    #         if node.get_key() != src:
    #             node.set_dist('inf')
    #         heapq.heappush(to_scan, node)
    #     while len(to_scan) > 0:
    #         node = heapq.heappop(to_scan)
    #         for curr_edge in self.graph.get_parsed_edges():
    #             pass
    #     pass

    def centerPoint(self) -> (int, float):
        pass
        # curr_minMax = 'inf'
        # chosen_node = 0
        # for curr_node_id in self.graph.get_nodeMap().keys():
        #     self.dijkstra_minimize(curr_node_id)
        #     minMax_index = self.find_max()
        #     node = self.graph.get_node(minMax_index)
        #     if node.get_dist() < curr_minMax:
        #         curr_minMax = node.get_dist()
        #         chosen_node = curr_node_id
        # return chosen_node

    def find_max(self) -> int:
        maximum = 'inf'
        max_index = 0
        for curr_node in self.graph.get_nodeMap().values():
            if curr_node.get_dist() > maximum:
                maximum = curr_node.get_dist()
                max_index = curr_node.get_key()
        return max_index

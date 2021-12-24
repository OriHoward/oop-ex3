import copy
import json
from typing import List

from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
import matplotlib.pyplot as plt
from GraphNode import GraphNode
from GraphInterface import GraphInterface
from NodeTagEnum import NodeTag
import heapq
from collections import deque

from GraphJSONEncoder import GraphEncoder


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=None):
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
        if id1 == id2 or self.graph.get_node_map().get(id1) is None or self.graph.get_node_map().get(id2) is None:
            return float('inf'), []
        prev = self.dijkstra(id1)
        prev.get(id2).append(id2)
        dest_node = self.graph.get_node(id2)
        if dest_node.get_dist() == float('inf'):
            return float('inf'), []
        return dest_node.get_dist(), prev.get(id2)

    def plot_graph(self) -> None:
        for curr_node in self.graph.get_node_map().values():
            x = curr_node.get_pos().get_x()
            y = curr_node.get_pos().get_y()
            plt.plot(x, y, markersize=8, marker='.', color="red")
            plt.text(x, y, curr_node.get_key(), color="b", fontsize=8, fontweight="bold")
        for curr_edge in self.graph.get_parsed_edges():
            node_key_src: int = curr_edge.get_src()
            node_key_dest: int = curr_edge.get_dest()
            node_src: GraphNode = self.graph.get_node(node_key_src)
            node_dest: GraphNode = self.graph.get_node(node_key_dest)
            src_x = node_src.get_pos().get_x()
            src_y = node_src.get_pos().get_y()
            dest_x = node_dest.get_pos().get_x()
            dest_y = node_dest.get_pos().get_y()
            plt.annotate("", xy=(src_x, src_y), xytext=(dest_x, dest_y), arrowprops=dict(arrowstyle="<-"))
        plt.xlabel('x axis')
        plt.ylabel('y axis')
        plt.tight_layout()
        plt.show()

    def get_graph(self) -> GraphInterface:
        return self.graph

    @staticmethod
    def reset_graph_vars(graph: DiGraph):
        """
        Resets the tag used to mark if the nodes were visited.
        """
        for node in graph.get_node_map().values():
            node.set_tag(NodeTag.WHITE)

    def is_connected(self):
        """
        Returns true if the graph is strongly connected (has a path from each node to every other node).
        """
        return self.is_connected_dfs()

    def is_connected_dfs(self):
        """
        Function creates a deep copy of the graph, runs DFS traversal on the original graph and then again on the
        transposed graph.
        """
        graph_copy = copy.deepcopy(self.graph)  # deep copy of graph to prevent issues
        if graph_copy is None:
            return False
        scanned_nodes = set()
        self.reset_graph_vars(graph_copy)
        first_node = graph_copy.get_node_map().get(0)
        self.dfs_traversal(graph_copy, first_node, scanned_nodes)
        if len(scanned_nodes) != len(graph_copy.get_node_map()):
            return False
        # init for second dfs on transposed graph
        scanned_nodes.clear()
        self.reset_graph_vars(graph_copy)
        graph_copy.initiate_edge_maps()
        self.dfs_traversal(graph_copy, first_node, scanned_nodes)
        if len(scanned_nodes) != len(graph_copy.get_node_map()):
            return False
        return True

    @staticmethod
    def dfs_traversal(graph_copy, curr_node, scanned_nodes):
        """
        DFS is iterative since the recursive approach can cause a stack overflow error on large graphs.
        The graph edges are transposed during the search.
        """
        stack = deque()
        stack.append(curr_node)
        while len(stack) > 0:
            curr_node = stack.pop()
            if curr_node is None:
                continue
            scanned_nodes.add(curr_node.get_key())
            if curr_node.get_tag() == NodeTag.WHITE:
                curr_node.set_tag(NodeTag.GRAY)
                for neighbor_edge in graph_copy.all_out_edges_of_node(curr_node.get_key()).values():
                    stack.append(graph_copy.get_node(neighbor_edge.get_dest()))
                    tmp = neighbor_edge.get_dest()  # transpose edges of the graph (for second dfs)
                    neighbor_edge.set_dest(neighbor_edge.get_src())
                    neighbor_edge.set_src(tmp)
            curr_node.set_tag(NodeTag.BLACK)
            curr_node.set_srcMap(dict())  # src and dest map are initialized in is_connected_dfs function (above)
            curr_node.set_destMap(dict())

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list.
        """
        if node_lst is None or len(node_lst) == 0:
            return list(), float('inf')
        if len(node_lst) == 1:
            return node_lst, 0
        cities = set(node_lst)  # set removes duplicates
        best_path, dist = self.get_optimal_path_to_cities(cities)
        self.remove_visited_cities(cities, best_path)
        path = list(best_path)
        while len(cities) > 0:
            path_from_end, dist_from_end = self.get_optimal_path_from_node(path[-1], cities, False)
            path_from_start, dist_from_start = self.get_optimal_path_from_node(path[0], cities, True)
            if path_from_start is None and path_from_end is None:
                return list(), float('inf')
            elif len(path_from_start) < len(path_from_end):
                path.extend(list(path_from_end))
                dist += dist_from_end
                self.remove_visited_cities(cities, path_from_end)
            else:
                path = list(path_from_start) + path
                dist += dist_from_start
                self.remove_visited_cities(cities, path_from_start)
        return path, dist

    @staticmethod
    def remove_visited_cities(cities: set[int], curr_path: tuple[int]):
        """
        Removes nodes from the set that are in the given path.
        """
        for key in curr_path:
            if key in cities:
                cities.remove(key)

    # previous name: getOptimalPathFromList
    def get_optimal_path_to_cities(self, cities: set[int]):
        """
        Finds the shortest path between every pair of nodes.
        """
        path_map: dict[tuple[int], float] = dict()
        for key1 in cities:
            for key2 in cities:
                if key1 != key2:
                    dist, shortest_path = self.shortest_path(key1, key2)
                    if len(shortest_path) > 0 and shortest_path is not None:
                        path_map[tuple(shortest_path)] = dist
        return self.get_optimal_path_from_map(cities, path_map)

    @staticmethod
    def get_optimal_path_from_map(cities: set[int], path_map: dict[tuple[int], float]) -> (tuple[int], float):
        """
        Returns the path that minimizes the the distance of the path containing the maximum number of unique nodes.
        """
        max_size = 0
        best_path = tuple()
        for path in path_map.keys():
            curr_participants: set[int] = set()
            for city in cities:
                if city in path:
                    curr_participants.add(city)
            if len(curr_participants) > max_size:
                best_path = path
                max_size = len(curr_participants)
            elif (len(curr_participants) == max_size) and (best_path is not None) and \
                    (path_map.get(path) < path_map.get(best_path)):
                best_path = path
        return best_path, path_map.get(best_path)

    # previous name: getOptimalPathFromLast
    def get_optimal_path_from_node(self, node_id: int, cities: set[int], is_start: bool) -> (tuple[int], float):
        # src  = 2 -> 1, 1  ->  4 = dest
        """
        Finds the shortest path from a given node to each node in the set. Returns the optimal path.
        (For optimal path: see function get_optimal_path_from_map documentation).
        """
        path_map: dict[tuple[int], float] = dict()
        for city in cities:
            if is_start:
                curr_dist, curr_shortest_path = self.shortest_path(city, node_id)
            else:
                curr_dist, curr_shortest_path = self.shortest_path(node_id, city)
            path_map[tuple(curr_shortest_path)] = curr_dist
        optimal_path, dist = self.get_optimal_path_from_map(cities, path_map)
        if optimal_path is None:
            return tuple(), -1
        else:
            path = list(optimal_path)
            if is_start:
                return tuple(path[:-1]), dist
            return tuple(path[1:]), dist

    def dijkstra(self, src: int) -> dict[int, list[int]]:
        prev: dict[int, list[int]] = {}
        curr_node = self.graph.get_node(src)
        curr_node.set_dist(0.0)
        to_scan = []
        for node in self.graph.get_node_map().values():
            if node.get_key() != src:
                node.set_dist(float('inf'))
                prev[node.get_key()] = []
            heapq.heappush(to_scan, node)

        while len(to_scan) > 0:
            node: GraphNode = heapq.heappop(to_scan)
            for curr_edge in node.get_destMap().values():
                neighbor = self.graph.get_node(curr_edge.get_dest())
                alt = node.get_dist() + curr_edge.get_weight()
                if alt < neighbor.get_dist():
                    neighbor.set_dist(alt)
                    if prev.get(node.get_key(), None) is not None:
                        prev[neighbor.get_key()] = copy.deepcopy(prev.get(node.get_key()))
                    prev.get(neighbor.get_key(), []).append(node.get_key())
                    heapq.heappush(to_scan, neighbor)
        return prev

    def dijkstra_minimize(self, src: int):
        curr_node = self.graph.get_node(src)
        curr_node.set_dist(0.0)
        to_scan = []
        for node in self.graph.get_node_map().values():
            if node.get_key() != src:
                node.set_dist(float('inf'))
            heapq.heappush(to_scan, node)
        while len(to_scan) > 0:
            node: GraphNode = heapq.heappop(to_scan)
            for curr_edge in node.get_destMap().values():
                neighbor = self.graph.get_node(curr_edge.get_dest())
                alt = node.get_dist() + curr_edge.get_weight()
                if alt < neighbor.get_dist():
                    neighbor.set_dist(alt)
                    heapq.heappush(to_scan, neighbor)

    def centerPoint(self) -> (int, float):
        if not self.is_connected():
            return -1, float('inf')
        curr_minMax = float('inf')
        chosen_node = 0
        for curr_node_id in self.graph.get_node_map().keys():
            self.dijkstra_minimize(curr_node_id)
            minMax_index = self.find_max()
            node = self.graph.get_node(minMax_index)
            if node.get_dist() < curr_minMax:
                curr_minMax = node.get_dist()
                chosen_node = curr_node_id
        return chosen_node, curr_minMax

    def find_max(self) -> int:
        maximum = float('-inf')
        max_index = 0
        for curr_node in self.graph.get_node_map().values():
            if curr_node.get_dist() > maximum:
                maximum = curr_node.get_dist()
                max_index = curr_node.get_key()
        return max_index

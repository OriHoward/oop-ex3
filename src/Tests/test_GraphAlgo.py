from unittest import TestCase

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from GraphInterface import GraphInterface
import os
from typing import cast


class TestGraphAlgo(TestCase):

    def setUp(self) -> None:
        self.test_json = './test.json'
        self.g_algo = GraphAlgo()
        g: GraphInterface = self.g_algo.get_graph()
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)

    def test_save_to_json(self):
        is_save_successful = self.g_algo.save_to_json(self.test_json)
        self.assertTrue(is_save_successful)
        os.unlink(self.test_json)

    def test_load_from_json(self):
        self.g_algo.save_to_json(self.test_json)
        self.g_algo.get_graph().remove_edge(0, 1)
        size = self.g_algo.get_graph().e_size()
        self.assertEqual(size, 1)
        self.g_algo.load_from_json(self.test_json)
        self.assertEqual(self.g_algo.get_graph().e_size(), 2)
        os.unlink(self.test_json)

    def test_shortest_path(self):
        self.g_algo.load_from_json("../../data/shortestPathTest.json")
        trail = [1, 2, 4, 5]
        self.assertEqual(trail, self.g_algo.shortest_path(1, 5)[1])

    def test_plot_graph(self):
        self.assertTrue(True)

    def test_get_graph(self):
        self.assertTrue(True)

    def test_tsp(self):
        self.g_algo.load_from_json("../../data/A1.json")
        cities = [5, 2, 9]
        actual_path = [2, 6, 5, 6, 7, 8, 9]
        path_dist, shortest_path = self.g_algo.TSP(cities)

        self.assertEqual(actual_path, shortest_path)

    def test_center_point(self):
        self.g_algo.load_from_json("../../data/centerTest.json")
        self.assertEqual(2, self.g_algo.centerPoint())

    def test_find_max(self):
        self.assertTrue(True)

    def test_is_connected(self):
        self.g_algo.load_from_json("../../data/notConnected.json")
        self.assertFalse(self.g_algo.is_connected())
        self.g_algo.load_from_json("../../data/isConnected.json")
        self.assertTrue(self.g_algo.is_connected())

    @staticmethod
    def get_dist_of_node(graph: DiGraph):
        return lambda node_id: graph.get_node(node_id).get_dist()

    def test_dijkstra(self):
        self.g_algo.load_from_json("../../data/dijkstraTest.json")
        self.g_algo.dijkstra(1)
        graph = cast(DiGraph, self.g_algo.get_graph())

        get_dist_of_node = self.get_dist_of_node(graph)

        self.assertAlmostEqual(1.9, get_dist_of_node(0), 4)
        self.assertAlmostEqual(0.0, get_dist_of_node(1), 4)
        self.assertAlmostEqual(0.4, get_dist_of_node(2), 4)
        self.assertAlmostEqual(1.2, get_dist_of_node(3), 4)
        self.assertAlmostEqual(float('inf'), get_dist_of_node(4), 4)
        self.assertAlmostEqual(2.4, get_dist_of_node(5), 4)

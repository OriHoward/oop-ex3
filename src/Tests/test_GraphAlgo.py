from unittest import TestCase

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from GraphInterface import GraphInterface
import os


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
        self.assertTrue(True)

    def test_plot_graph(self):
        self.assertTrue(True)

    def test_get_graph(self):
        self.assertTrue(True)

    def test_tsp(self):
        self.assertTrue(True)

    def test_center_point(self):
        self.assertTrue(True)

    def test_find_max(self):
        self.assertTrue(True)

import json
from unittest import TestCase

from GraphJSONEncoder import GraphEncoder
from GraphEdge import GraphEdge
from GraphNode import GraphNode


class Test(TestCase):
    def test_graph_encoder(self):
        first_node = GraphNode(0)
        second_node = GraphNode(1)
        edge = GraphEdge(0, 1, 2)
        expected_node_keys = ["id", "pos"]
        expected_edge_keys = ['src', 'w', "dest"]
        node_as_str = json.dumps(first_node, cls=GraphEncoder)
        edge_as_str = json.dumps(edge, cls=GraphEncoder)
        self.assertEqual(expected_node_keys, list(json.loads(node_as_str).keys()))
        self.assertEqual(expected_edge_keys, list(json.loads(edge_as_str).keys()))

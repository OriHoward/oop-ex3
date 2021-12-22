import pygame
from pygame import display
from pygame.constants import RESIZABLE
from pygame.gfxdraw import aacircle
from DiGraph import DiGraph
from GraphNode import GraphNode

WIDTH, HEIGHT = 1080, 800

pygame.init()
screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
clock = pygame.time.Clock()
pygame.font.init()

FONT = pygame.font.SysFont('Arial', 200, bold=True)


class GraphGui:
    def __init__(self, graph: DiGraph):
        self.graph: DiGraph = graph
        self.radius = 5
        self.margin = 40
        self.min_x = min(self.graph.get_nodeMap().values(), key=lambda node: node.get_pos().get_x()).get_pos().get_x()
        self.max_x = max(self.graph.get_nodeMap().values(), key=lambda node: node.get_pos().get_x()).get_pos().get_x()
        self.min_y = min(self.graph.get_nodeMap().values(), key=lambda node: node.get_pos().get_y()).get_pos().get_y()
        self.max_y = max(self.graph.get_nodeMap().values(), key=lambda node: node.get_pos().get_y()).get_pos().get_y()

    """this function is taken from class material"""

    def scale(self, data, min_screen, max_screen, min_data, max_data):
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

    def scale_me(self, data, x=False, y=False):
        if x:
            return self.scale(data, self.margin, screen.get_width() - self.margin, self.min_x, self.max_x)
        if y:
            return self.scale(data, self.margin, screen.get_width() - self.margin, self.min_y, self.max_y)

    def run_events(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

            screen.fill(pygame.Color(179, 229, 252))

            for curr_node in self.graph.get_nodeMap().values():
                pos_x = self.scale_me(curr_node.get_pos().get_x(), x=True)
                pos_y = self.scale_me(curr_node.get_pos().get_y(), y=True)
                pygame.gfxdraw.aacircle(screen, pos_x, pos_y, self.radius, pygame.Color(81, 45, 168))

            pygame.display.update()
            clock.tick(60)

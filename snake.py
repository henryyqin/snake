import pygame
import math

pygame.init()
pygame.display.set_caption('Snake')
MARGIN = 2
BLOCK_SIZE = 10
SIDE = 500
win = pygame.display.set_mode(size = (SIDE, SIDE))

class Spot():
    def __init__(self, side, x, y, color):
        self.side = side
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.side, self.side)
        self.color = color
        self.parent = parent

    def draw_spot(self):
        pygame.draw.rect(win, self.color, self.rect)

    def change_color(self, new_color):
        self.color = new_color
        pygame.draw.rect(win, self.color, self.rect)

    def get_color(self):
        return self.color

    def get_side(self):
        return self.side

    def get_position(self):
        return self.x, self.y

    def is_valid(self):
        return 0

class Grid():
    def __init__(self, margin, block_size, side):
        self.side = side
        self.margin = margin
        self.spots = []
        self.block_size = block_size

    def generate_spots(self):
        for x in range(0, self.side - self.block_size - self.margin, self.block_size + self.margin):
            for y in range(0, self.side - self.block_size - self.margin, self.block_size + self.margin):

                self.spots.append(Spot(self.block_size, i + self.margin, j + self.margin, white))
    def get_spots(self):
        return self.spots

    def draw(self):
        for spot in self.spots:
            spot.draw_spot()

    def get_neighbors(self, node):
        nbrs = []
        x1, y1 = node.get_position()
        for spot in self.spots:
            x2, y2 = spot.get_position()
            if (x2 == x1 + spot.get_side() + self.margin or x2 == x1 - self.margin - spot.get_side()) and y2 == y1 and spot.is_valid():
                nbrs.append(spot)
            elif (y2 == y1 + spot.get_side() + self.margin or y2 == y1 - self.margin - spot.get_side()) and y2 == y1 and spot.is_valid():
                nbrs.append(spot)
            elif (x2 == x1 + spot.get_side() + self.margin or x2 == x1 - self.margin - spot.get_side()) and (y2 == y1 + spot.get_side() + self.margin or y2 == y1 - spot.get_side() - self.margin) and spot.is_valid():
                nbrs.append(spot)
        return nbrs

grid = Grid(MARGIN, BLOCK_SIZE, SIDE)
spots = grid.get_spots()
grid.draw()
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            break
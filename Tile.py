import pygame
from pygame import Surface


class Tile:
    def __init__(self, x, y, size, armed):
        self.x = x
        self.y = y
        self.size = size

        # 0:Closed, 1:Flagged, 2:Opened
        self.state = 0

        self.armed = armed

    def draw(self, screen: Surface):
        # Draw the tile on the screen

        if self.armed:
            pygame.draw.rect(screen, (0, 0, 0, 255), (self.x, self.y, self.size, self.size))
        else:
            pygame.draw.rect(screen, (255, 255, 255, 255), (self.x, self.y, self.size, self.size))


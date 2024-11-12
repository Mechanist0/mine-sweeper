import pygame
from pygame import Surface


class Tile:
    def __init__(self, x, y, size, armed):
        self.x = x
        self.y = y
        self.size = size

        self.armed = armed

        self.danger = 0

        # 0:Closed, 1:Flagged, 2:Opened
        self.state = 0

        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)

    def draw(self, screen: Surface):
        # Draw the tile on the screen
        if self.state == 0:
            pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.size, self.size))
            pygame.draw.rect(screen, (255, 255, 255), (self.x+1, self.y+1, self.size-2, self.size-2))
        elif self.state == 1:
            pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.size, self.size))
        elif self.state == 2:
            if self.armed:
                pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.size, self.size))

            surface = self.my_font.render(str(self.danger), True, (0, 0, 0))
            screen.blit(surface, (self.x + self.size/4, self.y))

    def to_string(self):
        print(str(self.x), str(self.y), str(self.size), str(self.armed), str(self.state), str(self.danger))
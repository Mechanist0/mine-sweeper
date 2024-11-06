import pygame
from pygame import Surface


class Tile:
    def __init__(self, x, y, size, armed):
        self.x = x
        self.y = y
        self.size = size
        self.danger = 0

        # 0:Closed, 1:Flagged, 2:Opened
        self.state = 0

        self.armed = armed

        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)

    def draw(self, screen: Surface):
        # Draw the tile on the screen
        if self.state == 0:
            pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.size, self.size))
        elif self.state == 1:
            pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.size, self.size))
        elif self.state == 2:
            if self.armed:
                pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.size, self.size))

            if self.danger == 1:
                pygame.draw.rect(screen, (32, 0, 0), (self.x, self.y, self.size, self.size))
            elif self.danger == 2:
                pygame.draw.rect(screen, (32*2, 0, 0), (self.x, self.y, self.size, self.size))
            elif self.danger == 3:
                pygame.draw.rect(screen, (32*3, 0, 0), (self.x, self.y, self.size, self.size))
            elif self.danger == 4:
                pygame.draw.rect(screen, (32*4, 0, 0), (self.x, self.y, self.size, self.size))
            elif self.danger == 5:
                pygame.draw.rect(screen, (32*5, 0, 0), (self.x, self.y, self.size, self.size))
            elif self.danger == 6:
                pygame.draw.rect(screen, (32*6, 0, 0), (self.x, self.y, self.size, self.size))
            elif self.danger == 7:
                pygame.draw.rect(screen, (32*7, 0, 0), (self.x, self.y, self.size, self.size))
            elif self.danger == 8:
                pygame.draw.rect(screen, (32*8, 0, 0), (self.x, self.y, self.size, self.size))

            surface = self.my_font.render(str(self.danger), True, (0, 0, 0))
            screen.blit(surface, (self.x + self.size/4, self.y))



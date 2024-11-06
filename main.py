import pygame
from TileGrid import TileGrid

class MineSweeper:
    def __init__(self):
        # Game setup
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 720))
        self.clock = pygame.time.Clock()
        self.running = True
        self.width, self.height, self.size = 30, 30, 20
        self.tile_grid: TileGrid = TileGrid(30, 30, 20, 0.1)


    def main(self):
        self.game_init()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # Translate mouse location to grid index
                        index = (int(pygame.mouse.get_pos()[0] / self.size), int(pygame.mouse.get_pos()[1] / self.size))
                        self.tile_grid.uncover_tile(index[0], index[1], False)


            self.screen.fill((255, 255, 255))

            self.game_draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    # Setup the grid of the game and assign states to tiles
    def game_init(self):
        pygame.font.init()
        self.tile_grid.build_grid()
        self.tile_grid.calculate_nearby()

    def game_draw(self, screen):
        self.tile_grid.draw_grid(screen)

    def calculate_nearby(self, tile, tile_grid):
        pass

if __name__ == '__main__':
    MineSweeper().main()

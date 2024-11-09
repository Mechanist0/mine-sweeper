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
        self.tile_grid: TileGrid = TileGrid(10, 10, 20, 0.02, offset_x=50, offset_y=50)

        self.start_time = 0
        self.remaining_time = 0

    def main(self):
        self.game_init()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    index = (int((pygame.mouse.get_pos()[0]-50) / self.size), int((pygame.mouse.get_pos()[1]-50) / self.size))
                    output = 0
                    if event.button == 1:
                        output = self.tile_grid.uncover_tile(index[0], index[1], False)
                    elif event.button == 3:
                        output = self.tile_grid.uncover_tile(index[0], index[1], True)

                    if output == -1:
                        print("KABOOOOOM")
                        self.running = False

            if self.tile_grid.mines == 0:
                print("You WIN with " + str(self.remaining_time) + " seconds left")
                self.running = False

            self.screen.fill((255, 255, 255))

            self.game_draw(self.screen)
            self.remaining_time = 300 - (pygame.time.get_ticks() - self.start_time) / 1000
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    # Setup the grid of the game and assign states to tiles
    def game_init(self):
        pygame.font.init()
        self.tile_grid.build_grid()
        self.start_time = pygame.time.get_ticks()

    def game_draw(self, screen):
        # Draw Timer
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        mines_surface = my_font.render("Mines remaining: " + str(self.tile_grid.mines), False, (0, 0, 0))
        clock_surface = my_font.render("Mines remaining: " + str(int(self.remaining_time)), False, (0, 0, 0))

        screen.blit(mines_surface, (0, 0))
        screen.blit(clock_surface, (0, self.height))

        self.tile_grid.draw_grid(screen)


    def calculate_nearby(self, tile, tile_grid):
        pass

if __name__ == '__main__':
    MineSweeper().main()

import pygame

from TileGrid import TileGrid

tile_grid: TileGrid

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200, 720))
    clock = pygame.time.Clock()
    running = True

    # Game setup
    tiles = []
    tiles_remaining = 0
    game_difficulty = 100

    game_init()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        game_loop()
        game_draw(screen)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

# Setup the grid of the game and assign states to tiles
def game_init():
    global tile_grid
    tile_grid = TileGrid(30, 30, 20, 0.01)
    tile_grid.build_grid()

def game_loop():
    pass

def game_draw(screen):
    tile_grid.draw_grid(screen)

if __name__ == '__main__':
    main()

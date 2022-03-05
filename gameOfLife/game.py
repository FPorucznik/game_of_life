import pygame
from grid import Grid

BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
GREY_COLOR = (114, 114, 114)
WINDOW_SIZE = [800, 800]
MARGIN = 2
CELL_SIZE = 6


class Game():
    def __init__(self, size):
        pygame.init()
        self.size = size
        self.color = BLACK_COLOR
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.grid = Grid(self.size)
        self.finished = False
        self.ready = False
        pygame.display.set_caption('Game of life')

    def draw_grid(self):
        for row in range(self.size):
            for col in range(self.size):
                self.color = BLACK_COLOR
                if self.grid.state[row][col] == 1:
                    self.color = WHITE_COLOR
                pygame.draw.rect(self.screen, self.color,
                                 [(MARGIN + CELL_SIZE) * col + MARGIN,
                                  (MARGIN + CELL_SIZE) * row + MARGIN,
                                     CELL_SIZE, CELL_SIZE
                                  ])

    def run(self):
        while not self.finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    col = mouse_pos[0] // (CELL_SIZE + MARGIN)
                    row = mouse_pos[1] // (CELL_SIZE + MARGIN)

                    self.grid.state[row][col] = 1
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.ready:
                            self.ready = False
                        else:
                            self.ready = True
                    if event.key == pygame.K_BACKSPACE:
                        if self.ready:
                            self.ready = False
                            self.grid.state = self.grid.generate_empty_state()
                        else:
                            self.ready = True

            self.screen.fill(GREY_COLOR)
            if self.ready:
                self.grid.update()
            self.draw_grid()

            self.clock.tick(120)
            pygame.display.flip()

        pygame.quit()


game = Game(100)
game.run()

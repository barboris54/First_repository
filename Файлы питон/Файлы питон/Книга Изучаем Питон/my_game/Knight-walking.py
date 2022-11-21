import sys
import pygame
from Kinght import Knight1

class KnightWalking:
    """Класс управляющий ресурсвми игры"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Knight walking')
        self.knight = Knight1(self)
        self.bg_colour = (255, 255, 255)




    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.knight.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.knight.moving_left = True
                    elif event.key == pygame.K_UP:
                        self.knight.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        self.knight.moving_down = True


                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.knight.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.knight.moving_left = False
                    elif event.key == pygame.K_UP:
                        self.knight.moving_up = False
                    elif event.key == pygame.K_DOWN:
                        self.knight.moving_down = False



            pygame.display.flip()
            self.screen.fill(self.bg_colour)
            self.knight.blitme()
            self.knight.update()


if __name__ == '__main__':
    kw = KnightWalking()
    kw.run_game()
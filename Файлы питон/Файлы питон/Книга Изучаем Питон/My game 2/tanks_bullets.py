import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """класс для управления снарядами"""

    def __init__(self, ts_game):
        super().__init__()
        self.bullet_speed = 1
        self.bullet_height = 3
        self.bullet_width = 15
        self.bullet_colour = (60, 60, 60)
        self.screen = ts_game.screen
        self.colour = self.bullet_colour

        # Создание снаряда в позиции 0,0 и назначение правильной позции
        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midright = ts_game.tank.rect.midright

        # позиция снаряда хранится в вещественном формате
        self.x = float(self.rect.x)

    def update(self):
        """перемещает снаряд вправо"""
        self.x += self.bullet_speed

        # обновление поизиции прямоугольника
        self.rect.x = self.x

    def draw_bullet(self):
        """вывод снаряда на экран"""
        pygame.draw.rect(self.screen,self.bullet_colour,self.rect)
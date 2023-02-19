import pygame
from pygame.sprite import Sprite



class Bullet(Sprite):
    """Класс управления срнарядами выпущенными кораблем"""

    def __init__(self, ai_game):
        """Создает оюъект снаряда в текущем положении корабля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colour = self.settings.bullet_colour

        # Создание снаряда в точке (0,0) и назначение правильной позиции
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Позиция хранится в вещественном формате
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение снаряда в верх по экрану"""
        # обновление позиции снаряда в вещественном формате
        self.y -= self.settings.bullet_speed

        # обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод снаряда на экран"""
        pygame.draw.rect(self.screen, self.colour, self.rect)

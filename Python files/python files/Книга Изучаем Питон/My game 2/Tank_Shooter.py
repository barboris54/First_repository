import pygame
import sys
from tank import Tank
from tanks_bullets import Bullet


class TankShooter:
    """Класс управляет ресурсами игры"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption("Tank Shooter")
        self.bg_colour = (0, 0, 0)
        self.tank = Tank(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._update_screen()
            self._check_events()
            self.tank.update()
            self._update_bulles()

    def _update_bulles(self):
        """обновляет позицию снарядов и уничтожает старые снаряды"""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.right >= 1200:
                self.bullets.remove(bullet)


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагируте на нажитие клавиш"""
        if event.key == pygame.K_UP:
            self.tank.moving_up = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        if event.key == pygame.K_DOWN:
            self.tank.moving_down = True

    def _check_keyup_events(self, event):
        """Реагирует на поднятие клавиш"""
        if event.key == pygame.K_UP:
            self.tank.moving_up = False
        if event.key == pygame.K_DOWN:
            self.tank.moving_down = False

    def _fire_bullet(self):
        """создание нового снаряда и добваление его в группу bullets"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Обновляет экран"""
        self.screen.fill(self.bg_colour)
        self.tank.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    ts = TankShooter()
    ts.run_game()

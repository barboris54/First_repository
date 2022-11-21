import sys
import pygame
from pygame.sprite import Sprite

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Класс упавляющий ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((1200, 800))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Запуск основнаого цикла игры"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._check_fleet_edges()

    def _create_fleet(self):
        """Созддание флота пришельцев"""
        # Создание пришельца и вычисление количества пришельцев в ряду
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        aviable_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = aviable_space_x // (2 * alien_width)
        """Определяет количество рядов помащающихся на экране"""
        ship_height = self.ship.rect.height
        aviable_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = aviable_space_y// (2 * alien_height)

        # создание флота пришельцев
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """ Создание пришельца и размещение его в ряду"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев во флоте"""
        self.aliens.update()

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана."""
        for alien in self.aliens:
            if alien.check_edges():
                print(True)
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот вниз и меняет направление"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
            self.settings.fleet_direction *= -1

    def _update_bullets(self):
        """Обновляет позицию снарядов на экране и убирает старые снаряды"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        """Проверяет колизию снарядов и пришельцев"""
        collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)


    def _check_events(self):
        """Обрабатывает нажатие клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """реагирует на нажатие клавиш """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу Bullet"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bulet = Bullet(self)
            self.bullets.add(new_bulet)

    def _check_keyup_events(self, event):
        """реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Отображает изображение на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()

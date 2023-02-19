class Settings():
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параментры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (0, 51, 102)
        self.bullets_allowed = 3

        # Параментры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (254, 32, 32)

        # Настойки корабля
        self.ship_speed = 1.5

        # Настройка пришельцев
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

import pygame

class Tank:
    """инициирует класс Танк"""
    def __init__(self,ts_game):
        self.screen = ts_game.screen
        self.screen_rect = ts_game.screen.get_rect()

        self.image = pygame.image.load('images/Tank1.png')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        # Флаг движения танка
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Меняет расположение танка"""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1



    def blitme(self):
        """Отображает танк на экране"""
        self.screen.blit(self.image,self.rect)
import pygame

class Knight1:
    """Инициирует класс рыцарь"""
    def __init__(self, kw_game):
        self.screen = kw_game.screen
        self.screen_rect = kw_game.screen.get_rect()


        self.image = pygame.image.load('images/pixel-character-mage-for-games-and-web-sites-400-108018221.jpg')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False




    def update(self):
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
        if self.moving_up:
            self.rect.y -= 1
        if self.moving_down:
            self.rect.y += 1


    def blitme(self):
        self.screen.blit(self.image,self.rect)
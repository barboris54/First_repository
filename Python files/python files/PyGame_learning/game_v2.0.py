import pygame
import sys
from random import randint

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pixel Runner')
clock = pygame.time.Clock()
players_gravity = 0
game_active = False
tfont = pygame.font.Font(None, 60)
start_time = 0
score = 0






def display_score():
    """Отображает текущий счет очков в игре"""
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = tfont.render(f'Your score: {current_time}', False, (205, 92, 92))
    score_rect = score_surf.get_rect(center=(400, 100))
    screen.blit(score_surf, score_rect)

    return current_time


def obstacle_movement(obstacle_list):
    """Спавнит и двигает противников в лево"""
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 4

            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > 800]

            screen.blit(enemy_surface, obstacle_rect)
    else:
        return []


def collions(player, obstacle):
    """Если игрок сталкивается с препятствием игра заканчиается"""
    if obstacle:
        for obstacle_rect in obstacle:
            if player.colliderect(obstacle_rect):
                return False
    return True

def enemy_animations():
    global enemy_index, enemy_surface
    enemy_index += 0.1
    if enemy_index > len(enemy_walk_list):
        enemy_index = 0
    enemy_surface = enemy_walk_list[int(enemy_index)]

def player_animation():
    global player_index, player_surf
    player_index += 0.1
    if player_index >= len(player_walk_list):
        player_index = 0
    player_surf = player_walk_list[int(player_index)]


sky_surf = pygame.image.load('images/1625587282_33-kartinkin-com-p-pikselnii-fon-nebo-krasivie-foni-34.jpg')

player_walk_1 = pygame.image.load('images/player.png').convert_alpha()
player_walk_2 = pygame.image.load('images/player-walk.png').convert_alpha()
player_walk_list = [player_walk_1,player_walk_2]
player_index = 0
player_surf = player_walk_list[player_index]
player_rect = player_surf.get_rect(midbottom=(100, 385))

enemy_surf = pygame.image.load('images/Enemy_1.png').convert_alpha()
enemy_surf_1 = pygame.image.load('images/Enemy_walk_1.png').convert_alpha()
enemy_surf_2 = pygame.image.load('images/Enemy_walk_2.png').convert_alpha()
enemy_surf_3 = pygame.image.load('images/Enemy_walk_3.png').convert_alpha()
enemy_surf_4 = pygame.image.load('images/Enemy_walk_4.png').convert_alpha()
enemy_surf_5 = pygame.image.load('images/Enemy_walk_5.png').convert_alpha()
enemy_surf_6 = pygame.image.load('images/Enemy_walk_6.png').convert_alpha()
enemy_surf = pygame.transform.flip(enemy_surf, True, False).convert_alpha()
enemy_surf_1 = pygame.transform.flip(enemy_surf_1,True,False).convert_alpha()
enemy_surf_2 = pygame.transform.flip(enemy_surf_2,True,False).convert_alpha()
enemy_surf_3 = pygame.transform.flip(enemy_surf_3,True,False).convert_alpha()
enemy_surf_4 = pygame.transform.flip(enemy_surf_4,True,False).convert_alpha()
enemy_surf_5 = pygame.transform.flip(enemy_surf_5,True,False).convert_alpha()
enemy_surf_6 = pygame.transform.flip(enemy_surf_6,True,False).convert_alpha()
enemy_walk_list = [enemy_surf,enemy_surf_1, enemy_surf_2, enemy_surf_3, enemy_surf_4, enemy_surf_5, enemy_surf_6]
enemy_index = 0
enemy_surface = enemy_walk_list[enemy_index]
enemy_surf = pygame.transform.flip(enemy_surf, True, False).convert_alpha()

menu_surf = pygame.image.load('images/1625587305_25-kartinkin-com-p-pikselnii-fon-nebo-krasivie-foni-26.png')
menu_text_1 = tfont.render('Press SPACE to start !!!', False, (64, 64, 64))
text_rect_1 = menu_text_1.get_rect(center=(400, 100))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1200)

# Obstacle
obstacle_rect_list = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 385:
                    players_gravity = -20
            if event.type == obstacle_timer:
                obstacle_rect_list.append(enemy_surface.get_rect(midbottom=(randint(850, 1000), 385)))
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        players_gravity += 1
        player_rect.y += players_gravity
        if player_rect.bottom >= 385: player_rect.bottom = 385
        screen.blit(sky_surf, (-300, -470))
        player_animation()
        enemy_animations()
        screen.blit(player_surf, player_rect)
        obstacle_movement(obstacle_rect_list)
        game_active = collions(player_rect, obstacle_rect_list)
        display_score()


    else:
        screen.blit(menu_surf, (0, 0))
        screen.blit(menu_text_1, text_rect_1)
        obstacle_rect_list.clear()

    pygame.display.update()
    clock.tick(60)

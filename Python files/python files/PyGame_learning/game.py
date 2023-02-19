import pygame
from sys import exit
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f' Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x += 4

            obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x < 800]
            if obstacle_rect.bottom == 350:
                screen.blit(character_surface, obstacle_rect)
            else:
                screen.blit(fly_surf,obstacle_rect)
        return obstacle_list
    else:
        return []

def collisions (player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):return False
    return True

def player_animation():
    global player_index, player_surface
    player_index += 0.1
    if player_index >= len(player_walk):
        player_index = 0
    player_surface = player_walk[int(player_index)]


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load(
    'images/1625587305_25-kartinkin-com-p-pikselnii-fon-nebo-krasivie-foni-26.png').convert()
ground_surface = pygame.image.load('images/ground.png').convert_alpha()

# test_surface = test_font.render('My game', False, (64,64,64))
# test_rect = test_surface.get_rect(center=(400,50))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

# Obstacles
character_surface = pygame.image.load('images/Enemy_1.png').convert_alpha()
fly_surf = pygame.image.load('images/Fly1.png').convert_alpha()

obstacle_rect_list = []

player_walk_1 = pygame.image.load('images/player.png').convert_alpha()
player_walk_2 = pygame.image.load('images/player-walk.png').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom=(200, 350))

player_stand = pygame.image.load('images/player.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

text_menu_surf = test_font.render('Runner', False, (64, 64, 64))
text_menu_rect = text_menu_surf.get_rect(center=(400, 100))
players_gravity = 0

text_menu_surf_2 = test_font.render('Press SPACE to start', False, (64, 64, 64))
text_menu_rect_2 = text_menu_surf_2.get_rect(center=(400, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 350:
                    players_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 350:
                    players_gravity = -20
        if game_active is False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)
        if event.type == obstacle_timer and game_active:
           if randint(0,2):
                obstacle_rect_list.append(character_surface.get_rect(midbottom=(randint(-200, 0), 350)))
           else:
                obstacle_rect_list.append(fly_surf.get_rect(midbottom=(randint(-200, 0), 210)))

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 350))
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        game_active = collisions(player_rect,obstacle_rect_list)
        # pygame.draw.rect(screen,'#c0e8ec',test_rect)
        # pygame.draw.ellipse(screen,'Blue',pygame.Rect(100,100,70,70))
        #screen.blit(test_surface, test_rect)
        #screen.blit(character_surface, character_rect)
        # character_rect.x += 4
        #if character_rect.x >= 800:
            #character_rect.x = 0
        players_gravity += 1
        player_rect.y += players_gravity
        if player_rect.bottom >= 350: player_rect.bottom = 350
        player_animation()
        screen.blit(player_surface, player_rect)
        score = display_score()
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        # print('jump')

        #game_active = collision(player_rect,obstacle_rect_list)
        #if player_rect.colliderect(obstacle_rect):
            #game_active = False
    else:
        screen.fill((94, 129, 162))
        score_message = test_font.render(f'Your score: {score}', False, (64, 64, 64))
        score_message_rect = score_message.get_rect(center=(400, 300))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(text_menu_surf, text_menu_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (200,350)
        players_gravity = 0
        if score == 0:
            screen.blit(text_menu_surf_2, text_menu_rect_2)
        else:
            screen.blit(score_message, score_message_rect)


    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    # print(pygame.mouse.get_pressed())
    pygame.display.update()
    clock.tick(60)

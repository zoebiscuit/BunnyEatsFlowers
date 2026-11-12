import pygame
import random

pygame.init()


#game window

def collision_detection():
        return (player_x <= (falling_object_x + falling_object.get_width()) and (player_x + player.get_width()) >= falling_object_x and player_y <= (falling_object_y + falling_object.get_height() + 5) and (player_y + player.get_height()) >= falling_object_y)

window = pygame.display.set_mode((400,400))
window.fill((255,255,255))
pygame.display.set_caption("write your caption here!")

background = pygame.image.load("3.png").convert_alpha()
background = pygame.transform.scale(background, (400,400))

player = pygame.surface.Surface((100,100))
player.fill((0,0,0))
player_x = 0
player_y = 300
player_vel_x = 0
player_vel_y = 0
player = pygame.image.load("1.png").convert_alpha()
player = pygame.transform.scale(player, (100,100))

falling_object = pygame.image.load("2.png").convert_alpha()
falling_object = pygame.transform.scale(falling_object, (75,75))
falling_object_x = 0
falling_object_y = 0
falling_object_vel_x = 0
falling_object_vel_y = .40

total_points = 0
text_surface = pygame.font.SysFont(None, 50)
actual_text = text_surface.render("Points " + str(total_points), True, (0,0,0))
pos_text = (230,0)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(0)
            
    if collision_detection():
        falling_object_y = 0
        falling_object_x = random.randint(0, window.get_width()-50)
        total_points = -1
        
    if falling_object_y >= window.get_height():
        falling_object_y = 0
        falling_object_x = random.randint(0, window.get_width()-50)
        total_points += 1
        actual_text = text_surface.render("Points: " + str(total_points), True, (0,0,0))
            
    if event.type == pygame.KEYDOWN and total_points != -1:
        if event.key == pygame.K_LEFT:
            player_vel_x = -0.9
        if event.key == pygame.K_RIGHT:
            player_vel_x = 0.9
    else:
        player_vel_x = 0
        player_vel_y = 0
        
    if total_points == -1:
        player_vel_x = 0
        player_vel_y = 0
        falling_object_vel_y = 0
        falling_object_y = -200
        player_y = -200
        actual_text = text_surface.render("GAME OVER", True, (255,0,0))
        pos_text = (100,150)
        
        
    window.fill((255,255,255))
    
    player_x += player_vel_x
    player_y += player_vel_y
    
    falling_object_x += falling_object_vel_x
    falling_object_y += falling_object_vel_y
    
    
    text = actual_text
    
    window.blit(background,(0,0))
    window.blit(player,(player_x, player_y))
    window.blit(falling_object,(falling_object_x,falling_object_y))
    window.blit(text,pos_text)
    
    
    pygame.display.flip()
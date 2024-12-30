import pygame
from os.path import join
from random import randint

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

def main():
    pygame.init()
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Space Shooter")
    
    clock = pygame.time.Clock()
    running = True
    
   
    player_surf = pygame.image.load(join('images', 'player.png')).convert_alpha()
    player_rect = player_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
    player_speed = 300
    player_direction = pygame.math.Vector2(0,0)
    
    star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
    star_pos_list = [(randint(0,WINDOW_WIDTH), randint(0,WINDOW_HEIGHT)) for i in range(20)]
    
    meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
    meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
    
    laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
    laser_rect = laser_surf.get_frect(bottomleft=(20,WINDOW_HEIGHT - 20))
    
    
    
    # event loop
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_direction.x += 1
        elif keys[pygame.K_ESCAPE]:
            running = False
                
        display_surface.fill("darkgrey")
        
        for pos in star_pos_list:
            display_surface.blit(star_surf, pos)
            
        display_surface.blit(meteor_surf, meteor_rect)
        display_surface.blit(laser_surf, laser_rect)
        display_surface.blit(player_surf, player_rect)
           
        pygame.display.update()

if __name__ == "__main__": 
    main()
    pygame.quit()
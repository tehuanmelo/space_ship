import pygame
from os.path import join
from random import randint

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.speed = 300
        self.direction = pygame.math.Vector2()
        
        # laser delay
        self.laser_can_shoot = True
        self.laser_shoot_time = 0
        self.laser_shoot_delay = 400
        
    def laser_delay(self):
        if not self.laser_can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.laser_shoot_delay:
                self.laser_can_shoot = True
        
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt
        
        keys_pressed = pygame.key.get_just_pressed()
        if keys_pressed[pygame.K_SPACE] and self.laser_can_shoot:
                print("Laser fired")
                self.laser_can_shoot = False
                self.laser_shoot_time = pygame.time.get_ticks()
                
        self.laser_delay()

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))
    


        

def main():
    
    pygame.init()
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Space Shooter")
    
    clock = pygame.time.Clock()
    running = True
    all_sprites = pygame.sprite.Group()
    star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
    stars = [Star(all_sprites, star_surf) for i in range(20)]
    player = Player(all_sprites)
    
    meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
    meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
    
    laser_surf = pygame.image.load(join('images', 'laser.png')).convert_alpha()
    laser_rect = laser_surf.get_frect(bottomleft=(20,WINDOW_HEIGHT - 20))
    
    
    # event loop
    while running:
        dt = clock.tick() / 1000
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or 
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                running = False
                
        all_sprites.update(dt)  

        # Drawing sprites    
        display_surface.fill("darkgrey")
       
        display_surface.blit(meteor_surf, meteor_rect)
        display_surface.blit(laser_surf, laser_rect)
        all_sprites.draw(display_surface)
           
        pygame.display.update()

if __name__ == "__main__": 
    main()
    pygame.quit()
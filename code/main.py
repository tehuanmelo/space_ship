import pygame
from os.path import join
from random import randint, uniform

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.speed = 400
        self.direction = pygame.math.Vector2()
        self.sprite_groups = groups
        self.laser_image = pygame.image.load(join('images', 'laser.png')).convert_alpha()
        print(self.direction)
        
        # laser delay
        self.laser_can_shoot = True
        self.laser_shoot_time = 0
        self.laser_shoot_delay = 300
        
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
        new_position = self.rect.center + self.direction * self.speed * dt
        if (not (new_position.x > WINDOW_WIDTH or new_position.x < 0
            or new_position.y > WINDOW_HEIGHT or new_position.y < 0)):
            self.rect.center = new_position
        # self.rect.center += self.direction * self.speed * dt
        
        keys_pressed = pygame.key.get_just_pressed()
        if keys_pressed[pygame.K_SPACE] and self.laser_can_shoot:
                Laser(self.sprite_groups, self.laser_image, self.rect.midtop)
                self.laser_can_shoot = False
                self.laser_shoot_time = pygame.time.get_ticks()
                
        self.laser_delay()

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))
 
class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, surf, pos):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom=pos)  
        self.speed = 500
         
    def update(self, dt):
        self.rect.centery -= self.speed * dt
        if self.rect.bottom < 0:
            self.kill()

class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups, surf, pos):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=(pos))
        self.creation_time = pygame.time.get_ticks()
        self.destroy_time = 3000
        self.direction = pygame.Vector2(uniform(-.5,.5),1)
        self.meteor_speed = randint(300, 500)
        
    def update(self, dt):
        self.rect.center += self.direction * self.meteor_speed * dt
        current_time = pygame.time.get_ticks()
        if current_time - self.creation_time >= self.destroy_time:
            self.kill()
        

def main():
    
    # Game setup
    pygame.init()
    display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Space Shooter")
    clock = pygame.time.Clock()
    running = True
    
    # Imports
    star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
    meteor_surf = pygame.image.load(join('images', 'meteor.png')).convert_alpha()
    
    # Sprites
    all_sprites = pygame.sprite.Group()
    stars = [Star(all_sprites, star_surf) for i in range(20)]
    player = Player(all_sprites)
    
    meteor_event = pygame.event.custom_type()
    pygame.time.set_timer(meteor_event, 500)
    
    
    # event loop
    while running:
        dt = clock.tick() / 1000
        # print(dt)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or 
                (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                running = False
            if event.type == meteor_event:
                x, y = randint(0,WINDOW_WIDTH), 0
                Meteor(all_sprites, meteor_surf, (x,y))

        # Drawing sprites    
        all_sprites.update(dt)  
        display_surface.fill("darkgrey")
        all_sprites.draw(display_surface)
           
        pygame.display.update()

if __name__ == "__main__": 
    main()
    pygame.quit()
import pygame
from pygame.sprite import Sprite, AbstractGroup

class Player(Sprite):
    def __init__(self, x, y, *groups: AbstractGroup) -> None:
        super().__init__(*groups)
        
        self.image = pygame.Surface((50, 50))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5
        self.velocity = pygame.Vector2(0, 0)
        self.gravity = 0.5

        self.jump = False

        self.height_jump = 0 
        
        self.zac = False
    def update(self, keys, walls):
        
        if not self.jump and not self.zac:
            self.velocity.y += self.gravity
            self.rect.y += self.velocity.y

        
        platform_collision = pygame.sprite.spritecollideany(self, walls)
        if platform_collision:
            
            # Если есть столкновение, корректируем позицию игрока
            if self.velocity.y > 0:  # Если игрок движется вниз (падает)
                self.rect.bottom = platform_collision.rect.top 
                self.velocity.y = 0
                
            elif self.velocity.y < 0:  # Если игрок движется вверх (прыгает)
                
                self.jump = False
                self.rect.top = platform_collision.rect.bottom
                self.velocity.y = 0

        
        
        if platform_collision and keys[pygame.K_SPACE] and not self.jump and self.rect.bottom == platform_collision.rect.top:
            self.jump = True
            self.height_jump = platform_collision.rect.top - 150 
        
        
        
        
        if self.jump and self.rect.top > self.height_jump:
            self.velocity.y-=self.gravity
            self.rect.y -= 10

        elif self.jump and self.rect.top <= self.height_jump:
            self.jump = False
            

        dx = 0
        


        if keys[pygame.K_a]:
            dx = -self.speed
        if keys[pygame.K_d]:
            dx = self.speed

        self.rect.x += dx

        

        # Проверяем столкновение с боковыми стенами
        if pygame.sprite.spritecollideany(self, walls):
            
            if keys[pygame.K_SPACE]:
                self.jump = True
                self.height_jump = self.rect.y - 150
            if (keys[pygame.K_a] or keys[pygame.K_d]):
                self.zac = True
                
            self.rect.x -= dx
        else:
            self.zac = False
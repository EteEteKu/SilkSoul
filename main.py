import pygame 
from entity.player import Player
from objects.test_wall import Wall

class Game:
    def __init__(self) -> None:
        pygame.init()


        self.WIDTH = 800
        self.HEIGHT = 800
        self.game_run = True
        self.FPS = 60

        self.screen =  pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()

        

        
        #sprites group
        self.all_sprites = pygame.sprite.Group()
        self.collision_objects = pygame.sprite.Group()

        #sprites
        self.player = Player(150,400, self.all_sprites)

        self.flour = Wall(800,30,0,500, self.all_sprites, self.collision_objects)
        
        self.wall1 = Wall(20, 300, 300,100, self.all_sprites, self.collision_objects)
        self.wall2 = Wall(20, 300, 100,200, self.all_sprites, self.collision_objects)
        self.wall3 = Wall(60, 20, 400,350, self.all_sprites, self.collision_objects)
        self.wall4 = Wall(60, 20, 600,350, self.all_sprites, self.collision_objects)


    def update_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_run = False

        keys = pygame.key.get_pressed()
        self.player.update(keys, self.collision_objects)
        

    def game_loop(self):
        while self.game_run:
            self.update_game()
            self.render_game()
    def render_game(self):
        self.screen.fill((12,32,43)) 

        self.all_sprites.draw(self.screen)
        pygame.display.flip()


        self.clock.tick(self.FPS)


if __name__=="__main__":
    game = Game()
    game.game_loop()
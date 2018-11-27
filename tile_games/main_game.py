# Import needed modules
import pygame
import random
from settings import *
from Sprites import *

class Game(object):
    def __init__(self):
        # init game window, etc
        pygame.init()
        pygame.mixer.init()
        # set the display size to our game constants and set to variable
        self.screen = pygame.display.set_mode((width,height))
        # set window title (name that opens on top bar of window)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        # start a new game/ replay
        self.all_sprites = pygame.sprite.Group()
        self.run()
        self.player = Player(self, 0,0)
        
    
    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(fps)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            
    def draw_grid(self):
        for x in range(0,width, tilesize):
            pygame.draw.line(self.screen, lightgrey,(x,0), (x,height))
        for y in range(0,height, tilesize):
            pygame.draw.line(self.screen, lightgrey, (0,y), (width,y)) 
    
    def draw(self):
        # game loop draw
        self.screen.fill(bgcolor)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def show_start_screen(self):
        # show start screen duh
        pass
    
    def show_go_screen(self):
        # show game over screen
        pass

game = Game()
game.show_start_screen()

while game.running:
    game.new()
    game.show_go_screen()

pygame.quit()
    
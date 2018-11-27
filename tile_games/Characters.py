import pygame
from settings import *
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, game, x, y):
        # print "init running"
        # self.groups = game.all_sprites
        super(Player, self).__init__(self)
        # print "super ran"
        self.game = game
        self.image = pygame.Surface((tilesize,tilesize))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def update(self):
        self.rect.x = self.x * tilesize
        self.rect.y = self.y * tilesize
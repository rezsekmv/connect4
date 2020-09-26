import pygame

class Player:

    def __init__(self, id, color):
        self.id = id
        self.color = color

    def move(self, column, game):
        return game.place(self, column)

    def draw(self, win, xy, r):
        pygame.draw.circle(win, self.color, xy, r)


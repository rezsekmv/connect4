class Player:

    def __init__(self, id, color=None):
        self.id = id
        self.color = color

    def move(self, column, game):
        return game.place(self, column)

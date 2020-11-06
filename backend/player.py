class Player:

    def __init__(self, id, color=None):
        self.id = id
        self.color = color

    def move(self, column, game):
        return game.place(self, column)

    def __str__(self):
        return "{type} {id} {color}".format(type=type(self), id=self.id, color=self.color)
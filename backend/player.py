class Player:

    def __init__(self, id):
        self.id = id

    def move(self, column, game):
        return game.place(self, column)

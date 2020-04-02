import pyxel

class Game:
    def __init__(self):
        pyxel.init(100, 100)
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pass

Game()
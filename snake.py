import pyxel

#direcoes da cobra
CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

class Game:
    def __init__(self):
      pyxel.init(208, 208)
      self.x = pyxel.width/2
      self.y = pyxel.height/2
      self.direcao = DIREITA
      self.tamanho_sprite = 8
      pyxel.run(self.update, self.draw)

    def update(self):
      #atualiza a direção atual de acordo com entrada do usuario
      if pyxel.btn(pyxel.KEY_UP) and self.direcao != BAIXO:
        self.direcao = CIMA
      elif pyxel.btn(pyxel.KEY_RIGHT) and self.direcao != ESQUERDA:
        self.direcao = DIREITA
      elif pyxel.btn(pyxel.KEY_DOWN) and self.direcao != CIMA:
        self.direcao = BAIXO
      elif pyxel.btn(pyxel.KEY_LEFT) and self.direcao != DIREITA:
        self.direcao = ESQUERDA

      if pyxel.frame_count % 15 == 0:
        if self.direcao == CIMA:
            if self.y - self.tamanho_sprite < 0:
                self.y =  pyxel.height - self.tamanho_sprite
            else:
                self.y -= 8
        elif self.direcao == DIREITA:
            if self.x + self.tamanho_sprite > pyxel.width - self.tamanho_sprite:
                self.x = 0
            else:
                self.x += 8
        elif self.direcao == BAIXO:
            if self.y + self.tamanho_sprite > pyxel.height - self.tamanho_sprite:
                self.y = 0
            else:
                self.y += 8
        elif self.direcao == ESQUERDA:
            if self.x - self.tamanho_sprite < 0:
                self.x = pyxel.width - self.tamanho_sprite
            else:
                self.x -= 8

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, self.tamanho_sprite, self.tamanho_sprite, 7)

Game()

import pyxel

#direcoes da cobra
CIMA = 0
DIREITA = 1
BAIXO = 2
ESQUERDA = 3

class Posicao:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Game:
    def __init__(self):
        pyxel.init(208, 208)
        self.tamanho_sprite = 8
        self.segmentos = []
        cabeca = Posicao(pyxel.width/2, pyxel.height/2)
        self.segmentos.append(cabeca)
        self.segmentos.append(Posicao(pyxel.width/2 - self.tamanho_sprite, pyxel.height/2))
        self.segmentos.append(Posicao(pyxel.width/2 - self.tamanho_sprite*2, pyxel.height/2))
        self.segmentos.append(Posicao(pyxel.width/2 - self.tamanho_sprite*3, pyxel.height/2))
        self.segmentos.append(Posicao(pyxel.width/2 - self.tamanho_sprite*4, pyxel.height/2))
        self.segmentos.append(Posicao(pyxel.width/2 - self.tamanho_sprite*5, pyxel.height/2))
        self.direcao = DIREITA
        pyxel.run(self.update, self.draw)

    def update(self):
        # atualiza a direção atual de acordo com entrada do usuario
        if pyxel.btn(pyxel.KEY_UP) and self.direcao != BAIXO:
            self.direcao = CIMA
        elif pyxel.btn(pyxel.KEY_RIGHT) and self.direcao != ESQUERDA:
            self.direcao = DIREITA
        elif pyxel.btn(pyxel.KEY_DOWN) and self.direcao != CIMA:
            self.direcao = BAIXO
        elif pyxel.btn(pyxel.KEY_LEFT) and self.direcao != DIREITA:
            self.direcao = ESQUERDA

        if pyxel.frame_count % 5 == 0:
            # adicionar uma nova cabeca e remover a cauda eh mais facil
            # do que atualizar todos os segmentos
            cabeca = self.segmentos[0]

            if self.direcao == CIMA:
                if cabeca.y - self.tamanho_sprite < 0: #fazer o wrap
                    cabeca = Posicao(cabeca.x, pyxel.height - self.tamanho_sprite)
                else:
                    cabeca = Posicao(cabeca.x, cabeca.y - self.tamanho_sprite)
            elif self.direcao == DIREITA:
                if cabeca.x + self.tamanho_sprite > pyxel.width - self.tamanho_sprite:
                    cabeca = Posicao(0, cabeca.y)
                else:
                    cabeca = Posicao(cabeca.x + self.tamanho_sprite, cabeca.y)
            elif self.direcao == BAIXO:
                if cabeca.y + self.tamanho_sprite > pyxel.height - self.tamanho_sprite:
                    cabeca = Posicao(cabeca.x, 0)
                else:
                    cabeca = Posicao(cabeca.x, cabeca.y + self.tamanho_sprite)
            elif self.direcao == ESQUERDA:
                if cabeca.x - self.tamanho_sprite < 0:
                    cabeca = Posicao(pyxel.width - self.tamanho_sprite, cabeca.y)
                else:
                    cabeca = Posicao(cabeca.x - self.tamanho_sprite, cabeca.y)

            self.segmentos.pop()
            self.segmentos.insert(0, cabeca)


    def draw(self):
        pyxel.cls(0)
        for segmento in self.segmentos:
            pyxel.rectb(segmento.x, segmento.y, self.tamanho_sprite, self.tamanho_sprite, 7)

Game()

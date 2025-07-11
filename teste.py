import arcade
import random

# Constantes da tela
LARGURA_TELA = 800
ALTURA_TELA = 600
TITULO = "Jogo com Colisão"
VELOCIDADE = 5

class Jogador(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", 0.5)
        self.center_x = 100
        self.center_y = 100
        self.change_x = 0
        self.change_y = 0

    def update(self, delta_time: float = 1/60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Impede que o jogador saia da tela
        if self.left < 0:
            self.left = 0
        if self.right > LARGURA_TELA:
            self.right = LARGURA_TELA
        if self.bottom < 0:
            self.bottom = 0
        if self.top > ALTURA_TELA:
            self.top = ALTURA_TELA

class Inimigo(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/animated_characters/zombie/zombie_idle.png", 0.5)
        self.center_x = random.randint(100, LARGURA_TELA - 100)
        self.center_y = random.randint(100, ALTURA_TELA - 100)

class Jogo(arcade.Window):
    def __init__(self):
        super().__init__(LARGURA_TELA, ALTURA_TELA, TITULO)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.jogador = Jogador()
        self.inimigo = Inimigo()
        self.pontuacao = 0

        # Lista de sprites
        self.lista_sprites = arcade.SpriteList()
        self.lista_sprites.append(self.jogador)
        self.lista_sprites.append(self.inimigo)

    def on_draw(self):
        self.clear()
        self.lista_sprites.draw()
        arcade.draw_text(f"Pontuação: {self.pontuacao}", 10, ALTURA_TELA - 30, arcade.color.BLACK, 20)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.jogador.change_x = -VELOCIDADE
        elif key == arcade.key.RIGHT:
            self.jogador.change_x = VELOCIDADE
        elif key == arcade.key.UP:
            self.jogador.change_y = VELOCIDADE
        elif key == arcade.key.DOWN:
            self.jogador.change_y = -VELOCIDADE

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.jogador.change_x = 0
        elif key in (arcade.key.UP, arcade.key.DOWN):
            self.jogador.change_y = 0

    def on_update(self, delta_time):
        self.lista_sprites.update()
        
        # Verifica colisão entre jogador e inimigo
        if arcade.check_for_collision(self.jogador, self.inimigo):
            self.pontuacao += 1
            print(f"Colisão detectada! Pontuação: {self.pontuacao}")
            # Reposiciona o inimigo em uma nova posição aleatória
            self.inimigo.center_x = random.randint(100, LARGURA_TELA - 100)
            self.inimigo.center_y = random.randint(100, ALTURA_TELA - 100)

# Iniciar o jogo
if __name__ == "__main__":
    jogo = Jogo()
    arcade.run()

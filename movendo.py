import arcade

# Constantes para a janela
LARGURA_TELA = 600
ALTURA_TELA = 400
TITULO = "Movendo um Retângulo"

class Jogo(arcade.Window):
    def __init__(self):
        super().__init__(LARGURA_TELA, ALTURA_TELA, TITULO)
        arcade.set_background_color(arcade.color.BLACK)

        # Posição e velocidade do retângulo
        self.x = 300            # Posição inicial no eixo X
        self.velocidade = 100   # Velocidade em pixels por segundo

    def on_draw(self):
        self.clear()  # Limpa a tela com a cor de fundo
        arcade.draw_lbwh_rectangle_filled(self.x, 200, 50, 50, arcade.color.GREEN)

    def on_update(self, delta_time):
        # Atualiza a posição com base no tempo decorrido
        self.x += self.velocidade * delta_time

        # Inverte a direção ao atingir as bordas da tela
        if self.x > LARGURA_TELA - 25 or self.x < 25:
            self.velocidade *= -1

# Iniciar o jogo
if __name__ == "__main__":
    jogo = Jogo()
    arcade.run()

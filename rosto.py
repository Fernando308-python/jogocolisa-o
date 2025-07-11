import arcade

# Constantes para a janela
LARGURA_TELA = 600
ALTURA_TELA = 400
TITULO = "Rosto Sorridente"

class Jogo(arcade.Window):
    def __init__(self):
        super().__init__(LARGURA_TELA, ALTURA_TELA, TITULO)
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()  # Limpa a tela com a cor de fundo

        # Desenhar o rosto (círculo amarelo)
        arcade.draw_circle_filled(300, 200, 100, arcade.color.YELLOW)

        # Desenhar olhos
        arcade.draw_circle_filled(260, 240, 20, arcade.color.BLACK)
        arcade.draw_circle_filled(340, 240, 20, arcade.color.BLACK)

        # Desenhar boca (arco)
        arcade.draw_arc_outline(300, 160, 80, 60, arcade.color.BLACK, 190, 350, 10)

# Iniciar o jogo
if __name__ == "__main__":
    jogo = Jogo()
    arcade.run()

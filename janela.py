import arcade

# Constantes para a janela
LARGURA_TELA = 600
ALTURA_TELA = 400
TITULO = "Minha Primeira Janela"

# Criando a classe do jogo
class Jogo(arcade.Window):
    def __init__(self):
        super().__init__(LARGURA_TELA, ALTURA_TELA, TITULO)
        arcade.set_background_color(arcade.color.SKY_BLUE)

    def on_draw(self):
        self.clear()  # Limpa a tela com a cor de fundo definida
        # Aqui você pode adicionar outros desenhos

# Iniciar o jogo
if __name__ == "__main__":
    jogo = Jogo()
    arcade.run()

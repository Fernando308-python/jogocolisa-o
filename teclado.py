import arcade

# Constantes da janela
LARGURA_TELA = 600
ALTURA_TELA = 400
TITULO = "Controle de Triângulo por Teclado"

# Velocidade de movimento
VELOCIDADE = 5

class Jogo(arcade.Window):
    def __init__(self):
        super().__init__(LARGURA_TELA, ALTURA_TELA, TITULO)
        arcade.set_background_color(arcade.color.BLACK)

        # Posição inicial do triângulo
        self.x = 300
        self.y = 200

        # Velocidade inicial
        self.vel_x = 0
        self.vel_y = 0

    def on_draw(self):
        # Esta função é chamada automaticamente para desenhar a tela
        self.clear()  # ✅ Substitui start_render() com segurança
        # Define os vértices do triângulo com base na posição atual
        x1 = self.x
        y1 = self.y + 40  # topo
        x2 = self.x - 30
        y2 = self.y - 30
        x3 = self.x + 30
        y3 = self.y - 30

        # Desenha o triângulo
        arcade.draw_triangle_filled(x1, y1, x2, y2, x3, y3, arcade.color.GREEN)

    def on_update(self, delta_time):
        self.x += self.vel_x
        self.y += self.vel_y

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.vel_y = VELOCIDADE
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.vel_y = -VELOCIDADE
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.vel_x = -VELOCIDADE
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.vel_x = VELOCIDADE

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.W, arcade.key.DOWN, arcade.key.S):
            self.vel_y = 0
        if key in (arcade.key.LEFT, arcade.key.A, arcade.key.RIGHT, arcade.key.D):
            self.vel_x = 0

# Executa o jogo
if __name__ == "__main__":
    jogo = Jogo()
    arcade.run()

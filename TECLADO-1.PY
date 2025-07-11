import arcade

LARGURA_TELA = 600
ALTURA_TELA = 400
TITULO = "Controle por Teclado"

class Jogo(arcade.Window):
    def __init__(self):
        super().__init__(LARGURA_TELA, ALTURA_TELA, TITULO)
        arcade.set_background_color(arcade.color.BLACK)
        self.x = 300
        self.y = 200
        self.vel_x = 0
        self.vel_y = 0
        self.tamanho = 50

    def on_draw(self):
        self.clear()  # Limpa a tela

        metade = self.tamanho / 2
        arcade.draw_lrbt_rectangle_filled(
            left=self.x - metade,
            right=self.x + metade,
            bottom=self.y - metade,
            top=self.y + metade,
            color=arcade.color.GREEN
        )

    def on_update(self, delta_time):
        self.x += self.vel_x * delta_time
        self.y += self.vel_y * delta_time

        # Limitar o movimento às bordas
        if self.x < 25:
            self.x = 25
        elif self.x > LARGURA_TELA - 25:
            self.x = LARGURA_TELA - 25
        if self.y < 25:
            self.y = 25
        elif self.y > ALTURA_TELA - 25:
            self.y = ALTURA_TELA - 25

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.vel_y = 200
        elif symbol == arcade.key.DOWN:
            self.vel_y = -200
        elif symbol == arcade.key.LEFT:
            self.vel_x = -200
        elif symbol == arcade.key.RIGHT:
            self.vel_x = 200

    def on_key_release(self, symbol, modifiers):
        if symbol in (arcade.key.UP, arcade.key.DOWN):
            self.vel_y = 0
        if symbol in (arcade.key.LEFT, arcade.key.RIGHT):
            self.vel_x = 0

if __name__ == "__main__":
    jogo = Jogo()
    arcade.run()

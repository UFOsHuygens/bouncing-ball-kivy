from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

kv = '''
GameLayout:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
    AsyncImage:
        source: "https://image.flaticon.com/icons/png/512/2128/2128322.png"
        size_hint: 0.1, 0.1
        id: ball
'''

class GameLayout(FloatLayout):
    pos_x = 5
    pos_y = 1.5

    def __init__(self, **kwargs):
        super(GameLayout, self).__init__(**kwargs)
        Clock.schedule_interval(self.my_callback, 0.001)  # chamada da função callback a cada 0.001 segundos

    def my_callback(self, dt):  # função que movimenta objeto
        self.ids.ball.y += self.pos_y
        self.ids.ball.x += self.pos_x

        if self.ids.ball.x >= self.width - self.ids.ball.width: # colisão da bola com a parede direita
            self.pos_x += -5
        if self.ids.ball.x < 0: # colisão da bola com a parede esquerda
            self.pos_x += 5

        if self.ids.ball.y >= self.height-self.ids.ball.height: # colisão da bola com o teto
            self.pos_y += -1.5
        if self.ids.ball.y < 0: # colisão da bola com o chão
            self.pos_y += 1.5
        
        
class Kivy(App):
    def build(self):
        return Builder.load_string(kv)


Kivy().run()

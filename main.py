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
    Image:
        source: "ball.png"
        size_hint: 0.15, 0.15
        x: 150
        y: 150
        id: ball
    Scatter
        id: obstacle
        x: 150
        size_hint: 0.30, 0.05
        canvas:
            Color:
                rgba: 0, 0, 0, 1
            Rectangle:
                size: self.size
'''

class GameLayout(FloatLayout):
    pos_x = 25
    pos_y = 5

    def __init__(self, **kwargs):
        super(GameLayout, self).__init__(**kwargs)
        Clock.schedule_interval(self.my_callback, 0.001)  # chamada da função callback a cada 0.001 segundos

    def my_callback(self, dt):  # função que movimenta objeto
        ball = self.ids.ball
        obs = self.ids.obstacle
        ball.y += self.pos_y
        ball.x += self.pos_x

        if ball.x >= self.width - ball.width: # colisão da bola com a parede direita
            self.pos_x += -25
        if ball.x < 0: # colisão da bola com a parede esquerda
            self.pos_x += 25

        if ball.y >= self.height - ball.height: # colisão da bola com o teto
            self.pos_y += -5
        if ball.y < 0: # colisão da bola com o chão
            self.pos_y += 5

        
        # colisão com o obstaculo

        if ball.x < obs.x + obs.width and \
            ball.x + ball.width > obs.x and \
                ball.y < obs.y + obs.height and \
                    ball.y + ball.height > obs.y:
                        if ball.x >= obs.x - ball.width:
                            self.pos_x += -(self.pos_x*2)
                        if ball.x == obs.x + obs.width - ball.width:
                            self.pos_x += (self.pos_x*2)
                        if ball.y >= obs.y - ball.height:
                            self.pos_y += -(self.pos_y*2)
                        if ball.y == obs.y + obs.height - ball.height:
                            self.pos_y += (self.pos_y*2)

class Kivy(App):
    def build(self):
        return Builder.load_string(kv)


Kivy().run()

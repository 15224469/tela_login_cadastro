from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image, AsyncImage

class FloatApp(App):
    def build(self):
        Window.clearcolor = (0.97, 0.09, 0.64, 1)  # Cor de fundo em formato RGB

        flo = FloatLayout()
        icon_login = AsyncImage(
            source='https://i.pinimg.com/736x/15/ba/a6/15baa6d2990c29fdab616592ee70e5a2.jpg',
            pos=(590, 680),
            size_hint= (.4, .2)
            )
        flo.add_widget(icon_login)

        
        self.t1 = TextInput (hint_text= 'Login',
                             font_name='Georgia',
                             size_hint=(.2, .05),
                             pos=(780, 580))
        flo.add_widget(self.t1)

        self.t2 = TextInput(hint_text="Senha",
                    font_name='Georgia', 
                    multiline=False, 
                    password=True,
                    size_hint=(.2, .05),
                    pos=(780, 520)
                   )
        flo.add_widget(self.t2)


        b1 = Button(
            text='Entrar', size_hint=(.10, .05),
            pos_hint={'center_x': .5, 'center_y': .45},
            background_color=get_color_from_hex('ff0066'),
            on_press=self.entrar
        )
        b2 = Button(
            text='Cadastrar', size_hint=(.10, .05),
            pos_hint={'center_x': .5, 'center_y': .40},
            background_color=get_color_from_hex('ff0066'),
        )
        b2.bind(on_press=self.ir_para_tela_de_cadastro)
        self.add_widget(b2)

        self.label_cadastrar = Label(
            pos_hint={'center_x': .50, 'center_y': .30},
            color=[1, 1, 1, 1]
        )

    def ir_para_tela_de_cadastr (self, instanse):
        
    
class Cadastro(FloatLayout):
    def __init__(self, **kwargs):
        super(Cadastro, self).__init__(**kwargs)
        self.orientation='horizontal'
        self.spacing=5
        self.padding=[20, 10]
        Window.clearcolor = get_color_from_hex('d0417e') 

        self.label = Label(
            text= 'CADASTRO:', 
            font_size = 40, 
            font_name = 'Georgia',
            size_hint_y=None,
            pos_hint={'x': .013, "y": .8}
            )
        self.add_widget(self.label)

        self.nome = TextInput(
            hint_text="Digite Seu Nome Completo: ",
            size_hint=[.4, .1],
            multiline=False,
            pos_hint= {'x': .3, "y": .7},
            padding_y= [10, 10],
            padding_x= [10, 10],
            background_color=get_color_from_hex('ffdde8'),  
            background_normal='',  
            border=(1, 1, 1, 1)  
        )
        self.add_widget(self.nome)

        self.email = TextInput(
            hint_text="Digite um E-mail Válido: ",
            size_hint=[.4, .1],
            multiline=False,
            pos_hint= {'x': .3, "y": .5},
            padding_y= [10, 10],
            padding_x= [10, 10],
            background_color=get_color_from_hex('ffdde8'),  
            background_normal='',  
            border=(1, 1, 1, 1)  
        )
        self.add_widget(self.email)

        self.celular = TextInput(
            hint_text="Digite Seu Número de telefone: ",
            size_hint=[.4, .1],
            multiline=False,
            pos_hint= {'x': .3, "y": .3},
            padding_y= [10, 10],
            padding_x= [10, 10],
            background_color=get_color_from_hex('ffdde8'),  
            background_normal='',  
            border=(1, 1, 1, 1)  
        )
        self.add_widget(self.celular)

        self.senha = TextInput(
            hint_text="Senha: ",
            password=True,
            size_hint=(.4, .1),
            multiline=False,
            pos_hint= {'x': .3, "y": .1},
            padding_y= [10, 10],
            padding_x= [10, 10],
            background_color=get_color_from_hex('ffdde8'),  
            background_normal='',
            border=(1, 1, 1, 1)  
        )
        self.add_widget(self.senha)

        self.button = Button(
            size_hint = (.1, .05),
            pos_hint = {'x': .6, 'y':.13} ,
            text = 'Ver Senha',
            background_color = get_color_from_hex('ffdde8'),  
            background_normal='', 
            on_press = self.togglevisibility 
        )

        self.button2 = Button(
            size_hint = (.1, .05),
            pos_hint = {'x': .45, 'y':.04} ,
            text = 'Cadastrar',
            background_color = ('ffdde8')
              )
        self.add_widget(self.button2)

        self.add_widget(self.button)

    def togglevisibility(self, instance):
        if self.senha.password == True:
            self.senha.password = False
            self.button.text = 'Hide'   
        else:
            self.senha.password = True
            self.button.text = 'Show'   





class TelaCadastro(App):
    def build(self):
        return Cadastro()

TelaCadastro().run()

FloatApp().run()
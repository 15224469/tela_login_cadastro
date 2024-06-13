from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
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

        l1 = Label(text='Login', size_hint=(.2, .1), pos=(100, 200))
        self.t1 = TextInput(size_hint=(.2, .05), pos=(780, 490))
        flo.add_widget(l1)
        flo.add_widget(self.t1)

        l2 = Label(text="Senha", size_hint=(.2, .1), pos=(100, 200), color="ffa4dd")
        t2 = TextInput(multiline=True, size_hint=(.2, .05), pos=(780, 380))
        flo.add_widget(l2)
        flo.add_widget(t2)

        b1 = Button(
            text='Entrar', size_hint=(.3, .1),
            pos_hint={'center_x': .5, 'center_y': .07},
            on_press=self.entrar
        )
        b2 = Button(
            text='Cadastrar', size_hint=(.3, .1),
            pos_hint={'center_x': .5, 'center_y': .20},
            on_press=self.cadastrar
        )

        self.label_cadastrar = Label(
            pos_hint={'center_x': .50, 'center_y': .30},
            color=[1, 1, 1, 1]
        )

        flo.add_widget(b1)
        flo.add_widget(b2)
        flo.add_widget(self.label_cadastrar)

        return flo

    def cadastrar(self, instance):
        login = self.t1.text
        mensagem = f'O Login {login} foi cadastrado!'
        self.label_cadastrar.text = mensagem

    def entrar(self, instance):
        login = self.t1.text
        mensagem = f'O login {login} acessou!'
        self.label_cadastrar.text = mensagem

FloatApp().run()
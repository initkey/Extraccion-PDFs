import flet as ft

class WelcomeView:

    #Definimos el constructor
    def __init__(self):
        self.name_input = ft.TextField(label="Escribe tu nombre",text_align=ft.TextAlign.CENTER)
        self.enter_button = ft.FilledButton(text="Entrar")

    def build(self):
        return ft.Column(
            [
                self.name_input,
                self.enter_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
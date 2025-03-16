import flet as ft

class WelcomeView:

    #Definimos el constructor
    def __init__(self):
        self.name_input = self.create_text_field("Bienvenida!","Escribe tu nombre")

    def create_text_field(self,label,text):
        return ft.TextField(
                label=label,
                label_style=ft.TextStyle(size=20,weight="Bold"),
                hint_text=text,
                hint_style=ft.TextStyle(size=20, weight="Normal"),
                text_align=ft.TextAlign.CENTER,
                text_size=25,
                text_style=ft.TextStyle(size=30,weight="Bold"),
                border=ft.InputBorder.UNDERLINE,
                filled=True,
                autofocus=True
            )

    def build(self):
        return ft.Column(
            [
                self.name_input
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
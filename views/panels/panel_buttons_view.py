import flet as ft

class PanelButtonsView:

    #Definimos el constructor
    def __init__(self):
        self.button_load = None
        self.button_extract = None
        self.button_change = None
        self.button_save = None

        def create_button(text):
            return ft.CupertinoFilledButton(
                    text=text,
                    width=200,
                    height=40,
                    on_click= lambda _: print(f"Botón: {text} -> Presionado")
                )
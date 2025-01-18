import flet as ft

class PanelButtonsView:

    #Definimos el constructor
    def __init__(self):
        self.button_load = None
        self.button_extract = None
        self.button_change = None
        self.button_save = None

    def create_panel_buttons(self):
        self.button_load = self.create_button("Cargar Documentos",ft.Icons.DOCUMENT_SCANNER)
        self.button_extract = self.create_button("Extraer Información", ft.Icons.PERM_DEVICE_INFORMATION_ROUNDED)
        self.button_change = self.create_button("Cambiar Nombre/Ubicación", ft.Icons.CHANGE_CIRCLE)
        self.button_save = self.create_button("Guardar Información",ft.Icons.SAVE_AS)
        return ft.Column(
            [
                self.button_load,
                self.button_extract,
                self.button_change,
                self.button_save
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def create_button(self,text,icon):
        return ft.CupertinoFilledButton(
                content= ft.Row(
                    [
                        ft.Icon(name=icon),
                        ft.Container(
                            content=ft.Text(text,size=12,weight="Bold",text_align=ft.TextAlign.LEFT),
                            width=150,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                width=220,
                height=50,
                padding=0,
                icon=icon,
                on_click= lambda _: print(f"Botón: {text} -> Presionado")
            )
    
    def build(self):
        return self.create_panel_buttons()
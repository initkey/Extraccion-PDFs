import flet as ft

class MainView:

    #Definimos el constructor
    def __init__(self):
        self.load_button = ft.FilledButton("Cargar Archivos", width=200, height=40)
        self.extract_button = ft.FilledButton("Extraer información", width=200, height=40)
        self.change_button = ft.FilledButton("Cambiar Nombre/Ubicación", width=200, height=40)
        self.save_button = ft.FilledButton("Guardar información", width=200, height=40)


    def build(self,session):
        user_name = session.get_user_name()
        connection_date = session.get_connection_date()
        return ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            content = 
                                ft.Column(
                                    [
                                        self.load_button,
                                        self.extract_button,
                                        self.change_button,
                                        self.save_button
                                    ],
                                    spacing=30,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                ),
                            width=250,
                            height=350,
                            border=ft.border.all(1),
                            border_radius=10
                        ),
                        ft.Container(
                            width=700,
                            height=350,
                            border=ft.border.all(1),
                            border_radius=10
                        )
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Container(
                            width=960,
                            height=250,
                            border=ft.border.all(1),
                            border_radius=10
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Container(
                            content = ft.Text(f"Buenos días, {user_name} - Última de conexión: {connection_date}", text_align= ft.TextAlign.CENTER, size=20),
                            width=960,
                            height=70,
                            border=ft.border.all(1),
                            border_radius=10
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER
                ),
            ]
        )
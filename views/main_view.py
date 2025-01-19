import flet as ft
from controllers.panel_buttons_controller import PanelButtonsController

class MainView:

    #Definimos el constructor
    def __init__(self,page,data):
        self.page = page
        self.data = data
        self.panel_buttons = PanelButtonsController(self.page,self.data)


    def build(self,session):
        user_name = session.get_user_name()
        connection_date = session.get_connection_date()
        return ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            content =self.panel_buttons.build(),
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
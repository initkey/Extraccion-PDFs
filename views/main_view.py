import flet as ft
from controllers.panel_buttons_controller import PanelButtonsController
from controllers.panel_selection_controller import PanelSelectionController
from controllers.panel_information_controller import PanelInformationController
class MainView:

    #Definimos el constructor
    def __init__(self,page,data,session):
        self.page = page
        self.data = data
        self.session = session
        self.panel_selection = PanelSelectionController(self.page,self.data)
        self.panel_buttons = PanelButtonsController(self.page,self.data,self.panel_selection)
        self.panel_information = PanelInformationController(self.session)

    def build(self):
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
                            content=self.panel_selection.build(),
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
                            content = self.panel_information.build(),
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
import flet as ft
from pyautogui import size
from controllers.welcome_controller import WelcomeController

def main(page:ft.Page):

    # Configuración inicial del page de la aplicación
    page.title = "Extracción de datos de PDFs"
    page.window.width = 300
    page.window.height = 200
    page.window.resizable = False
    page.window.maximizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def center_on_screen():
        # Obtener las dimensiones de la pantalla con la librería pyautogui
        screen_width, screen_height = size()
        # Centramos la aplicación en la pantalla
        page.window.left = (screen_width - page.window.width) // 2
        page.window.top = (screen_height - page.window.height) // 2
    center_on_screen()

    welcome_controller = WelcomeController(page)
    page.add(welcome_controller.build())

ft.app(target=main)
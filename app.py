import flet as ft
from pyautogui import size
from controllers.welcome_controller import WelcomeController
from controllers.main_controller import MainController

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
    
    def start_app(session):
        #Actualizamos el page para el tamaño correcto del main de la aplicación
        page.window.width = 1024
        page.window.height = 768
        center_on_screen()
        page.update()
        
        #Limpiamos la pantalla y colocamos un ft.Text de prueba para posteriormente colocar un MainView
        page.clean()
        main_controller = MainController(session,page)
        page.add(main_controller.build())

    center_on_screen()

    welcome_controller = WelcomeController(start_app)
    page.add(welcome_controller.build())

ft.app(target=main)
import flet as ft

def main(page:ft.Page):

    # Configuración inicial del page de la aplicación
    page.title = "Extracción de datos de PDFs"
    page.window.width = 300
    page.window.height = 200
    page.window.resizable = False
    page.window.maximizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(ft.Text("Primera vista"))

ft.app(target=main)
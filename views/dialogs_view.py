import flet as ft

class DialogsView:
    
    #Definimos el constructor
    def __init__(self,page):
        self.page = page
        self.dialog_selection = ft.CupertinoBottomSheet()
        self.dialog_selection.content = self.create_dialog()

    def show_dialog(self,e):
        self.page.overlay.append(self.dialog_selection)
        self.dialog_selection.open = True
        self.page.update()
    
    def close_dialog(self,e):
        self.dialog_selection.open = False
        self.page.update()
        self.page.overlay.remove(self.dialog_selection)

    def create_dialog(self):
        return ft.CupertinoActionSheet(
            title=ft.Row([ft.Text("Selección de documentos")],alignment=ft.MainAxisAlignment.START),
            message= ft.Row([ft.Text("Por favor, selecciona una de las siguientes opciones: ")],alignment=ft.MainAxisAlignment.CENTER),
            cancel= ft.CupertinoActionSheetAction(content=ft.Text("Cancelar"), is_destructive_action=True, on_click=lambda _: print("Se presionó cancelar")),
            actions=[
                ft.CupertinoActionSheetAction(
                    content=ft.Text("Seleccionar Carpeta"),
                    is_default_action=True,
                    on_click=lambda _: print("Seleccionar Carpeta")
                ),
                ft.CupertinoActionSheetAction(
                    content=ft.Text("Seleccionar Documentos"),
                    is_default_action=True,
                    on_click=lambda e: print("Seleccionar Documentos")
                ),
            ],
        )
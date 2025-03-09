import flet as ft

class SaveFileView:

    # Definimos el constructor
    def __init__(self,page):
        self.page = page
        self.file_picker = ft.FilePicker(on_result=None)
        self.page.overlay.append(self.file_picker)

    # Definimos
    def open_file_picker(self):
        self.file_picker.save_file(
            dialog_title="Guardar archivo",
            file_name="temporal.xlsx",
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["xlsx"])
        self.page.update()

    def build(self):
        self.open_file_picker()
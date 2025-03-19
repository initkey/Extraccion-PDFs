from models.data_model import DataModel
from views.save_file_view import SaveFileView

class SaveFileController:
    def __init__(self,page,data,snackbar_save,view_buttons,view_selection):
        self.page = page
        self.data = data
        self.view = SaveFileView(page)
        self.snackbar = snackbar_save
        self.view_buttons = view_buttons
        self.view_selection = view_selection

    def build(self, e):
        self.view.build()
        self.open_file_picker(e)

    def open_file_picker(self, e):
        self.view.file_picker.on_result = self.on_file_selected

    def on_file_selected(self, e):
        if e.path:
            self.data.set_file_path(e.path)
            # Guardar el DataFrame en Excel
            created = self.data.save_dataframe_to_excel()
            if created:
                self.page.open(self.snackbar)
                #! Crear función que limpie controles
                self.data.list_documents = []
                self.view_buttons.button_save.disabled = True
                self.view_buttons.button_load.disabled = False
                self.view_selection.view.grid_selection.controls.clear()
                self.view_selection.update_text_button()
                self.page.update()
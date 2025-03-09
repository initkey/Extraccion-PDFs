from models.data_model import DataModel
from views.save_file_view import SaveFileView

class SaveFileController:
    def __init__(self,page,data):
        self.page = page
        self.data = data
        self.view = SaveFileView(page)

    def build(self, e):
        self.view.build()
        self.open_file_picker(e)

    def open_file_picker(self, e):
        self.view.file_picker.on_result = self.on_file_selected

    def on_file_selected(self, e):
        if e.path:
            self.data.set_file_path(e.path)
            # Guardar el DataFrame en Excel
            self.data.save_dataframe_to_excel()
from views.dialogs_view import DialogsView
from controllers.open_folders_files_controller import OpenFoldersFilesController

class DialogsController:

    #Definimos el constructor
    def __init__(self,page,data):
        self.page = page
        self.view = DialogsView(self.page,self.on_click_file_picker)
        self.view_file_picker = OpenFoldersFilesController(self.page,data)

    def on_click_file_picker(self,e):
        self.view_file_picker.build(e)
        self.view_file_picker.get_documents()
        self.view.close_dialog(e)

    def build(self,e):
        return self.view.show_dialog(e)

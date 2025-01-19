from views.dialogs_view import DialogsView
from controllers.open_folders_files_controller import OpenFoldersFiles

class DialogsController:

    #Definimos el constructor
    def __init__(self,page):
        self.page = page
        self.view = DialogsView(self.page,self.on_click_file_picker)
        self.view_file_picker = OpenFoldersFiles(self.page)

    def on_click_file_picker(self,e):
        self.view_file_picker.build(e)
        self.view.close_dialog(e)

    def build(self,e):
        return self.view.show_dialog(e)

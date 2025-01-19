import flet as ft

class OpenFoldersFiles():

    #Definimos el constructor
    def __init__(self,page):
        self.page = page
        self.pick_files_dialog = ft.FilePicker(on_result=None)
        self.page.overlay.append(self.pick_files_dialog)

    def open_file_picker(self,e):
        self.pick_files_dialog.pick_files(allow_multiple=True)
        self.page.update()
    
    def build(self,e):
        return self.open_file_picker(e)
from views.open_folders_files import OpenFoldersFiles

class OpenFoldersFilesController:

    #Definimos el constructor
    def __init__(self,page,data):
        self.page = page
        self.view = OpenFoldersFiles(self.page)
        self.data = data

    def get_documents(self):
        self.view.pick_files_dialog.on_result = self.pick_files_result
    
    def pick_files_result(self, e):
        # Guardar los archivos seleccionados
        self.documents = [f.name for f in e.files] if e.files else []
        self.data.set_list_documents(self.documents)
        print(f"Archivos guardados: {self.data.get_list_documents()}")

    def build(self,e):
        return self.view.build(e)
from views.open_folders_files import OpenFoldersFiles
import asyncio
import os

class OpenFoldersFilesController:

    #Definimos el constructor
    def __init__(self,page,data):
        self.page = page
        self.view = OpenFoldersFiles(self.page)
        self.data = data

    async def check_data(self):
        while not self.data.get_list_documents():
            await asyncio.sleep(1)

    async def get_documents(self):
        self.view.pick_files_dialog.on_result = self.pick_files_result
        await self.check_data()
    
    def pick_files_result(self, e):
        # Guardar los archivos seleccionados
        self.documents = [f.name for f in e.files] if e.files else []
        directory_path = os.path.dirname(e.files[0].path)
        self.data.set_documents_path(directory_path)
        self.data.set_list_documents(self.documents)
        print(f"Archivos guardados: {self.data.get_list_documents()}")

    def build(self,e):
        return self.view.build(e)
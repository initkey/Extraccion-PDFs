from views.open_folders_files import OpenFoldersFiles

class OpenFoldersFilesController:

    #Definimos el constructor
    def __init__(self,page):
        self.page = page
        self.view = OpenFoldersFiles(self.page)

    def build(self,e):
        return self.view.build(e)
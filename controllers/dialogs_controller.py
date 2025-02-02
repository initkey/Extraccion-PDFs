from views.dialogs_view import DialogsView
from controllers.open_folders_files_controller import OpenFoldersFilesController

class DialogsController:

    #Definimos el constructor
    def __init__(self,page,data,selection,buttons):
        self.page = page
        self.buttons = buttons
        self.selection = selection
        self.view = DialogsView(self.page,self.on_click_file_picker)
        self.view_file_picker = OpenFoldersFilesController(self.page,data)

    async def on_click_file_picker(self,e):
        self.view_file_picker.build(e)
        await self.view_file_picker.get_documents()
        self.view.close_dialog(e)
        await self.selection.load_data()
        self.buttons.button_load.disabled = True
        self.buttons.button_extract.disabled = False
        self.page.update()

    def build(self,e):
        return self.view.show_dialog(e)

from views.panels.panel_buttons_view import PanelButtonsView
from controllers.dialogs_controller import DialogsController

class PanelButtonsController:
    
    #Definimos el constructor
    def __init__(self,page,data,selection):
        self.page = page
        self.data = data
        self.selection = selection
        self.view = PanelButtonsView()
        self.view_dialog = DialogsController(self.page,self.data,selection)
        self.view.button_load.on_click = self.on_click_load
        self.view.button_extract.on_click = self.on_click_extract

    def on_click_extract(self,e):
        container = [doc for doc in self.selection.view.grid_selection.controls]
        self.data.set_documents_selected([doc.content.label.value for doc in container])
        documents = self.data.get_documents_selected()
        path = self.data.get_documents_path()
        list_documents = self.data.get_documents_with_path(path,documents)
        tables = self.data.get_preprocessed_data(list_documents)
        information = self.data.get_real_data(tables)

    def on_click_load(self,e):
        self.view_dialog.build(e)

    def build(self):
        return self.view.build()
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

    def on_click_load(self,e):
        self.view_dialog.build(e)
        # self.selection.load_data()

    def build(self):
        return self.view.build()
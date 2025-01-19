from views.panels.panel_buttons_view import PanelButtonsView
from controllers.dialogs_controller import DialogsController

class PanelButtonsController:
    
    #Definimos el constructor
    def __init__(self,page):
        self.page = page
        self.view = PanelButtonsView()
        self.view_dialog = DialogsController(self.page)
        self.view.button_load.on_click = self.on_click_load

    def on_click_load(self,e):
        self.view_dialog.build(e)

    def build(self):
        return self.view.build()
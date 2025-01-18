from views.panels.panel_buttons_view import PanelButtonsView

class PanelButtonsController:
    
    #Definimos el constructor
    def __init__(self):
        self.view = PanelButtonsView()

    def build(self):
        return self.view.build()
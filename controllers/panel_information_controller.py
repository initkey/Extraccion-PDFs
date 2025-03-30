from views.panels.panel_information_view import PanelInformationView

class PanelInformationController:

    #Definimos el controlador
    def __init__(self, session):
        self.session = session
        self.view = PanelInformationView(self.session)

    def build(self):
        return self.view.build()
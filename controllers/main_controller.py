from views.main_view import MainView

class MainController:

    #Definimos el constructor
    def __init__(self,session):
        self.view = MainView()
        self.session = session

    def build(self):
        return self.view.build(self.session)
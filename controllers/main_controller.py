from views.main_view import MainView

class MainController:

    #Definimos el constructor
    def __init__(self,session,page):
        self.page = page
        self.view = MainView(self.page)
        self.session = session

    def build(self):
        return self.view.build(self.session)
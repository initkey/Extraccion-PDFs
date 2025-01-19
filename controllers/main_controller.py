from views.main_view import MainView
from models.data_model import DataModel

class MainController:

    #Definimos el constructor
    def __init__(self,session,page):
        self.page = page
        self.data = DataModel()
        self.view = MainView(self.page,self.data)
        self.session = session

    def build(self):
        return self.view.build(self.session)
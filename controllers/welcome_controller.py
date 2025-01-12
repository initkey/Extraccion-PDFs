from views.welcome_view import WelcomeView

class WelcomeController:
    
    #Definimos el constructor
    def __init__(self,page):
        self.view = WelcomeView()
        self.page = page
    
    def build(self):
        return self.view.build()
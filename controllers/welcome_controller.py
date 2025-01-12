from views.welcome_view import WelcomeView
from models.session_model import SessionModel

class WelcomeController:
    
    #Definimos el constructor
    def __init__(self,page,on_enter_callback):
        self.session = SessionModel()
        self.view = WelcomeView()
        self.page = page
        self.on_enter_callback = on_enter_callback

        # Asignar evento al botón "Entrar"
        self.view.enter_button.on_click = self.handle_enter

    def handle_enter(self, e):
        user_name = self.view.name_input.value.strip()
        if user_name:
            self.session.set_user_name(user_name)
            self.on_enter_callback(self.session)
    
    def build(self):
        return self.view.build()
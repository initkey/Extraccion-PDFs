from views.welcome_view import WelcomeView
from models.session_model import SessionModel

class WelcomeController:
    
    #Definimos el constructor
    def __init__(self,on_enter_callback):
        self.session = SessionModel()
        self.view = WelcomeView()
        self.on_enter_callback = on_enter_callback

        # Asignar evento al botón "Entrar"
        self.view.name_input.on_submit = self.handle_enter

    def handle_enter(self, e):
        user_name = self.view.name_input.value.strip()
        if user_name:
            self.session.set_user_name(user_name)
            self.on_enter_callback(self.session)
    
    def build(self):
        return self.view.build()
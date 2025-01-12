from datetime import datetime
class SessionModel:
    
    #Creamos el constructor
    def __init__(self):
        self.user_name = None
    
    def get_connection_date(self):
        return datetime.now().strftime(f"%d/%m/%Y %I:%M:%S %p")

    #Guardamos el nombre del usuario
    def set_user_name(self,name):
        self.user_name = name

    #Devolvemos el nombre del usuario
    def get_user_name(self):
        return self.user_name
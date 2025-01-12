class SessionModel:
    
    #Creamos el constructor
    def __init__(self):
        self.user_name = None
    
    #Guardamos el nombre del usuario
    def set_user_name(self,name):
        self.user_name = name

    #Devolvemos el nombre del usuario
    def get_user_name(self):
        return self.user_name
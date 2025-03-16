from datetime import datetime
import json
class SessionModel:
    
    #Creamos el constructor
    def __init__(self):
        self.user_name = None
    
    def get_connection_date(self):
        return datetime.now().strftime(f"%d/%m/%Y %I:%M:%S %p")
    
    # Definición de la función que modifica la palabra y le da formato
    def format_name(self,name):
        name = name.strip().lower()
        return name.title()

    # Definición de la función que guarda el valor en un json
    def set_name(self,name):
        data = {"name": name}
        with open("username.json","w") as file:
            json.dump(data,file)  

    # Definición de la función que recupera el valor de un json
    def get_name(self):
        try:
            with open("username.json","r") as file:
                data = json.load(file)
                return data.get("name",None)
        except (FileNotFoundError, json.JSONDecodeError):
            return None
import time
import json
class SessionModel:
    
    #Creamos el constructor
    def __init__(self):
        self.__username = None
    
    def get_connection_date(self):
        return time.strftime(f"%d/%m/%Y %I:%M:%S %p", time.localtime())
    
    # Definición de la función que modifica la palabra y le da formato
    def format_name(self,name):
        self.__username = name.strip().lower()
        return self.__username.title()

    # Definición de la función que recupera el valor de un json
    @property
    def username(self):
        try:
            with open("username.json","r") as file:
                data = json.load(file)
                self.__username = data.get("name",None)
                return self.__username
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    # Definición de la función que guarda el valor en un json
    @username.setter
    def username(self,name):
        self.__username = name
        data = {"name": self.__username}
        with open("username.json","w") as file:
            json.dump(data,file)
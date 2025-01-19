class DataModel:

    #Creamos el constructor
    def __init__(self):
        self.list_documents = []

    def set_list_documents(self,documents):
        self.list_documents = documents
    
    def get_list_documents(self):
        return self.list_documents
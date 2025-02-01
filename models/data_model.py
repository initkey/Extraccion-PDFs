import os
class DataModel:

    #Creamos el constructor
    def __init__(self):
        self.list_documents = []
        self.documents_selected = []
        self.documents_path = ""

    def get_documents_with_path(self,path,documents):
        for document in documents:
            full_path = os.path.join(path,document)
            normalized_full_path = os.path.normpath(full_path)
            yield normalized_full_path   

    def set_documents_path(self,path):
        self.documents_path = path

    def get_documents_path(self):
        return self.documents_path

    def set_documents_selected(self,documents):
        self.documents_selected = documents

    def get_documents_selected(self):
        return self.documents_selected

    def set_list_documents(self,documents):
        self.list_documents = documents
    
    def get_list_documents(self):
        return self.list_documents
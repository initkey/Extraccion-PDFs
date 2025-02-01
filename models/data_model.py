import os
import itertools
class DataModel:

    #Creamos el constructor
    def __init__(self):
        self.list_documents = []
        self.documents_selected = []
        self.documents_path = ""

    def check_generator(self,generator):
            #Creamos una copia de nuestro generador para poder trabajar con ella
            new_generator, new_generator_2 = itertools.tee(generator,2)
            try:
                element = next(new_generator)
            except StopIteration:
                return False, new_generator_2
            try: 
                next_element = next(new_generator)
                return False, new_generator_2
            except StopIteration:
                return True, new_generator_2

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
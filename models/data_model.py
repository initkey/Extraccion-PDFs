import os
import itertools
import pdfplumber
class DataModel:

    #Creamos el constructor
    def __init__(self):
        self.list_documents = []
        self.documents_selected = []
        self.documents_path = ""

    def check_document(self,generator):
        try:
            document_name = next(generator)
            tables = next(generator)
            text = next(generator)
        except Exception as e:
            print(f"Error en lectura {e}")
        if text:
            return document_name,tables,text
        else:
            return None,None,None
        


    def get_real_data(self,data):
        data_result = []
        
        while True:
            document = list()
            try:
                document,tables,text = self.check_document(data)
                
            except StopIteration:
                break
        return data_result

    def get_raw_data(self,document):
        #Ingresamos a cada documento, guardamos el nombre del documento, las tablas y el texto general en un generador, si ocurre un error posteriormente en la exception agregaremos la función para informar del tema.
        with pdfplumber.open(document) as pdf:
            for page in pdf.pages:
                try:
                    yield document
                    yield page.extract_tables()
                    yield page.extract_text()
                except Exception as e:
                    #!Anexar función para recuperar la información en caso de error
                    print(f'Error {e}')

    def get_preprocessed_data(self,documents):
        #Verificamos con cuantos documentos vamos a trabajar, según sea el caso.. Llamaremos a una función que extraerá toda la información en bruto.
        isTrue, documents = self.check_generator(documents)
        if isTrue:
            yield from self.get_raw_data(next(documents))
        else:
            for document in documents:
                yield from self.get_raw_data(document)

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
import os
import itertools
import pdfplumber
from re import search, IGNORECASE
class DataModel:

    #Creamos el constructor
    def __init__(self):
        self.list_documents = []
        self.documents_selected = []
        self.documents_path = ""
        self.names = self.extract_info("config.txt")

    def check_pattern(self,value, data):
        table_pattern = {
            1 : r'Pág\. 1\/\d{1,2}|Pág\. 1\/',
            2 : rf"Especialista\s+({'|'.join(self.names)})",
            3 : r'Datos del Dispositivo',
            4 : r'Observaciones.*Condiciones',
            5 : r'Especialista(.*?)Fecha',
            6 : r'Fecha:\s*(\d{1,2}/\d{1,2}/\d{2,4})'
        }
        pattern = table_pattern.get(value,r'Datos del Dispositivo')
        return search(pattern,''.join(map(str,data)), IGNORECASE)

    def extract_info(self,txt):
        try:
            with open(txt, 'r') as file:
                for line in file:
                    if line.startswith("Especialista:"):
                        names_str = line.split(":",1)[1].strip()
                        names = [name.strip() for name in names_str.split(",")]
                return names
        except FileNotFoundError:
            print(f"El archivo {txt} no se encontró.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
        return []

    def check_document(self,data):
        document = list()
        name_document = None
        tables = None
        text = None
        try:
            for _ in range(3):
                    document.append(next(data))
                    print(f"Data:{document}")
            name_document = document[0]
            tables = document[1]
            text = document[2]
            print("Nombres:")
            print(name_document)
            print("Tablas")
            print(tables)
            print("Textos:")
            print(text)
        except Exception as e:
            print(f"Error inesperado: {e}")
        return name_document,tables,text
        
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
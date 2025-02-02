import os
import itertools
import pdfplumber
from re import search, IGNORECASE,sub
class DataModel:

    #Creamos el constructor
    def __init__(self):
        self.list_documents = []
        self.documents_selected = []
        self.documents_path = ""
        self.names = self.extract_info("config.txt")

    def filter_invalid_information(self,list,data_result,info_extra):
        for row in list:
            empty_count = sum(1 for item in row if item == "" or item is None or item == [""])
            empty_percentage = (empty_count/len(row)) * 100
            threshold = 70
            if empty_percentage < threshold:
                for index,extra in enumerate(info_extra):
                    row.insert(index,extra)
                improved_row = self.get_improved_info(row)
                data_result.append(improved_row)

    def get_improved_info(self,data):
        remove_none = [info for info in data if info is not None]
        try:
            information_clear = [sub("\n"," ",info) if type(info) == str else info for info in remove_none]
        except Exception as e:
            print(f"Error al limpiar datos: {e}")
        return information_clear

    def get_match(self,tables,data_result,initial,info_extra):
        for data in tables:
            pattern_match = self.check_pattern(3,data)
            if pattern_match:
                size = len(data)
                info = [data[index] for index in range(initial,size)]
                self.filter_invalid_information(info,data_result,info_extra)

    def get_real_data(self,tables_doc):
        data_result = []
        owner = ""
        date = ""
        while True:
            document = list()
            try:
                for _ in range(3):
                    document.append(next(tables_doc))
                name_document = document[0].replace("\\", "/")
                tables = document[1]
                text_doc = document[2]
                if tables:
                    owner = self.check_pattern(5,text_doc).group(1).strip() if self.check_pattern(5,text_doc) else "No encontrado"
                    date = self.check_pattern(6,text_doc).group(1).strip() if self.check_pattern(6,text_doc) else "Sin fecha"
                    info_extra = [name_document,owner,date]
                    try:
                        pattern_match_page = self.check_pattern(1,tables)
                        pattern_owner_match = self.check_pattern(2,text_doc)
                        if pattern_match_page:
                            self.get_match(tables,data_result,3,info_extra)
                        elif pattern_owner_match:
                            self.get_match(tables,data_result,2,info_extra)
                        else:
                            pattern_word_match = self.check_pattern(4,tables)
                            if not (pattern_word_match and tables):
                                self.filter_invalid_information(tables,data_result,info_extra)
                    except Exception:
                        continue
            except StopIteration:
                break
        return data_result

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
            name_document = document[0]
            tables = document[1]
            text = document[2]
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
                    print(f'Error: {e} - {document}')

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
        for document in documents:
            if document.endswith("pdf"):
                self.list_documents.append(document)
    
    def get_list_documents(self):
        return self.list_documents
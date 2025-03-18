from views.panels.panel_buttons_view import PanelButtonsView
from controllers.dialogs_controller import DialogsController
from controllers.save_file_controller import SaveFileController
from flet import SnackBar,Text

"""

    Es necesario mover el SnackBar a una vista para que sea correcto el modelo MVC
    Crear un SnackBar general que reciba un texto y mande la información... ya hay 2
    vistas incrustadas que debemos corregir

"""

class PanelButtonsController:
    
    #Definimos el constructor
    def __init__(self,page,data,selection):
        self.page = page
        self.data = data
        self.selection = selection
        self.view = PanelButtonsView()
        self.view_dialog = DialogsController(self.page,self.data,selection,self.view)
        self.view.button_load.on_click = self.on_click_load
        self.view.button_extract.on_click = self.on_click_extract
        self.information = None
        self.view.button_save.on_click = self.on_click_save
        #! Debemos corregir este anexo con una vista
        file_save = SnackBar(Text("Archivo guardado correctamente"))
        self.view_save = SaveFileController(page,data,file_save)

    def on_click_save(self,e):
        self.data.set_information(self.information)
        self.view_save.build(e)

    def on_click_extract(self,e):
        documents_selected = self.selection.get_chip_selected()
        if documents_selected[1]:
            self.page.open(SnackBar(Text(f"Información extraída de {documents_selected[0]} documentos") if documents_selected[0] > 2 else Text(f"Información extraída de {documents_selected[0]} documento")))
            self.data.set_documents_selected(documents_selected[1])
            documents = self.data.get_documents_selected()
            path = self.data.get_documents_path()
            list_documents = self.data.get_documents_with_path(path,documents)
            tables = self.data.get_preprocessed_data(list_documents)
            self.information = self.data.get_real_data(tables)
            self.view.button_save.disabled = False
            self.view.button_extract.disabled = True
            self.page.update()
        else:
            self.page.open(SnackBar(Text(f"No ha seleccionado ningún documento")))

    def on_click_load(self,e):
        self.view_dialog.build(e)

    def build(self):
        return self.view.build()
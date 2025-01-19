from views.dialogs_view import DialogsView

class DialogsController:

    #Definimos el constructor
    def __init__(self,page):
        self.page = page
        self.view = DialogsView(self.page)

    def build(self,e):
        return self.view.show_dialog(e)

import flet as ft

class PanelInformationView:

    #Definimos el constructor
    def __init__(self,session):
        self.session = session

    def create_panel(self):
        connection_date = self.session.get_connection_date()
        return ft.Text(f"Buenos días, {self.session.username} - Última de conexión: {connection_date}", text_align= ft.TextAlign.CENTER, size=20)

    def build(self):
        return self.create_panel()
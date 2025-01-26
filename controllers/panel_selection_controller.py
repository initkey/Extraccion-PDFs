from views.panels.panel_selection_view import PanelSelectionView

class PanelSelectionController:

    #Definimos el constructor
    def __init__(self,page,data):
        self.page = page
        self.data = data
        self.view = PanelSelectionView(page,data)
    
    async def load_data(self):
        await self.view.refresh_grid()
        self.data.set_list_documents([])

    def build(self):
        return self.view.build()
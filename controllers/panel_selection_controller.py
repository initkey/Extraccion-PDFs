from views.panels.panel_selection_view import PanelSelectionView
from flet import Chip

class PanelSelectionController:

    #Definimos el constructor
    def __init__(self,page,data):
        self.page = page
        self.data = data
        self.view = PanelSelectionView(page,data)
        self.view.button_select.on_click = self.on_click_selected
        self.button_text = self.view.button_select.content.controls[1].content
    
    def update_text_button(self):
        if self.button_text.value == "Select All":
            self.button_text.value = "Unselect All"
        else:
            self.button_text.value = "Select All"
        self.page.update()

    def on_click_selected(self,e):
        if not len(self.view.grid_selection.controls) == 0:
            for container in self.view.grid_selection.controls:
                chip = container.content
                if isinstance(chip,Chip):
                    if self.button_text.value == "Select All":
                        chip.selected = True
                    else:
                        chip.selected = False
            self.update_text_button()
            self.view.grid_selection.update()
            
    
    async def load_data(self):
        self.view.button_select.disabled = False
        await self.view.refresh_grid()
        self.page.update()
        self.data.set_list_documents([])

    def build(self):
        return self.view.build()
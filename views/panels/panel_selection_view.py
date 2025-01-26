import flet as ft
import asyncio

class PanelSelectionView:

    #Definimos el constructor:
    def __init__(self,page,data):
        self.page = page
        self.data = data
        self.grid_selection = self.create_panel_selection()

    def chip_selected(self,e):
        self.grid_selection.update()

    def create_chip(self,name):
        return ft.Container(
            content=ft.Chip(
                label=ft.Text(name,size=9,max_lines=2),
                on_select=self.chip_selected,
                expand=True,
                padding=ft.padding.all(1),
            ),
            border_radius=10,
            alignment=ft.alignment.center_left,
            expand=True
        )

    def create_panel_selection(self):
        return ft.GridView(
            expand=True,
            width=600,
            height=250,
            runs_count=2,
            child_aspect_ratio=8,
            spacing=5,
            run_spacing=5,
            padding=10
        )
    
    async def refresh_grid(self):
        self.grid_selection.controls.clear()
        documents = self.data.get_list_documents()
        for document in documents:
            self.grid_selection.controls.append(self.create_chip(document))
        self.grid_selection.update()
        await asyncio.sleep(1)

    def build(self):
        return self.grid_selection
    
# if __name__ == "__main__":
#     def main(page:ft.Page):
#         interface = PanelSelectionView(page)
#     ft.app(target=main)
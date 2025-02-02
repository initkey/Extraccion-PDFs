import flet as ft
import asyncio

class PanelSelectionView:

    #Definimos el constructor:
    def __init__(self,page,data):
        self.page = page
        self.data = data
        self.grid_selection = self.create_grid()
        self.button_select = self.create_button("Select All",ft.Icons.SELECT_ALL)

    def create_button(self,text,icon):
        return ft.CupertinoFilledButton(
                content= ft.Row(
                    [
                        ft.Icon(name=icon),
                        ft.Container(
                            content=ft.Text(text,size=12,weight="Bold",text_align=ft.TextAlign.LEFT),
                            width=100,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                width=150,
                height=40,
                padding=0,
                icon=icon,
                disabled=True
            )

    def create_select_all(self):
        return ft.Row(
            [
                ft.Container(content=self.button_select,width=200,padding=ft.Padding(0,0,20,0))
            ], 
            alignment=ft.MainAxisAlignment.END
        )

    def create_panel_selection(self):
        return ft.Column(
            [
                ft.Container(content=self.grid_selection,width=700,height=290,border_radius=10),
                ft.Container(content=self.create_select_all(),width=700,height=50,border_radius=10,border=ft.border.all(1))
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=5
        )

    def chip_selected(self,e):
        self.grid_selection.update()

    def create_chip(self,name):
        return ft.Container(
            content=ft.Chip(
                label=ft.Text(name,size=11,max_lines=2,overflow=ft.TextOverflow.ELLIPSIS),
                on_select=self.chip_selected,
                height=90,
                padding=ft.padding.all(1)
            ),
            border_radius=10,
            alignment=ft.alignment.center_left,
            expand=True
        )

    def create_grid(self):
        return ft.GridView(
            width=690,
            height=350,
            max_extent=340,
            child_aspect_ratio=10,
            spacing=5,
            run_spacing=5,
            padding=5
        )
    
    async def refresh_grid(self):
        self.grid_selection.controls.clear()
        documents = self.data.get_list_documents()
        for document in documents:
            self.grid_selection.controls.append(self.create_chip(document))
        self.grid_selection.update()
        await asyncio.sleep(0.5)
        self.page.update()

    def build(self):
        return self.create_panel_selection()
    
# if __name__ == "__main__":
#     def main(page:ft.Page):
#         interface = PanelSelectionView(page)
#     ft.app(target=main)
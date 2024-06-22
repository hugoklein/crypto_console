import flet as ft
import json
import os

from ctrConsola import ctrConsola 

class MainForm(ft.UserControl):

    def __init__(self):
        super().__init__(expand=True)

        self.menu = ft.Container(
            bgcolor="red",
            border_radius=10,
            alignment = ft.alignment.top_center,            
            col = 1,
            padding = ft.padding.only(top=10),
            content=  ft.Column(
                [
                    ft.OutlinedButton(text="Test", on_click=self.onTest),         
                    ft.OutlinedButton(text="image", on_click=self.onTest2),         
                ]         
            )
        )
        self.txtCommand = ft.TextField(
            prefix_text=" c:\\",            
            on_submit=self.onSendCommand,
            border = ft.InputBorder.NONE,
            text_style = ft.TextStyle(font_family="Consolas",size=11),
            bgcolor="blue",
        )

        self.panelConsola = ft.Container(
            bgcolor="blue",
            border_radius=10,
            col = 11,
            content=ft.Column(scroll=ft.ScrollMode.AUTO,auto_scroll=True, spacing=1,
                              controls=[
                                  self.txtCommand
                              ]
                              
            )
        )      
        self.consola = ctrConsola()
        self.consola.col = 11       
        self.consola.on_click = self.setFocus        
        self.cnt = ft.ResponsiveRow(
            controls=[
                self.menu,
                self.consola
            ]
        )
    def setFocus(self, e):
        self.consola.setFocus()
    
    def build(self):
        return self.cnt
    
    def onSendCommand(self, e):
        self.panelConsola.lineas.insert(-1, ft.Text(self.txtCommand.value, font_family="Consolas" ))

        self.txtCommand.value = ""
        self.txtCommand.focus()
        self.update()


    def onTest(self, e):
        #self.panelConsola.content.controls.insert(-1, ft.Text("Nueva Fila " + str(self.panelConsola.content.controls.count)    ))
        self.consola.clear()
        self.update()
    
    def onTest2(self, e):
        #self.panelConsola.content.controls.insert(-1, ft.Text("Nueva Fila " + str(self.panelConsola.content.controls.count)    ))
        img = ft.Image(
            src=f"assets/kucoin.png",
            width=100,
            height=100,
            fit=ft.ImageFit.CONTAIN,
        )
        self.consola.lineas.insert(-1,  img  )
        self.update()

def main(page: ft.Page):    
    page.window_min_height = 500
    page.window_min_width = 1100
    page.spacing = 0
    page.padding = 0
    page.title = "Crypto console"    

    mf = MainForm()
    page.add(mf)
        
    page.dark_theme = ft.Theme(color_scheme_seed="teal")
    page.theme_mode = ft.ThemeMode.DARK
    page.update()

ft.app(target=main)
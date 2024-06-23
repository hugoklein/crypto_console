import flet as ft
import json
import os

from ctrConsola import ctrConsola 
from ConsoleManager import ConsoleManager

class MainForm(ft.ResponsiveRow):

    def __init__(self):
        super().__init__(expand=True)
        self.accounts = self.getAccounts()
        self.BrokersIcons = {"Binance": ft.icons.LAYERS,
                             "Kucoin" :  ft.icons.COPYRIGHT,
                             "Balanz" : ft.icons.FORMAT_BOLD }

        self.menu = ft.Container(            
            border_radius=4,
            alignment = ft.alignment.top_center,            
            col = 1,
            padding = ft.padding.only(top=10),
            content=  ft.Column(
                [
                    ft.OutlinedButton(text="Test", on_click=self.onTest,width=95,icon=f"assets/kucoin.ico"),         
                    ft.OutlinedButton(text="image", on_click=self.onTest2,width=95),         
                    ft.OutlinedButton(text="cmd", on_click=self.onCmd,width=95),         
                    ft.OutlinedButton(text="pos", on_click=self.onPos,width=95),         
                    ft.OutlinedButton(text="both", on_click=self.onBoth,width=95),         
                    ft.OutlinedButton(text="out", on_click=self.onOut,width=95),         
                    ft.OutlinedButton(text=">>>", on_click=self.onRight,width=95),         
                    ft.OutlinedButton(text="<<<", on_click=self.onLeft,width=95),         
                ]         
            )
        )
        
        self.tabMain = ft.Tabs(
            selected_index=0,
            animation_duration=200,
            on_change = self.changeTab,
            col=11

        )

        for account in self.accounts:
            t = ft.Tab(                
                text=account["title"], 
                content=ConsoleManager(account) 
            )
            if account["broker"] in self.BrokersIcons:
                t.icon = self.BrokersIcons[account["broker"]]

            self.tabMain.tabs.append(t)
            
       
        self.cnt = ft.ResponsiveRow(
            controls=[
                self.menu,
                self.tabMain
            ]
        )

    def build(self):
        return self.cnt


    def changeTab(self, e):
        index = self.tabMain.selected_index    
        self.consoleManager:ConsoleManager  = self.tabMain.tabs[index].content        
        self.page.update()
        

    def getAccounts(self):
        if os.path.exists("accounts.json"):
            f = open("accounts.json","r")
            self.accounts = json.loads(f.read())
            f.close()                
        else:
            self.accounts = [
                {"title": "Futuro Hugo",
                 "broker": "Binance",
                 "name" : "hugo",
                 "wallet" : "future"
                },
                {"title": "Spot Hugo",
                 "broker": "Binance",
                 "name" : "hugo",
                 "wallet" : "spot"
                },
                {"title": "Hugo",
                 "broker": "Kucoin",
                 "name" : "hugo",
                 "wallet" : "future"
                },
                {"title": "Maru",
                 "broker": "Kucoin",
                 "name" : "maru",
                 "wallet" : "future"
                 }
            ]
            f = open("accounts.json", "w")
            f.write(json.dumps(self.accounts))
            f.close()

        return self.accounts


    def setFocus(self, e):
        self.consoleManager.setFocus()
   
    def onTest(self, e):        
        self.consoleManager.clearConsole()        
    
    def onTest2(self, e):
        #self.panelConsola.content.controls.insert(-1, ft.Text("Nueva Fila " + str(self.panelConsola.content.controls.count)    ))
        img = ft.Image(
            src=f"assets/kucoin.png",
            width=50,
            height=50,
            fit=ft.ImageFit.CONTAIN,
        )
        msg = ft.Row(controls=[
            img,
            ft.Text("Esto es una prueba")
        ])        
        self.consoleManager.out(msg)
        self.update()

    def onCmd(self, e):
        self.consoleManager.onlyConsole()        

    def onPos(self, e):
        self.consoleManager.onlyPositions()        
        
    def onBoth(self, e):
        self.consoleManager.both()        

    def onOut(self, e):
        self.consoleManager.outText("Hola Mundo", True,)
        self.consoleManager.outText("Renglon 2")
        self.consoleManager.outText("Renglon 3")

    def onRight(self, e):
        current = self.consoleManager.console.col
        current += 1
        if current == 12:
            pass
        if current > 12:
            pass
        self.consoleManager.console.col = current
        self.consoleManager.positions.col = 12 - current
        self.update()
    
    def onLeft(self, e):
        current = self.consoleManager.console.col
        current -= 1
        if current == 1:
            pass
        if current < 1:
            pass
        self.consoleManager.console.col = current
        self.consoleManager.positions.col = 12 - current
        self.update()


def main(page: ft.Page):    
    page.window.min_height = 500
    page.window.min_width = 1100
    page.spacing = 0
    page.padding = 0
    page.title = "Crypto console"    

    mf = MainForm()
    page.add(mf)

    page.dark_theme = ft.Theme(color_scheme_seed="teal")
    page.theme_mode = ft.ThemeMode.DARK
    page.update()

ft.app(target=main)
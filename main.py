import flet as ft
import json
import os
from ctrConsola import ctrConsola 

class MainPage:

    def __init__(self):
        self.accounts = self.getAccounts()
                
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

    def changeTab(self, e):
        index = self.tabs.selected_index        
        self.tabs.tabs[index].content.setFocusCommand()
        self.page.update()
        

    def createTabs(self):
        self.tabs = ft.Tabs(animation_duration=300)
        for account in self.accounts:
            ac = AccountContainer(account, self.page)            
            self.tabs.tabs.append(ft.Tab( content=ac, text = account["title"]))
            self.tabs.on_change = self.changeTab
       
        
        return self.tabs

    def main(self, page: ft.Page):
        self.page = page
        page.window_min_height = 1000
        page.window_min_width = 1000
        page.spacing = 0
        page.padding = 0
        page.title = "Crypto console"
        self.tabs = self.createTabs()
        page.add(self.tabs)
               
        page.dark_theme = ft.Theme(color_scheme_seed="teal")
        page.theme_mode = ft.ThemeMode.DARK        
        

        page.update()

class AccountContainer(ft.Container):
    def __init__(self, account, page):
        super().__init__()
        self.account = account
        self.page = page
        self.content = self.createAccountContainer()

    def build(self):
        return self.content

    def setFocusCommand(self):
        self.cCommand.focus()

    def sendCommand(self, e):
        self.cRowsConsole.controls[0].controls.append(  ft.Text(self.cCommand.value))
        self.cCommand.value = ""
        self.setFocusCommand()

        self.cRowsConsole.controls[0].scroll_to(offset=-1, duration=2000, curve=ft.AnimationCurve.EASE_IN_OUT)

        self.page.update()

    def createAccountContainer(self):
        self.cPositions = ft.Container(
            bgcolor = "green",
            padding = 15,
            col = 6,
            content=ft.Column(controls=
                [
                    ft.Text("Posicion")
                ],
             
            )
        )
        self.cCommand = ft.TextField(
            label="Command:", 
            prefix_text= f"{self.account['broker']}->{self.account['wallet']}[{self.account['name']}]: ", 
            on_submit=self.sendCommand
            )
        
        self.cRowsConsole = ctrConsola()
        self.cRowsConsole.col = 12

        self.cConsoleOut = ft.Container(
            bgcolor="red",            
            padding = 15,            
            expand = True,
            col = 6,
            content = ft.ResponsiveRow(controls=
                [                    
                    self.cRowsConsole                    
                ]
            ),
            
        )                
        return ft.ResponsiveRow(
                controls=
                [
                    self.cConsoleOut,
                    self.cPositions                                    
                ], expand=True)

p = MainPage()
ft.app(target=p.main)
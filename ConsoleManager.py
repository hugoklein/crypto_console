import flet as ft
from ctrConsola import ctrConsola 

class ConsoleManager(ft.ResponsiveRow):
    def __init__(self, data):
        super().__init__()
        
        self.data = data
        self.console = ctrConsola(self.data)
        self.console.col = 7       
        self.console.on_click = self.setFocus        

        self.positions = ft.Text("Positions")
        self.positions.col = 5
        self.positions.bgcolor = "blue"

        self.cnt =   ft.ResponsiveRow(
            controls=[
                self.console,
                self.positions,
            ]        
        )  
    def build(self):
        return self.cnt
    
    def setFocus(self,e):
        self.console.setFocus()
    
    def clearConsole(self):
        self.console.clear()

    def onlyConsole(self):
        self.cnt.controls.clear()
        self.cnt.controls.append(self.console)
        self.update()
    
    def onlyPositions(self):
        self.cnt.controls.clear()
        self.cnt.controls.append(self.positions)    
        self.update()

    def both(self):
        self.cnt.controls.clear()
        self.cnt.controls.append(self.console)
        self.cnt.controls.append(self.positions)
        self.update()        

    def outText(self, text, dateVisible:bool=False):
        self.console.outText(text, dateVisible)
    
    def out(self, info, dateVisible:bool=False):
        self.console.out(info, dateVisible)


import flet as ft
import time
from datetime import datetime

class ctrConsola(ft.Container):
    def __init__(self,data):
        super().__init__()
        self.border_radius= 0
        self.data = data    
        self.BrokersLogos = {"Binance": f"assets/binance.png",
                             "Kucoin" : f"assets/kucoin.png",
                             "Balanz" : f"assets/balanz.webp" }

        
        self.lbPrompt = ft.Text(f"{self.data['broker']}>{self.data['wallet']}[{self.data['name']}]: ", font_family="Consolas", size=14, height=30, text_align=ft.TextAlign.LEFT )
        
        self.txtCommand = ft.TextField(   
            autofocus=True,         
            on_submit=self.onSendCommand,
            border = ft.InputBorder.NONE,
            height=10,
            text_style = ft.TextStyle(font_family="Consolas",size=14),
            text_size=14,
            text_vertical_align=ft.VerticalAlignment.START,            
            expand=True
            
        )
        self.lineCommand = ft.Row(spacing=1, height=18,
            controls = [
                self.lbPrompt,
                self.txtCommand
            ]
        )
 
        rows = ft.Column(scroll=ft.ScrollMode.AUTO,auto_scroll=True, spacing=1,
                    controls=[]                        
        )   
        self.lineas = rows.controls    
        self.content = rows
        
        self.lineas.append(self.consoleInfo())
        self.lineas.append(ft.Text(""))
        self.lineas.append(self.lineCommand)        

    def LogoKucoin(self):
        img =  ft.Image(            
            width=100,
            height=100,
            opacity=0.5,
            fit=ft.ImageFit.COVER,        
        )
        if self.data["broker"] in self.BrokersLogos :
            img.src = self.BrokersLogos[self.data["broker"]]
        return img

    def consoleInfo(self):
        img = self.LogoKucoin()   
        time.sleep(0.5)
        texts = ft.Column([
            ft.Text("Console Kucoin", size=18),
            ft.Text("Verision: 1.01", size=11),
            ft.Text("Account: hugo   Wallet: Future", color="yellow"),
        ])
        return ft.Row(
            controls=
            [
                img,                
                texts,                
            ],

        )

    
    def clear(self):
        self.lineas.clear()    
        self.lineas.append(self.consoleInfo())
        self.lineas.append(ft.Text(""))
        self.lineas.append(self.lineCommand)
        self.txtCommand.value= ""
        self.txtCommand.focus()
        self.update()
    
    def setFocus(self):
        self.txtCommand.focus()

    def getDateTimeText(self)->ft.Text:        
        date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        return  ft.Text("  " + date_time, font_family="Consolas", size=10, color="blue" )
    
    def outText(self, text, dateVisible:bool = False):
        txt = ft.Text( text, font_family="Consolas", size=14 )
        if dateVisible:
            lbd = self.getDateTimeText()
            self.lineas.insert(-1, ft.Row([txt,lbd]) )        
        else:
            self.lineas.insert(-1, txt )
        self.update()    
    
    def out(self, text, dateVisible:bool = False):        
        if dateVisible:
            lbd = self.getDateTimeText()
            self.lineas.insert(-1, ft.Row([text,lbd]) )        
        else:
            self.lineas.insert(-1, text )
        self.update()    

    def outError(self, text):
        txt = ft.Text( text, font_family="Consolas", size=14, color="red" )        
        lbd = self.getDateTimeText()
        self.lineas.insert(-1, ft.Row([txt,lbd]) )        
        self.update()    

        
    def onSendCommand(self, e):              
        txt = ft.Text( self.lbPrompt.value + self.txtCommand.value, font_family="Consolas", size=14 )
        if self.txtCommand.value != "":
            lbd = self.getDateTimeText()
            self.lineas.insert(-1, ft.Row([txt,lbd]) )            
        else:
            self.lineas.insert(-1, txt )
            self.txtCommand.focus()
            self.update()    
            return

        cmdResponse = self.executeCommand(self.txtCommand.value)
        if cmdResponse["error"] != "":
            self.outError(cmdResponse["error"])
            self.txtCommand.focus()
            self.update()    
            return
        

        if cmdResponse["executed"]:
            self.txtCommand.value = ""
            self.txtCommand.focus()
            self.update()    

    def executeCommand(self, cmd:str):
        response = {"error":"", "data": {}, "msg" : "", "executed":False }
        if cmd.lower() in ("cls", "clear"):
            self.clear()
            response["executed"] = True
            return response
        
        response["error"] = "invalid command"
        return response
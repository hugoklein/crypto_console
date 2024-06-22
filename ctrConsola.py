import flet as ft
import time

class ctrConsola(ft.Container):
    def __init__(self):
        super().__init__()
        self.border_radius= 0
    
        
        self.lbPrompt = ft.Text("Kucoin->Hugo: ", font_family="Consolas", size=14, height=30, text_align=ft.TextAlign.LEFT )
        
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
            src=f"assets/kucoin.png",
            width=100,
            height=100,
            opacity=0.2,
            fit=ft.ImageFit.COVER,        
        )

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
        
    def onSendCommand(self, e):      
        txt = ft.Text( self.lbPrompt.value + self.txtCommand.value, font_family="Consolas", size=14 )
        lbd = ft.Text( "  2021-06-18 15:02:00", font_family="Consolas", size=10, color="blue" )
        self.lineas.insert(-1, ft.Row([txt,lbd]) )
        self.txtCommand.value = ""
        self.txtCommand.focus()
        self.update()    
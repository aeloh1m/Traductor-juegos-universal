from PIL import Image, ImageGrab
import pytesseract
import cutlet
import os, time
import translators as ts
import translators.server as tss
import wx

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

global lenguaje_seleccionado

lenguaje_seleccionado = 'eng'


class Translator():
    def get_lines(self, x1, y1, x2, y2):
        bbox = (x1,y1,x2,y2)
        im = ImageGrab.grab(bbox)
        text_raw = pytesseract.image_to_string(im, lang=lenguaje_seleccionado, config='--psm 11')
        text = text_raw.replace('/','!')
        # Borrar espacios en blanco
        text = "\n".join([linea.rstrip() for linea in text.splitlines() if linea.strip()])
        lines = text.splitlines()
        return lines

    def start_reading(self, x1, y1, x2, y2):
        katsu = cutlet.Cutlet()
        katsu.use_foreign_spelling = False

        lines = ''

        while True:
            new_lines = self.get_lines(x1,y1,x2,y2)

            if lines != new_lines:
                os.system('cls')
                lines = new_lines
                for line in lines:
                    print(' 💬  ' + line  )
                    print(' 👀  ' + katsu.romaji(line))
                    print(' 🌍  ' + ts.translate_text(line, to_language="es"))
                    print("----------------------------------")
           
            time.sleep(0.1)


class DesktopController(wx.Frame):
    def __init__(self, parent, title):
        super(DesktopController, self).__init__(parent, title=title)
        self.SetTransparent(200)
        self.button = wx.Button(self)
        self.Bind(wx.EVT_BUTTON, self.on_button_click, self.button)

        self.SetPosition(wx.Point(0,0))
        self.Show()

        

        
        # Select bar options
        menuFile = wx.Menu()
        menuFile.Append(1, "&Cómo usar...")
        menuFile.AppendSeparator()
        menuFile.Append(2, "&Salir")

        menuTranslate = wx.Menu()
        menuTranslate.Append(3, "&Inglés...")
        menuTranslate.Append(3, "&Japonés...")

        # Selectable bar first section
        menuBar = wx.MenuBar()
        menuBar.Append(menuFile, "&Ayuda")
        menuBar.Append(menuTranslate, "&Traducir juego en idioma...")

        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText("¡Buen juego! @aeloh1m")
        
        # Binding
        self.Bind(wx.EVT_MENU, self.Help, id=1)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=2)
        self.Bind(wx.EVT_MENU, self.TranslateToJapanese, id=3)
    
    def TranslateToJapanese(self, event):
        global lenguaje_seleccionado

        if lenguaje_seleccionado == 'eng':
            lenguaje_seleccionado = 'jpn'
            wx.MessageBox("Ahora la casilla traducirá al Japonés", "¡Éxito!", wx.OK | wx.ICON_INFORMATION, self)
        else:
            lenguaje_seleccionado = 'eng'
            wx.MessageBox("Ahora la casilla traducirá al Inglés", "¡Éxito!", wx.OK | wx.ICON_INFORMATION, self)


    def OnQuit(self, event):
        self.Close()
         
    def Help(self, event):
        mensaje = 'Para utilizar el programa, usted deberá seleccionar el área que desee traducir, ampliando \n o achicando la ventana. Una vez seleccionada, clickear dentro de la misma.'
        wx.MessageBox(mensaje, "Ayuda", wx.OK | wx.ICON_INFORMATION, self)

    def on_button_click(self, event):
        print(self.button.Size)
        size = self.button.Size
        x1, y1 = self.button.GetScreenPosition()
        x2, y2 = x1 + size[0], y1 + size[1]
        print(x1,y1,x2,y2)
        self.Hide()
        # Iniciar traducción
        Translator().start_reading(x1,y1,x2,y2)


if __name__ == '__main__':
    app = wx.App()
    mf = DesktopController(None, title="Selecciona un área")
    app.MainLoop()

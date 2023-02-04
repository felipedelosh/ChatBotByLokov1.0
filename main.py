"""
FelipedelosH
2023

Chatbot By Loko
"""
from tkinter import *
from Controller import *

class Software:
    def __init__(self) -> None:
        self.controller = Controller()
        self.display_h = 400
        self.display_w = 360
        self.screem = Tk()
        self.canvas = Canvas(self.screem, height=self.display_h, width=self.display_w,  bg="gray20")
        self.femputadoraIMG = PhotoImage(file=self.controller.getIMGRouteOfFempuradora())
        self.lbl_name_femputadora = Label(self.canvas, text=self.controller.getNameFemputadora())
        self.chat_historial_area = Text(self.canvas, width=42, height=16, fg="white", bg="gray20")
        self.txt_user_entry = Entry(width=25, fg="white", bg="gray20")
        self.txt_user_entry.bind('<Key>', self.enterText)

        self.visualizeAndRun()

    def visualizeAndRun(self):
        self.screem.title("Chat with Femputadora")
        self.screem.geometry(str(self.display_w)+"x"+str(self.display_h))

        self.canvas.place(x=0, y=0)
        self.canvas.create_image(10, 10, image=self.femputadoraIMG, anchor=NW)
        self.lbl_name_femputadora.place(x=80, y=15)
        self.chat_historial_area.place(x=10, y=70)

        self.txt_user_entry.place(x=160, y=350)
        

        self.screem.mainloop()

    def updateChatHistorial(self):
        self.chat_historial_area.delete("1.0", "end")
        self.chat_historial_area.insert(END, self.controller.chat_historial)

    def clearInputTxt(self):
        self.txt_user_entry.delete(0, END)


    def enterText(self, event):
        if event.keysym == "Return":
            self.controller.insert_user_input(self.txt_user_entry.get())
            self.clearInputTxt()

        self.updateChatHistorial()
        

s = Software()
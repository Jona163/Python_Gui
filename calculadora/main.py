from customtkinter import CTkButton,CTk, CTkEntry
from tkinter import StringVar, PhotoImage
import customtkinter as ct

ct.set_appearance_mode("Dark")  

class CircularButton(CTkButton):
    def __init__(self, master=None, text='', command=None):
        super().__init__(master=master, text=text, command=command)
        self.configure(width=50, height=70, corner_radius=20,
            hover_color = ('#CCCCCC','#333333') ,
            fg_color = ('#7f5af0','#7f5af0'),
            text_font = ('Arial', 16)) # 
        self.grid(padx=5, pady=5, sticky='nsew')

def delete_last():
    global expression
    exp = expression.get()
    if exp:
        new_exp = exp[:-1]
        expression.set(new_exp)

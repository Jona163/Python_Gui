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


def calculate():
    global expression
    try:
        result = eval(expression.get())
        if isinstance(result, float):
            result = round(result, 3)
        expression.set(str(result))
    except Exception as e:
        expression.set("ERROR")

def toggle_mode():
    global mode
    if mode == "light":
        mode = "dark"
        button_mode.configure(image = img_light)         
        ct.set_appearance_mode("Dark")
        root.config(bg='black')
    else:
        mode = "light"
        button_mode.configure(image = img_dark )  
        ct.set_appearance_mode("Light")
        root.config(bg='white')

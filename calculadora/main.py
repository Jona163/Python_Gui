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


root = CTk()
root.geometry('375x500')
root.title('')
root.resizable(False, False)
root.call('wm', 'iconphoto', root._w, PhotoImage(file = 'images/logo.png'))
root.configure(bg="black")

mode = "dark" 
expression = StringVar() 
img_light = PhotoImage(file = 'images/sun.png')
img_dark = PhotoImage(file = 'images/moon.png')

button_mode = CTkButton(root, image = img_light , text='', 
    hover_color = ('white','black'),
    fg_color = ('white','black'),width=50, height=50,
    command= toggle_mode)
button_mode.grid(row=0, column=0)

# Autor: Jonathan Hernández
# Fecha: 25 Septiembre 2024
# Descripción: Código Python_GUI.
# GitHub: https://github.com/Jona163

from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, CTkCheckBox
from tkinter import PhotoImage

root = CTk() 
root.geometry("500x600+350+20")
root.minsize(480,500)
root.config(bg ='#010101')
root.title("Iniciar Sesion")

frame = CTkFrame(root, fg_color='#010101')
frame.grid(column=0, row = 0, sticky='nsew',padx=50, pady =50)

frame.columnconfigure([0,1], weight=1)
frame.rowconfigure([0,1,2,3,4,5], weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)



logo = PhotoImage(file='images/logo.png') 
img_google = PhotoImage(file='images/google.png')
img_facebook = PhotoImage(file='images/facebook.png')


CTkLabel(frame, image = logo).grid(columnspan=2, row=0)

correo = CTkEntry(frame,  text_font = ('sans serif',12), placeholder_text= 'Correo electronico', 
	border_color='#2cb67d', fg_color= '#010101',width =220,height=40)
correo.grid(columnspan=2, row=1,padx=4, pady =4)

contrasenna = CTkEntry(frame,show="*", text_font = ('sans serif',12), placeholder_text= 'Contraseña',
 border_color='#2cb67d', fg_color= '#010101', width =220,height=40)
contrasenna.grid(columnspan=2, row=2,padx=4, pady =4)

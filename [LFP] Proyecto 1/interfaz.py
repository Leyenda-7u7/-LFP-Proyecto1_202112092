from fileinput import filename
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter.tix import Tree
from tkinter import Tk
from tkinter import *
from tkinter import ttk
from analizadorlexico import instruccion, operar2, getErrores
import tkinter as tk
import webbrowser
import json
import os
import tempfile

class Pantalla_Principal():
    
        
    def __init__(self):
        self.PP = Tk()
        self.PP.title("Pantalla Principal")
        self.centrar(self.PP, 1200, 900)
        self.PP.configure(bg = "#102027")
        self.pantalla_1()
        
        
    def centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        anchura_pantalla= r.winfo_screenwidth()
        w = (anchura_pantalla // 2) - (ancho//2)
        e = (altura_pantalla // 2) - (alto//2)
        r.geometry(f"+{w}+{e}")
        
        
    def pantalla_1(self):
        self.Frame = Frame()
        self.Frame.config(bg ="purple4")
        self.Frame.config(bd=15)
        self.Frame.config(relief="sunken")  #Le da el borde
        self.Frame.config(cursor="hand2")
        self.Frame.pack(side=tk.LEFT, fill="x") 
        self.Frame.configure(height=800, width=625)

        
        Button(self.Frame, command=self.abrir_archivo ,text="Abrir Archivo", font=("Arial Black", 18), fg="AntiqueWhite3", bg="blue4", width=15).place(x=200, y=50)

        
        Button(self.Frame ,text="Guardar", command=self.guardar2 ,font=("Arial Black", 18),fg="AntiqueWhite3", bg="blue4", width=15).place(x=200, y=150)
        
        Button(self.Frame, command=self.guardar_como ,text="Guardar Como", font=("Arial Black", 18),fg="AntiqueWhite3", bg="blue4", width=15).place(x=200, y=250)
        
        Button(self.Frame, command=self.ejecutar ,text="Ejecutar", font=("Arial Black", 18), fg="AntiqueWhite3", bg="blue4", width=15).place(x=200, y=350)
        
        Button(self.Frame,text="Errores", command=self.getErrores, font=("Arial Black", 18), fg="AntiqueWhite3", bg="blue4", width=15).place(x=200, y=450)
        
        Button(self.Frame, text="Cerrar Ventana", command=self.PP.destroy, font=("Arial Black", 18), fg="AntiqueWhite3", bg="blue4", width=15).place(x=200, y=550)

        
        self.Frame = Frame()
        self.Frame.config(bg = "tan")
        self.Frame.config(bd=15)
        self.Frame.config(relief="sunken")  #Le da el borde
        self.Frame.config(cursor="hand2")
        self.Frame.pack(side=tk.RIGHT, fill="x")
        self.Frame.configure(height=800, width=580)


        
        Button(self.Frame,text="Manual Tecnico", command=self.abrir_manual_tecnico, font=("Arial Black", 18), fg="AntiqueWhite2", bg="azure4", width=15).place(x=200, y=50)
        
        Button(self.Frame ,text="Manual de Usuario", command=self.abrir_manual_usuario, font=("Arial Black", 18),fg="AntiqueWhite1", bg="azure4", width=15).place(x=200, y=150)
        
        Button(self.Frame,text="Ayuda", command=self.ayuda, font=("Arial Black", 18), fg="AntiqueWhite1", bg="azure4", width=15).place(x=200, y=250)
        
        self.text = Text(self.Frame, font=("Arial", 15), fg="black", width=45, height=8)
        self.text.place(x=50, y=350)
        
        
        self.resultado_text = Text(self.Frame, font=("Arial", 15), fg="black", width=30, height=6)
        self.resultado_text.place(x=130, y=600)
        

        
        self.Frame.mainloop() 
        

    def abrir_archivo(self):
        x = ""
        Tk().withdraw()
        try:
            filename = askopenfilename(title='Selecciona un archivo', filetypes=[('Archivos', f'*.json')])
            with open(filename, encoding='utf-8') as infile:
                x = infile.read()
                                            
        except: 
            print("Error, no se ha seleccionado ningun archivo")
            return
        
        self.texto = x
        self.text.insert('1.0', x)
        
    def ejecutar(self):
        instruccion(self.texto)
        respuestas = operar2()
        resultado = ""
        for respuesta in respuestas:
            resultado += str(respuesta.operar(None)) + "\n"
        self.resultado_text.insert('1.0',format(resultado))


    def abrir_manual_usuario(self):
        try:  
            path = 'https://acrobat.adobe.com/link/review?uri=urn:aaid:scds:US:af9e3749-2061-3661-861c-d1bebe7dc1eb'
            webbrowser.open_new(path)
        except:
            print("No se pudo abrir el archivo")
            
            
    def abrir_manual_tecnico(self):
        try:  
            path = 'https://acrobat.adobe.com/link/review?uri=urn:aaid:scds:US:19d97a09-77e1-3cca-9fb6-669e01469268'
            webbrowser.open_new(path)
        except:
            print("No se pudo abrir el archivo")

    
    def ayuda(self):
        try:  
            path = 'https://acrobat.adobe.com/link/review?uri=urn:aaid:scds:US:f21a58a0-47f1-3af9-ab92-698f030d4660'
            webbrowser.open_new(path)
        except:
            print("No se pudo abrir el archivo")
            

    def getErrores(self):
        lista_errores = getErrores()
        w = 1
        resultado = "{\n"
        while lista_errores:
            error = lista_errores.pop(0)
            resultado += error.operar(w) + "\n"
            w += 1
        resultado += "}"
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, resultado)
                
    def guardar_como(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if filename:
            with open(filename, "w", encoding="utf-8") as outfile:
                outfile.write(self.resultado_text.get("1.0", "end-1c"))

    def guardar2(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if filename:
            with open(filename, "w", encoding="utf-8") as outfile:
                outfile.write(self.resultado_text.get("1.0", "end-1c"))

r = Pantalla_Principal()




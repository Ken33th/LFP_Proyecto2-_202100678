from fileinput import filename
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from common.analizador import Scanner
import os

class panatalla_principal():
    os.system("cls")
    def __init__(self):
        global prinpage
        prinpage = tk.Tk()
        # prinpage = Tk()
        prinpage.title("Pantalla Principal Proyecto 2")
        self.centrar(prinpage, 800, 500)
        #color de fondo de ventana
        prinpage.configure(bg = "#800000")
        #panel de dentro
        self.Frame = tk.Frame(height=500, width=1100)
        self.Frame.config(bg = "#FF0000")
        self.Frame.pack(padx=10, pady=25)
        #primer panel
        Label(prinpage, text="Interactuar", font=("Times New Roman", 20), fg="white", bg= "#0000FF", width=10).place(x=30, y=10)
        self.area_texto = Text(prinpage,font=("Times New Roman", 17), fg="black", width=35, height=17)
        self.area_texto.place(x=30, y=60)
        scroll1 = Scrollbar(prinpage, command=self.area_texto.yview)    
        scroll1.place(x=420, y=61)
        #segundo panel
        Label(prinpage, text="Resultado", font=("Times New Roman", 20),fg="white", bg= "#0000FF", width=10).place(x=690, y=10)
        self.area_textoresult = Text(prinpage,font=("Times New Roman", 17), fg="black", width=35, height=17)
        self.area_textoresult.place(x=690, y=60)
        scroll1 = Scrollbar(prinpage, command=self.area_textoresult.yview)    
        scroll1.place(x=1080, y=61)
        
        def do_something():
            print("Haz algo aquí")

        
        def nuevo():
            """Pregunta al usuario si desea guardar los cambios antes de limpiar el editor."""
            if self.area_texto.edit_modified():
                response = messagebox.askquestion("Pregunta", "¿Desea guardar los cambios?")
            if response == "yes":
                guardarcomo()
            else:
                print("Deteniendo...")

            clear_editor()

        def clear_editor():
            """Limpia el área de edición de código."""
            self.area_texto.delete('1.0', tk.END)

        def guardarcomo():
            """Guarda el archivo con un nuevo nombre y ubicación."""
            file_path = asksaveasfilename(
                defaultextension='.json',
                filetypes = (
                    ('Text files', '*.txt,*.json'),
                    ('PDF files', '*.pdf'),
                    ('Image files', '*.jpg;*.png'),
                    ('All files', '*.*')
                )
            )
            if file_path:
                with open(file_path, 'w') as f:
                    f.write(self.area_texto.get('1.0', tk.END))

        def abrir():
            x = ""
            try:
                global filename
                filename = askopenfilename(title='Selecciona un Archivo', filetypes=[('All files', '*.*')])
                archivo_txt = open(filename, encoding='utf-8')
                x = archivo_txt.read().strip()
            except:
                mensaje_error = messagebox.showerror(title="Mensaje de Alerta", message="No ha cargado ningún archivo, verifique por favor")
                return
            self.texto = x
            self.area_texto.insert(END,self.texto)
            
            scanner = Scanner(x)
            tokens = scanner.scan()
            print(tokens)
        
        def salir():
            prinpage.destroy()

        def guardar_archivo(): 
            try:
                save_archivo = open(filename, "w", encoding="UTF-8")
                save_archivo.write(self.area_texto.get(1.0, "end-1c"))
                save_archivo.close()
                self.area_texto.delete(1.0, "end-1c")                  
                mensaje_exito = messagebox.showinfo(title="Mensaje de notificación", message="Se ha guardado con éxito el archivo")                                                  
            except: 
                mensaje_error = messagebox.showerror(title="Mensaje de Alerta", message="No se ha podido guardar el archivo, verifique por favor")

        def guardarComo_archivo(): 
            global texto
            texto = StringVar() 
            prinpage.withdraw()
            ventana_guardarComo = Toplevel()
            ventana_guardarComo.title("Guardar archivo como")
            ventana_guardarComo.geometry("400x190+500+150")
            
            def regresar():
                ventana_guardarComo.withdraw()
                prinpage.deiconify() 
                
            def save_comoArchivo():
                try:       
                    if texto.get() == '':
                        mensaje_espacio = messagebox.showerror(title="Mensaje de Alerta", message="No puede dejar en blanco el cuadro de texto")
                    else:                       
                        ventana_guardarComo.withdraw()
                        prinpage.deiconify()
                        save_archivoComo = open(texto.get()+".json", "w", encoding="UTF-8")
                        save_archivoComo.write(self.area_texto.get(1.0, "end-1c"))
                        save_archivoComo.close()
                        self.area_texto.delete(1.0, "end-1c")
                        texto.set("")
                        mensaje_exito = messagebox.showinfo(title="Mensaje de notificación", message="Se ha guardado con éxito el nuevo archivo")
                except: 
                    mensaje_error = messagebox.showerror(title="Mensaje de Alerta", message="No se ha podido guardar el archivo, verifique por favor")
            label_ruta = Label(ventana_guardarComo, text="Nombre del archivo:").place(x=25, y =40)    
            archivo_ruta = Entry(ventana_guardarComo, width=30, textvariable=texto).place(x=150, y =40)    
            btn_seleccionar = Button(ventana_guardarComo, text="Guardar", command=save_comoArchivo).place(x=160, y=120)
            btn_regresar = Button(ventana_guardarComo, text="Regresar", command=regresar).place(x=280, y=120) 

        def tablatokens():
            # prinpage.withdraw()
            # global ventana_abrir
            # ventana_abrir = Toplevel() 
            # global texto
            # texto = StringVar()    
            # # Add Buttons
            # ventana_abrir.title("Interactuar con un Archivo")
            # ventana_abrir.configure(bg = "#4169E1")
            # ventana_abrir.geometry("1200x600")
            # #primer panel
            # Label(ventana_abrir, text="Interactuar", font=("Times New Roman", 20), fg="#7FFFD4", bg= "#4169E1", width=10).place(x=10, y=10)
            # self.area_texto = Text(ventana_abrir,font=("Times New Roman", 17), fg="black", width=40, height=20)
            # self.area_texto.place(x=20, y=50)
            # scroll1 = Scrollbar(ventana_abrir, command=self.area_texto.yview)    
            # scroll1.place(x=470, y=50)
            # #segundo panel
            # Label(ventana_abrir, text="Resultado", font=("Times New Roman", 20), fg="#7FFFD4", bg= "#4169E1", width=10).place(x=700, y=10)
            # self.area_textoresult = Text(ventana_abrir,font=("Times New Roman", 17), fg="black", width=40, height=20)
            # self.area_textoresult.place(x=700, y=50)
            # scroll1 = Scrollbar(ventana_abrir, command=self.area_textoresult.yview)    
            # scroll1.place(x=1150, y=50)
            # btn_cargar = Button(ventana_abrir,command= self.cargar_archivo ,text="Cargar Archivo", font=("Times New Roman", 20), fg="#ffffff", bg= "#ff6f00", width=12).place(x=496, y=110)
            # btn_gdr = Button(ventana_abrir,command= self.guardar_archivo, text="Guardar", font=("Times New Roman", 20), fg="#ffffff", bg= "#ff6f00", width=12).place(x=496, y=190)
            # btn_gdrC = Button(ventana_abrir,command= self.guardarComo_archivo,text="Guardar Como", font=("Times New Roman", 20), fg="#ffffff", bg= "#ff6f00", width=12).place(x=496, y=270)
            # btn_eje = Button(ventana_abrir,command= self.ejecutar,text="Ejecutar", font=("Times New Roman", 20), fg="#ffffff", bg= "#ff6f00", width=12).place(x=496, y=350)
            # btn_regresar = Button(ventana_abrir,command= self.regresar, text="Regresar", font=("Times New Roman", 20), fg="#ffffff", bg= "#ff6f00", width=12).place(x=496, y=430)
            # # Execute Tkinter
            # ventana_abrir.mainloop()
            pass
        menubar = tk.Menu(prinpage)

        # Primer menú
        archivo_menu = tk.Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Nuevo", command=nuevo)
        archivo_menu.add_command(label="Abrir", command=abrir)
        archivo_menu.add_command(label="Guardar", command=guardar_archivo)
        archivo_menu.add_command(label="Guardar como", command=guardarComo_archivo)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=salir)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)

        # Segundo menú
        analisis_menu = tk.Menu(menubar, tearoff=0)
        analisis_menu.add_command(label="Analizar archivo", command=do_something)
        menubar.add_cascade(label="Análisis", menu=analisis_menu)

        # Tercer menú
        tokens_menu = tk.Menu(menubar, tearoff=0)
        tokens_menu.add_command(label="Ver tokens", command=tablatokens)
        menubar.add_cascade(label="Tokens", menu=tokens_menu)

        # Cuarto menú
        errores_menu = tk.Menu(menubar, tearoff=0)
        errores_menu.add_command(label="Ver tabla de errores", command=do_something)
        menubar.add_cascade(label="Errores", menu=errores_menu)

        prinpage.config(menu=menubar)
        prinpage.mainloop()

    def centrar(self,r, ancho, alto):
        altura_pantalla = r.winfo_screenheight()
        ancho_pantalla = r.winfo_screenwidth()
        x = (ancho_pantalla // 2) - (ancho//2)
        y = (altura_pantalla // 2) - (alto //2)
        r.geometry(f"+{x}+{y}")


r = panatalla_principal()
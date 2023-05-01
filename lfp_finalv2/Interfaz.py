from tkinter import *
from tkinter import ttk
import tkinter as tk
import codecs
from tkinter import filedialog, messagebox
from common.analizador import Scanner

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Pantalla principal Proyecto 2")
        self.area_sentencias = FALSE
        self.contenido = ""
        
        # Frame para alinear a la derecha
        self.frame = Frame(self.master)
        self.frame.pack(fill=BOTH, expand=YES)
        
        # Crear area de texto
        self.text_area = Text(self.frame)
        self.text_area.pack(side=LEFT, fill=BOTH, expand=YES)
        self.text_area.bind('<Motion>', self.mostrar_posicion_cursor) # Llamada a la función mostrar_posicion_cursor cuando el cursor se mueve
        self.text_area.configure(background='#00008B', foreground="White")
        


        # Crear etiqueta para mostrar la posición del cursor
        self.cursor_pos_label = Label(self.master, text="Posición del cursor: ")
        self.cursor_pos_label.pack(side=BOTTOM, anchor=W)

        # Crear menu
        self.menu_bar = Menu(self.master)

        # Menu Archivos
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Nuevo", command=self.nuevo_archivo)
        self.file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        self.file_menu.add_command(label="Guardar", command=self.guardar_archivo)
        self.file_menu.add_command(label="Guardar como", command=self.guardar_como_archivo)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.salir)
        self.menu_bar.add_cascade(label="Archivos", menu=self.file_menu)

        # Menu Analisis
        self.analysis_menu = Menu(self.menu_bar, tearoff=0)
        self.analysis_menu.add_command(label="Generar sentencias MongoDB", command=self.generar_sentencias_mongodb)
        self.menu_bar.add_cascade(label="Análisis", menu=self.analysis_menu)

        # Menu Tokens
        self.tokens_menu = Menu(self.menu_bar, tearoff=0)
        self.tokens_menu.add_command(label="Ver", command=self.ver_tokens)
        self.menu_bar.add_cascade(label="Tokens", menu=self.tokens_menu)

        # Menu Errores
        self.errors_menu = Menu(self.menu_bar, tearoff=0)
        self.errors_menu.add_command(label="Ver", command=self.ver_errores)
        self.menu_bar.add_cascade(label="Errores", menu=self.errors_menu)

        self.master.config(menu=self.menu_bar)

    def mostrar_posicion_cursor(self, event):
        """
        Función que muestra la posición del cursor en la etiqueta de la parte inferior izquierda de la ventana
        """
        pos = self.text_area.index(INSERT)  # Obtener la posición del cursor
        self.cursor_pos_label.config(text="Posición del cursor: " + pos)  # Actualizar el texto de la etiqueta

    def nuevo_archivo(self):
        if messagebox.askyesno("Guardar", "¿Desea guardar los cambios antes de crear un nuevo archivo?"):
            self.guardar_archivo()
        self.text_area.delete("1.0", END)
        if self.area_sentencias == TRUE:
            self.generated_text_area.pack_forget()
            self.area_sentencias = FALSE

    def abrir_archivo(self):
        # if messagebox.askyesno("Guardar", "¿Desea guardar los cambios antes de abrir un archivo?"):
        # self.guardar_archivo()
        archivo = filedialog.askopenfile(initialdir="/", title="Abrir archivo", filetypes=(("Archivos de texto", "*.txt"),))
        if archivo:
            try:
                self.contenido = archivo.read().strip()
                self.text_area.delete("1.0", END)
                self.text_area.insert(END, self.contenido)
            except UnicodeDecodeError:
                archivo.close()
                archivo = codecs.open(archivo.name, encoding='utf-8', errors='replace')
                self.contenido = archivo.read().strip()
                self.text_area.delete("1.0", END)
                self.text_area.insert(END, self.contenido)
            finally:
                archivo.close()
        if self.area_sentencias == TRUE:
            self.generated_text_area.pack_forget()
            self.area_sentencias = FALSE

    def guardar_archivo(self):
        if not self.text_area.get("1.0", END).strip():
            messagebox.showerror("Error", "No hay nada que guardar.")
            return

        if not self.archivo_actual:
            messagebox.showwarning("Advertencia", "No se ha guardado el archivo antes. Use guardar como.")
            return

        try:
            with open(self.archivo_actual, "w") as archivo:
                archivo.write(self.text_area.get("1.0", END))
            messagebox.showinfo("Éxito", "Archivo guardado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

    def guardar_como_archivo(self):
        """
        Función que guarda el contenido del área de texto en un archivo seleccionado por el usuario
        """
        # Abrir diálogo de guardar archivo
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        
        # Si el usuario ha seleccionado un archivo
        if archivo:
            # Escribir el contenido del área de texto en el archivo
            with open(archivo, "w") as f:
                f.write(self.text_area.get("1.0", END))

    def ver_tokens(self):
        # Crea una tabla de ejemplo
        tabla = [['No.', 'Token', 'Numero de Token', 'Lexema'],]

        # Crea una nueva ventana para mostrar la tabla
        tabla_window = tk.Toplevel(self.master)
        tabla_window.title("Tabla")

        # Crea el widget Treeview de la tabla
        tabla_tree = ttk.Treeview(tabla_window, columns=tabla[0], show='headings')
        for col in tabla[0]:
            tabla_tree.heading(col, text=col.title())
        for row in tabla[1:]:
            tabla_tree.insert('', 'end', values=row)
        tabla_tree.pack(fill='both', expand=True)

        # Ajusta el tamaño de la ventana al tamaño de la tabla
        tabla_width = sum([len(col) for col in tabla[0]]) * 10  # Ancho de la tabla
        tabla_height = len(tabla) * 20  # Alto de la tabla
        tabla_window.geometry('{}x{}'.format(tabla_width + 20, tabla_height + 50))
    

    def ver_errores(self, master):
        # Crea el widget Treeview de la tabla y lo oculta
        self.tabla_tree = ttk.Treeview(master, columns=['Nombre', 'Apellido', 'Edad'], show='headings')
        self.tabla_tree.heading('Nombre', text='Nombre')
        self.tabla_tree.heading('Apellido', text='Apellido')
        self.tabla_tree.heading('Edad', text='Edad')
        self.tabla_tree.pack_forget()

    def mostrar_tabla(self):
        # Crea una tabla de ejemplo
        tabla = [['Juan', 'Pérez', 35],
                ['María', 'González', 27],
                ['Pedro', 'Martínez', 42]]

        # Limpia la tabla anterior (si la hay)
        self.tabla_tree.delete(*self.tabla_tree.get_children())

        # Inserta los datos en la tabla
        for row in tabla:
            self.tabla_tree.insert('', 'end', values=row)

        # Muestra la tabla
        self.tabla_tree.pack(fill='both', expand=True)
        
    
    def salir(self):
        self.master.destroy()
    
    def generar_sentencias_mongodb(self):
        if self.contenido == "":
            messagebox.showerror("Error", f"No se ha cargado ningun archivo para generar sentencias")
        else:
            if self.area_sentencias == False:
                # Crear segunda area de texto para sentencias generadas
                self.area_sentencias = TRUE
                self.generated_text_area = Text(self.frame, state=NORMAL)
                self.generated_text_area.configure(background='#4682B4', foreground="White")
                self.generated_text_area.pack(side=LEFT, fill=BOTH, expand=YES)
                
                scanner = Scanner(self.contenido)
                tokens = scanner.scan()
                print(tokens)
                self.generated_text_area.insert(END, tokens)
            else:
                self.contenido_area = self.text_area.get("1.0", "end-1c")
                self.generated_text_area.delete("1.0", END)
                print(self.contenido_area)
                scanner = Scanner(self.contenido_area)
                tokens = scanner.scan()
                print(tokens)
                self.generated_text_area.insert(END, tokens)

root = Tk()
ventana = App(root)
root.mainloop()
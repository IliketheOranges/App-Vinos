import tkinter as tk
import pandas as pd
from tkinter import ttk, filedialog, messagebox

# Variables globales

excel_file_path = None


# Funciones para el menú

def open_file():
    
    global excel_file_path

    file_path = filedialog.askopenfilename(
        title="Selecciona un archivo Excel",
        filetypes=[("Archivos Excel", "*.xlsx *.xls")]
    )
    
    # Mensajes de confirmación
    if file_path:
        excel_file_path = file_path 
        messagebox.showinfo("Archivo seleccionado", f"Has seleccionado: {file_path}")

        dispplay_data(file_path)
    else:
        messagebox.showerror("Error", "No se ha seleccionado ningún archivo")
    



def dispplay_data(excel_file_path):
    try:

        tree = create_treeview()

        df = pd.read_excel(excel_file_path)

        for item in tree.get_children():
            tree.delete(item)

        # Configurar las columnas del Treeview en función del Excel
        tree["columns"] = list(df.columns)
        tree["show"] = "headings"  # Solo mostrar encabezados

        # Definir encabezados y ancho de las columnas
        for col in df.columns:
            tree.heading(col, text=col)  
            tree.column(col, width=100) 

        # Agregar las filas al Treeview
        for index, row in df.iterrows():
            tree.insert("", "end", values=list(row))

    except Exception as e:
        messagebox.showerror("Error", f"No se ha podido leer correctamente: {e}")

# Crear TreeView

def create_treeview():
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    tree = ttk.Treeview(frame)
    tree.pack(side="left", fill="both", expand=True)

    scrollbar_y = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar_y.pack(side="right", fill="y")
    tree.configure(yscroll=scrollbar_y.set)
    return(tree)


# Crear ventanta

root = tk.Tk()
root.geometry("1280x720")
root.title("Aplicación de Vinos")

# Barra de menú

menubar = tk.Menu(root)

# Menú de archivo 

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Abrir archivo", command=open_file)
menubar.add_cascade(label="Archivo", menu=file_menu)
root.config(menu=menubar)

# Ejecutar la aplicación
root.mainloop()

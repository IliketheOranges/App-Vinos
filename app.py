import tkinter as tk
from tkinter import filedialog, messagebox

# Funciones para el menú

def open_file():
    file_path = filedialog.askopenfilename(
        title="Selecciona un archivo Excel",
        filetypes=[("Archivos Excel", "*.xlsx *.xls")]
    )

# Crear ventanta
root = tk.Tk()
root.geometry("644x434")
root.title("Aplicación de Vinos")

# Barra de menú
menubar = tk.Menu(root)

# Menú de archivo 
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Abrir archivo", command=open_file)
menubar.add_cascade(label="Archivo", menu=file_menu)

# Asignar la barra de menú a la ventana principal
root.config(menu=menubar)

# Ejecutar la aplicación
root.mainloop()

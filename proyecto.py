"""
Estructura de la Aplicacion:
Este programa esta estructurado de la siguiente manera: Primero creamos la clase TaskManager que sera la encargada de guarda tanto la logica como la dispociosion de nuetra
ventana (la lista de almacenaje para las tareas, un Entry par, los botones que se usaran al agregar, eliminar o marcar como completada la tarea.)
Posterior a esta clase codifique las funciones que llevaran a cabo las acciones correspondientes de los botones antes mencionados. 
Elegi este proytecto porque se me hizo el que mas util puede ser a mis necesidades
"""


import tkinter as tk
from tkinter import messagebox

# Creamos la clase de logica 
class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        
        # Creamos la estructura de los widgets
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        #Creamos la lista para almacenar las tareas
        self.task_listbox = tk.Listbox(self.frame, height=10, width=50)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        #Programamos la barra del scroll
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        
        #Creamos el espacio para las nuevas tareas
        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(padx=10, pady=10, fill=tk.X)
        
        self.entry = tk.Entry(self.entry_frame, width=40)
        self.entry.pack(side=tk.LEFT, padx=5, pady=5)
        
        #Agregamos el boton para las sumar tareas
        self.add_button = tk.Button(self.entry_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Agregamos el boton para borrar la tarea que tengamos seleccionada
        self.delete_button = tk.Button(self.entry_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        #Agregamos el boton para marcar como completada la tarea seleccionada
        self.complete_button = tk.Button(self.entry_frame, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=5, pady=5)

    # Funcion para eliminar la tarea seleccionada
    def add_task(self):
        task = self.entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Ingrese una tarea antes de añadirla.")
    
    # Funcion para eliminar la tarea seleccionada
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.task_listbox.delete(selected_index)
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")
    
    # Funcion para marcar una tarea como completada
    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            current_text = self.task_listbox.get(selected_index)
            if not current_text.startswith("[Completada]"):
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, f"[Completada] {current_text}")
            else:
                messagebox.showinfo("Información", "La tarea ya está marcada como completada.")
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()


import tkinter as tk
from tkinter import messagebox
from servicios.tarea_servicio import TareaServicio

class AppTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.servicio = TareaServicio()
        tk.Label(root, text="Lista de Tareas (usa teclado o mouse)", font=("Arial", 12)).pack(pady=5)
        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        # Enter → agregar tarea
        self.entry.bind("<Return>", self.agregar_tarea_evento)
        # Lista de tareas
        self.lista = tk.Listbox(root, width=50)
        self.lista.pack(pady=10)
        # Doble clic para completar
        self.lista.bind("<Double-1>", self.marcar_completado_evento)
        # Botones con atajos visibles
        tk.Button(root, text="Agregar tarea (Enter)", command=self.agregar_tarea).pack(pady=5)
        tk.Button(root, text="Completar (C)", command=self.marcar_completada).pack(pady=5)
        tk.Button(root, text="Eliminar (D)", command=self.eliminar_tarea).pack(pady=5)
        tk.Button(root, text="Salir (Esc)", command=self.root.quit).pack(pady=5)
        # agregamos los atajos del teclado
        self.root.bind("<c>", self.marcar_completada_evento)
        self.root.bind("<C>", self.marcar_completada_evento)
        self.root.bind("<d>", lambda event: self.eliminar_tarea())
        self.root.bind("<D>", lambda event: self.eliminar_tarea())
        self.root.bind("<Delete>", lambda event: self.eliminar_tarea())
        self.root.bind("<Escape>", lambda event: self.root.quit())
    #agregamos las funciones

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for tarea in self.servicio.obtener_tareas():
            texto = tarea.descripcion
            if tarea.completado:
                texto = "[✔] " + texto
            else:
                texto = "[ ] " + texto
            self.lista.insert(tk.END, f"{tarea.id}. {texto}")
    def agregar_tarea(self):
        texto = self.entry.get()
        if texto:
            self.servicio.agregar_tarea(texto)
            self.entry.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showerror("Error", "Por favor escribe una tarea")

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def obtener_id_seleccionado(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            return None
        item = self.lista.get(seleccion)
        return int(item.split(".")[0])

    def marcar_completado_evento(self, event):
        self.marcar_completada()

    def marcar_completada(self):
        id_tarea = self.obtener_id_seleccionado()
        if id_tarea:
            self.servicio.completar_tarea(id_tarea)
            self.actualizar_lista()

    def marcar_completada_evento(self, event):
        self.marcar_completada()

    def eliminar_tarea(self):
        id_tarea = self.obtener_id_seleccionado()
        if id_tarea:
            self.servicio.eliminar_tarea(id_tarea)
            self.actualizar_lista()
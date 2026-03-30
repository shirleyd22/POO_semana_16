import tkinter as tk
from ui.app_tkinter import AppTkinter

if __name__ == "__main__":
    root = tk.Tk()
    app = AppTkinter(root)
    app.actualizar_lista()
    root.mainloop()
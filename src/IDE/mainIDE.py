from src.combinerClass import Editor
import tkinter as tk

# Main
window = tk.Tk()
editor = Editor(window)
editor.pack(side="top", fill="both", expand=True)
editor.SetGUI(window)
window.mainloop()

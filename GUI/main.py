import customtkinter as tk
import ttkbootstrap as ttk

tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("Arranha Application")
        master.geometry("1200x600")
        
        ##define window here i.e. menus etc.
    
    def close_application(self):
        self.master.destroy()
        
#create main window
root = tk.CTk()

my_gui = MyGUI(root)

root.mainloop()
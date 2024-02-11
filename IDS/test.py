import tkinter as tk
# from tkinter import messagebox as tkMessageBox
class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("My GUI")
        master.geometry("300x300")

        # Create a menu bar
        self.menu_bar = tk.Menu(master)

        # Create a 'main' menu
        self.main_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Main", menu=self.main_menu)

        # Create a 'App' submenu with a 'Close' option
        self.app_submenu = tk.Menu(self.main_menu, tearoff=0)
        self.app_submenu.add_command(label="Close", command=self.close_application)
        self.main_menu.add_cascade(label="App", menu=self.app_submenu)

        # Set the menu bar for the window
        master.config(menu=self.menu_bar)

    def close_application(self):
        self.master.destroy()

# Create the main window
root = tk.Tk()

# Instantiate the MyGUI class
my_gui = MyGUI(root)

# Run the Tkinter event loop
root.mainloop()

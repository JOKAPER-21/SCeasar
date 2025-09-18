import os
import tkinter as tk

# Change working directory to the script's folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from ui import ProjectSetupApp

if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectSetupApp(root)
    root.mainloop()

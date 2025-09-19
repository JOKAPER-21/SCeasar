import os
import sys
import tkinter as tk

from ui import ProjectSetupApp

if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectSetupApp(root, default_root=r"P:\SProjects")  # <-- force default root
    root.mainloop()

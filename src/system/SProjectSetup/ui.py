import tkinter as tk
from tkinter import messagebox, filedialog
import shutil
import json, os
from logic.folders import create_folders
from datetime import datetime
from tkcalendar import DateEntry  # For selectable date

# Load config
with open("config/settings.json") as f:
    settings = json.load(f)

with open("config/theme.json") as f:
    theme = json.load(f)


class ProjectSetupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SProject Setup")
        self.root.configure(bg=theme["colors"]["bg"])

        # Make window full screen
        self.root.attributes('-fullscreen', True)

        # ---- Title ----
        tk.Label(root, text="S PROJECT SETUP",
                 font=("Poppins", 18, "bold"),
                 fg=theme["colors"]["title"],
                 bg=theme["colors"]["bg"]).pack(pady=20)

        # ---- Project Name ----
        tk.Label(root, text="Project Name:",
                 bg=theme["colors"]["bg"], fg=theme["colors"]["fg"]).pack()
        self.project_name_var = tk.StringVar()
        tk.Entry(root, textvariable=self.project_name_var, font=("Poppins", 14)).pack(pady=5)

        # ---- Selectable Date ----
        tk.Label(root, text="Select Date:",
                 bg=theme["colors"]["bg"], fg=theme["colors"]["fg"]).pack(pady=(10, 0))
        self.date_entry = DateEntry(
            root,
            width=12,
            background='darkblue',
            foreground='white',
            borderwidth=2,
            date_pattern='yy/mm/dd'  # Valid date format
        )
        self.date_entry.set_date(datetime.today())  # Default date
        self.date_entry.pack(pady=5)

        # ---- Root Folder ----
        tk.Label(root, text="Root Folder:",
                 bg=theme["colors"]["bg"], fg=theme["colors"]["fg"]).pack()
        self.root_path_var = tk.StringVar(value=os.getcwd())
        frame = tk.Frame(root, bg=theme["colors"]["bg"])
        frame.pack(pady=5)
        tk.Entry(frame, textvariable=self.root_path_var, width=50, font=("Poppins", 12)).pack(side="left", padx=5)
        tk.Button(frame, text="Browse", command=self.browse_root,
                  bg=theme["colors"]["button_bg"], fg=theme["colors"]["fg"], font=("Poppins", 12)).pack(side="left")

        # ---- Software checkboxes ----
        self.software_vars = {}
        container = tk.Frame(root, bg=theme["colors"]["bg"])
        container.pack(pady=20, fill="both", expand=True)

        left_col = ["ref", "mod", "tex", "uv", "lkd"]
        right_col = ["ani", "fx", "cmp", "edt"]

        def build_column(column, side):
            col_frame = tk.Frame(container, bg=theme["colors"]["bg"])
            col_frame.pack(side=side, padx=50, anchor="n")

            for cat in column:
                tk.Label(col_frame, text=settings.get("display_names", {}).get(cat, cat.title()),
                         font=("Poppins", 14, "bold"),
                         fg=theme["colors"]["title"], bg=theme["colors"]["bg"]).pack(anchor="w", pady=(10, 0))

                for sw in settings["software_templates"][cat]:
                    var = tk.BooleanVar(value=sw.get("default", False))
                    chk = tk.Checkbutton(col_frame, text=sw["name"], variable=var,
                                         font=("Poppins", 12),
                                         fg=theme["colors"]["fg"],
                                         bg=theme["colors"]["bg"],
                                         activebackground=theme["colors"]["bg"],
                                         selectcolor=theme["colors"]["bg"])
                    chk.pack(anchor="w", padx=10)
                    self.software_vars[f"{sw['name']}_{cat}"] = {
                        "var": var,
                        "from": sw["from"],
                        "to": sw["to"],
                        "category": cat
                    }

        build_column(left_col, "left")
        build_column(right_col, "right")

        # ---- Create Project button ----
        tk.Button(root, text="Create Project", command=self.create_project,
                  bg=theme["colors"]["button_bg"], fg=theme["colors"]["fg"], font=("Poppins", 14)).pack(pady=20)

    def browse_root(self):
        folder = filedialog.askdirectory(title="Select Root Project Folder")
        if folder:
            self.root_path_var.set(folder)

    def create_project(self):
        project_name = self.project_name_var.get().strip()
        if not project_name:
            messagebox.showerror("Error", "Enter project name!")
            return

        # Get selected date from calendar
        folder_date = self.date_entry.get_date().strftime("%y%m%d")
        base_path = os.path.join(self.root_path_var.get(), f"{folder_date}_{project_name}")
        os.makedirs(base_path, exist_ok=True)

        # Create folder structure
        create_folders(base_path, settings["folders"])

        # Copy selected software templates with versioning
        errors = []
        for _, info in self.software_vars.items():
            if info["var"].get():
                src = info["from"]
                category = info["category"]
                dest_folder = os.path.join(base_path, *info["to"])
                os.makedirs(dest_folder, exist_ok=True)
                ext = os.path.splitext(src)[1]

                # Determine next version
                existing_versions = []
                if os.path.exists(dest_folder):
                    for f in os.listdir(dest_folder):
                        if f.startswith(f"{project_name}_{category}_v") and f.endswith(ext):
                            ver_str = f.split("_v")[-1].split(ext)[0]
                            try:
                                existing_versions.append(int(ver_str))
                            except:
                                pass
                next_ver = max(existing_versions) + 1 if existing_versions else 1

                # Destination filename
                dest_file = os.path.join(dest_folder, f"{project_name}_{category}_v{next_ver:02d}{ext}")

                # Copy the template
                try:
                    shutil.copy2(src, dest_file)
                except Exception as e:
                    errors.append(f"{src} → {dest_file}: {str(e)}")

        # Final message
        if errors:
            messagebox.showwarning("Project Created with Warnings",
                                   f"Project created at:\n{base_path}\n\nSome templates failed:\n" +
                                   "\n".join(errors))
        else:
            messagebox.showinfo("Success", f"Project created successfully at:\n{base_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ProjectSetupApp(root)
    root.mainloop()

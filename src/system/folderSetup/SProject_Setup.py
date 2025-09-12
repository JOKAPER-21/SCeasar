import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
import os
import shutil

# ---------------- GUI Setup -----------------
root = tk.Tk()
root.title("SPROJECT SETUP - powered by Jokaper21")

# Window size
window_width = 550
window_height = 800

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position x, y to center the window
position_x = int((screen_width / 2) - (window_width / 2))
position_y = int((screen_height / 2) - (window_height / 2))

# Set window size + position
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
root.resizable(False, False)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# -------- Title & Inputs --------
tk.Label(root, text="S PROJECT SETUP", font=("Helvetica", 18, "bold")).grid(
    row=0, column=0, columnspan=2, pady=20
)

tk.Label(root, text="Project Name:", font=("Helvetica", 12)).grid(
    row=1, column=0, columnspan=2, pady=5
)
entry_project = tk.Entry(root, font=("Helvetica", 12), justify="center")
entry_project.grid(row=2, column=0, columnspan=2, pady=5, ipadx=100)

tk.Label(root, text="Select Date:", font=("Helvetica", 12)).grid(
    row=3, column=0, columnspan=2, pady=5
)
date_entry = DateEntry(
    root,
    width=10,
    background="darkblue",
    foreground="white",
    borderwidth=4,
    font=("Helvetica", 12),
)
date_entry.grid(row=4, column=0, columnspan=2, pady=5)

# -------- Folder Structure --------
folders_to_create = [
    ["scene", "reference"],
    ["scene", "downloads"],
    ["scene", "reference"],

    ["scene", "export", "3mf"],
    ["scene", "export", "fbx"],
    ["scene", "export", "gltf"],
    ["scene", "export", "obj"],
    ["scene", "export", "stl"],
    ["scene", "export", "usd"],

    ["scene", "renderOutput", "image", "blender"],
    ["scene", "renderOutput", "image", "photoshop"],
    ["scene", "renderOutput", "imageSeq"],
    ["scene", "renderOutput", "video"],
    ["scene", "renderOutput", "showcase"],

    ["scene", "textures", "cgTextures"],
    ["scene", "textures", "compTextures"],

    ["scene", "workfile", "mod", "blender"],
    ["scene", "workfile", "mod", "rhino"],
    ["scene", "workfile", "mod", "zbrush"],
    ["scene", "workfile", "tex", "illustrator"],
    ["scene", "workfile", "tex", "photoshop"],
    ["scene", "workfile", "tex", "substancePainter"],
    ["scene", "workfile", "uv", "blender"],
    ["scene", "workfile", "uv", "rizomuv"],
    ["scene", "workfile", "lkd", "blender"],
    ["scene", "workfile", "ani", "blender"],
    ["scene", "workfile", "fx", "aftereffects"],
    ["scene", "workfile", "fx", "houdini"],
    ["scene", "workfile", "cmp", "photoshop"],
    ["scene", "workfile", "edt", "davinci"]
]

# -------- Software Templates --------
software_categories = {
    "ref": [
        {
            "name": "PureRef",
            "from": r"S:\Pipeline\Softwares_Templates\pureRef_Template\2.0.3\PureRef_2.0.3_Basic_setting.pur",
            "to": ["scene", "reference"],
            "default": True,
        }
    ],
    "mod": [
        {
            "name": "Blender",
            "from": r"S:\Pipeline\Softwares_Templates\blender_Template\4.5\Blender_4.5_Basic_setting.blend",
            "to": ["scene", "workfile", "mod", "blender"],
            "default": True,
        },
        {
            "name": "Rhino",
            "from": r"S:\Pipeline\Softwares_Templates\rhino_Template\2024\rhino2024_Basic_setting.3dm",
            "to": ["scene", "workfile", "mod", "rhino"],
            "default": False,
        },
        {
            "name": "Zbrush",
            "from": r"S:\Pipeline\Softwares_Templates\zbrush_Template\2024\zbrush2024_Basic_setting.zpr",
            "to": ["scene", "workfile", "mod", "zbrush"],
            "default": False,
        },
    ],
    "tex": [
        {
            "name": "Illustrator",
            "from": r"S:\Pipeline\Softwares_Templates\illustrator_Template\2021\Illustrator_2021_Basic_setting.ai",
            "to": ["scene", "workfile", "tex", "illustrator"],
            "default": False,
        },
        {
            "name": "Photoshop",
            "from": r"S:\Pipeline\Softwares_Templates\photoshop_Template\2021\Photoshop_2021_Basic_setting.psd",
            "to": ["scene", "workfile", "tex", "photoshop"],
            "default": False,
        },
        {
            "name": "substancePainter",
            "from": r"S:\Pipeline\Softwares_Templates\substancePainter_Template\2024\substancePainter_2024_Basic_setting.exe",
            "to": ["scene", "workfile", "tex", "substancePainter"],
            "default": True,
        },
    ],
    "uv": [
        {
            "name": "Blender",
            "from": r"S:\Pipeline\Softwares_Templates\blender_Template\4.5\Blender_4.5_Basic_setting.blend",
            "to": ["scene", "workfile", "uv", "blender"],
            "default": False,
        },
        {
            "name": "RizomUV",
            "from": r"S:\Pipeline\Softwares_Templates\rizomuv_Template\2024\RizomUV VS RS 2024.0_Basic_setting.lnk",
            "to": ["scene", "workfile", "uv", "rizomuv"],
            "default": True,
        },
    ],
    "lkd": [
        {
            "name": "Blender",
            "from": r"S:\Pipeline\Softwares_Templates\blender_Template\4.5\Blender_4.5_Basic_setting.blend",
            "to": ["scene", "workfile", "lkd", "blender"],
            "default": True,
        },
    ],
    "ani": [
        {
            "name": "Blender",
            "from": r"S:\Pipeline\Softwares_Templates\blender_Template\4.5\Blender_4.5_Basic_setting.blend",
            "to": ["scene", "workfile", "ani", "blender"],
            "default": False,
        }
    ],
    "fx": [
        {
            "name": "Blender",
            "from": r"S:\Pipeline\Softwares_Templates\blender_Template\4.5\Blender_4.5_Basic_setting.blend",
            "to": ["scene", "workfile", "fx", "blender"],
            "default": False,
        },
        {
            "name": "AfterEffects",
            "from": r"S:\Pipeline\Softwares_Templates\aftereffects_Template\2023\aftereffects_2023_Basic_setting.aep",
            "to": ["scene", "workfile", "fx", "aftereffects"],
            "default": False,
        },
        {
            "name": "Houdini",
            "from": r"S:\Pipeline\Softwares_Templates\houdini_Template\19.5\houdini_19.5_Basic_setting.hip",
            "to": ["scene", "workfile", "fx", "houdini"],
            "default": False,
        },
    ],
    "cmp": [
        {
            "name": "Photoshop",
            "from": r"S:\Pipeline\Softwares_Templates\photoshop_Template\2021\Photoshop_2021_Basic_setting.psd",
            "to": ["scene", "workfile", "cmp", "photoshop"],
            "default": True,
        }
    ],
    "edt": [
        {
            "name": "AfterEffects",
            "from": r"S:\Pipeline\Softwares_Templates\aftereffects_Template\2023\aftereffects_2023_Basic_setting.aep",
            "to": ["scene", "workfile", "edt", "aftereffects"],
            "default": False,
        }
    ],
}

# -------- Friendly Display Names --------
display_names = {
    "ref": "Reference",
    "mod": "Modeling",
    "tex": "Texture",
    "uv": "UV",
    "lkd": "LookDev",
    "ani": "Animation",
    "fx": "Fx",
    "cmp": "Compositing",
    "edt": "Editorial",
}

left_column = ["ref", "mod", "tex", "uv", "lkd"]
right_column = ["ani", "fx", "cmp", "edt"]

software_vars = {}

# -------- Left-aligned Checkboxes --------
row_start = 5
for idx, cat in enumerate(left_column):
    softwares = software_categories.get(cat, [])
    tk.Label(root, text=f"{display_names[cat]}", font=("Helvetica", 12, "bold")).grid(
        row=row_start + idx * 4,
        column=0,
        sticky="w",
        padx=50,
        pady=(10, 0),
    )
    for i, sw in enumerate(softwares):
        var = tk.BooleanVar(value=sw.get("default", True))
        chk = tk.Checkbutton(
            root, text=sw["name"], variable=var, font=("Helvetica", 11)
        )
        chk.grid(row=row_start + idx * 4 + i + 1, column=0, sticky="w", padx=50, pady=2)
        software_vars[sw["name"] + "_" + cat] = {
            "var": var,
            "from": sw["from"],
            "to": sw["to"],
            "category": cat,
        }

for idx, cat in enumerate(right_column):
    softwares = software_categories.get(cat, [])
    tk.Label(root, text=f"{display_names[cat]}", font=("Helvetica", 12, "bold")).grid(
        row=row_start + idx * 4,
        column=1,
        sticky="w",
        padx=50,
        pady=(10, 0),
    )
    for i, sw in enumerate(softwares):
        var = tk.BooleanVar(value=sw.get("default", True))
        chk = tk.Checkbutton(
            root, text=sw["name"], variable=var, font=("Helvetica", 11)
        )
        chk.grid(row=row_start + idx * 4 + i + 1, column=1, sticky="w", padx=50, pady=2)
        software_vars[sw["name"] + "_" + cat] = {
            "var": var,
            "from": sw["from"],
            "to": sw["to"],
            "category": cat,
        }

# -------- Versioning Helper --------
def get_next_version(dest_folder, project_name, category, ext, formatted_date):
    """Determine the next version number based on existing files, starting from v01."""
    existing_versions = []
    if os.path.exists(dest_folder):
        for f in os.listdir(dest_folder):
            if f.startswith(f"{formatted_date}_{project_name}_{category}_v") and f.endswith(ext):
                ver_str = f.split("_v")[-1].split(ext)[0]
                try:
                    existing_versions.append(int(ver_str))
                except:
                    pass
    next_ver = max(existing_versions) + 1 if existing_versions else 1  # start from 1
    return f"v{next_ver:02d}"

# -------- Submit Function --------
def submit_form():
    project_name = entry_project.get().strip()
    if not project_name:
        messagebox.showerror("Error", "Project name is required!")
        return

    date_object = date_entry.get_date()
    formatted_date = date_object.strftime("%y%m%d")
    base_path = os.path.join(os.getcwd(), f"{formatted_date}_{project_name}")

    error_log = []

    # Create all folders
    for path in folders_to_create:
        try:
            folder_path = os.path.join(base_path, *path)
            os.makedirs(folder_path, exist_ok=True)
        except Exception as e:
            error_log.append(f"Failed to create folder {os.path.join(*path)}: {str(e)}")

    # Copy selected software templates with versioning
    for name, info in software_vars.items():
        if info["var"].get():
            src = info["from"]
            category = info["category"]
            dest_folder = os.path.join(base_path, *info["to"])
            os.makedirs(dest_folder, exist_ok=True)
            ext = os.path.splitext(src)[1]
            version_str = get_next_version(dest_folder, project_name, category, ext, formatted_date)
            dest_file = os.path.join(
                dest_folder, f"{formatted_date}_{project_name}_{category}_{version_str}{ext}"
            )
            try:
                shutil.copy2(src, dest_file)
            except Exception as e:
                error_log.append(
                    f"Failed to copy {name} from {src} to {dest_file}: {str(e)}"
                )

    if error_log:
        messagebox.showerror("Errors Occurred", "\n".join(error_log))
    else:
        messagebox.showinfo(
            "Success", f"Project created successfully:\n{base_path}"
        )

# -------- Submit Button --------
tk.Button(
    root,
    text="Create Project",
    font=("Helvetica", 12),
    bg="green",
    fg="white",
    command=submit_form,
).grid(row=50, column=0, columnspan=2, pady=20)

root.mainloop()

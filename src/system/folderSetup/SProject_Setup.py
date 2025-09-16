import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime
import os
import shutil

# ---------------- Colors -----------------
BG_COLOR = "#0C0D10"        # Background
TITLE_COLOR = "#b342ff"     # Section titles
LABEL_COLOR = "white"         # Labels
CHK_COLOR = "white"           # Checkboxes text
ENTRY_BG = "#FFFFFF"        # Entry background
ENTRY_FG = "black"            # Entry text
BTN_BG = "#008013"          # Button background
BTN_FG = "white"              # Button text

# ---------------- GUI Setup -----------------
root = tk.Tk()
root.title("SPROJECT SETUP - powered by Jokaper21")
root.configure(bg=BG_COLOR)

window_width = 550
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_x = int((screen_width / 2) - (window_width / 2))
position_y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
root.resizable(False, False)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# -------- Title & Inputs --------
tk.Label(root, text="S PROJECT SETUP", font=("Poppins", 18, "bold"), fg=TITLE_COLOR, bg=BG_COLOR).grid(
    row=0, column=0, columnspan=2, pady=20
)

tk.Label(root, text="Project Name", font=("Poppins", 12), fg=LABEL_COLOR, bg=BG_COLOR).grid(
    row=1, column=0, columnspan=2, pady=5
)
entry_project = tk.Entry(root, font=("Poppins", 12), justify="center", bg=ENTRY_BG, fg=ENTRY_FG, insertbackground="white")
entry_project.grid(row=2, column=0, columnspan=2, pady=5, ipadx=100, ipady=8)

tk.Label(root, text="Select Date", font=("Poppins", 12), fg=LABEL_COLOR, bg=BG_COLOR).grid(
    row=3, column=0, columnspan=2, pady=5
)
date_entry = DateEntry(
    root,
    width=10,
    background="#1C1E21",
    foreground="white",
    borderwidth=4,
    font=("Helvetica", 12),
)
date_entry.grid(row=4, column=0, columnspan=2, pady=5)

# -------- Folder Structure --------
folders_to_create = [  
    ["dev"],
    
    ["download"],
    
    ["scene", "reference"],

    ["scene", "export", "3mf"],
    ["scene", "export", "fbx"],
    ["scene", "export", "gltf"],
    ["scene", "export", "obj"],
    ["scene", "export", "stl"],
    ["scene", "export", "usd"],

    ["scene", "render", "image", "blender"],
    ["scene", "render", "image", "photoshop"],
    ["scene", "render", "imageSeq"],
    ["scene", "render", "video"],
    ["scene", "render", "showcase"],

    ["scene", "texture", "cgTexture"],
    ["scene", "texture", "compTexture"],

    ["scene", "workfile", "mod", "blender"],
    ["scene", "workfile", "mod", "blender", "export", "fbx"],
    ["scene", "workfile", "mod", "blender", "render"],
    ["scene", "workfile", "mod", "rhino"],
    ["scene", "workfile", "mod", "zbrush"],
    ["scene", "workfile", "tex", "illustrator"],
    ["scene", "workfile", "tex", "photoshop"],
    ["scene", "workfile", "tex", "substancePainter"],
    ["scene", "workfile", "uv", "blender"],
    ["scene", "workfile", "uv", "blender", "export", "fbx"],
    ["scene", "workfile", "uv", "blender", "render"],
    ["scene", "workfile", "uv", "rizomuv"],
    ["scene", "workfile", "lkd", "blender"],
    ["scene", "workfile", "lkd", "blender", "export", "fbx"],
    ["scene", "workfile", "lkd", "blender", "render"],
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
            "from": r"S:\Pipeline\development\CG_SProjects\SCeasar\src\system\softwaresTemplates\pureRef_Template\2.0.3\PureRef_2.0.3_Basic_setting.pur",
            "to": ["scene", "reference"],
            "default": True,
        }
    ],
    "mod": [
        {
            "name": "Blender",
            "from": r"S:\Pipeline\development\CG_SProjects\SCeasar\src\system\softwaresTemplates\blender_Template\4.5\Blender_4.5_Basic_setting.blend",
            "to": ["scene", "workfile", "mod", "blender"],
            "default": True,
        },
        {
            "name": "Rhino",
            "from": r"S:\Pipeline\development\CG_SProjects\SCeasar\src\system\softwaresTemplates\rhino_Template\2024\rhino2024_Basic_setting.3dm",
            "to": ["scene", "workfile", "mod", "rhino"],
            "default": False,
        },
        {
            "name": "Zbrush",
            "from": r"S:\Pipeline\development\CG_SProjects\SCeasar\src\system\softwaresTemplates\zbrush_Template\2024\zbrush2024_Basic_setting.zpr",
            "to": ["scene", "workfile", "mod", "zbrush"],
            "default": False,
        },
    ],
    "tex": [
        {
            "name": "Illustrator",
            "from": r"S:\Pipeline\development\CG_SProjects\SCeasar\src\system\softwaresTemplates\illustrator_Template\2021\Illustrator_2021_Basic_setting.ai",
            "to": ["scene", "workfile", "tex", "illustrator"],
            "default": False,
        },
        {
            "name": "Photoshop",
            "from": r"S:\Pipeline\development\CG_SProjects\SCeasar\src\system\softwaresTemplates\photoshop_Template\2021\Photoshop_2021_Basic_setting.psd",
            "to": ["scene", "workfile", "tex", "photoshop"],
            "default": False,
        },
        {
            "name": "substancePainter",
            "from": r"S:\Pipeline\development\CG_SProjects\SCeasar\src\system\softwaresTemplates\substancePainter_Template\2024\substancePainter_2024_Basic_setting.spp",
            "to": ["scene", "workfile", "tex", "substancePainter"],
            "default": True,
        },
    ],
    "uv": [
        {
            "name": "Blender",
            "from": r"S:\Pipeline\development\CG_SProjects\SCeasar\src\system\softwaresTemplates\blender_Template\4.5\Blender_4.5_Basic_setting.blend",
            "to": ["scene", "workfile", "uv", "blender"],
            "default": False,
        },
        {
            "name": "RizomUV",
            "from": r"S:\Pipeline\development\CG_SProjects\SCeasar\src\system\softwaresTemplates\rizomuv_Template\2024\RizomUV VS RS 2024.0_Basic_setting.lnk",
            "to": ["scene", "workfile", "uv", "rizomuv"],
            "default": True,
        },
    ],
    "lkd": [
        {
            "name": "Blender",
            "from": r"S:\Pipeline\development\CG_SProjects\SCeasar\src\system\softwaresTemplates\blender_Template\4.5\Blender_4.5_Lookdev_setting.blend",
            "to": ["scene", "workfile", "lkd", "blender"],
            "default": True,
        },
    ],
    "ani": [
        {
            "name": "Blender",
            "from": r"S:\Pipeline\development\CG_SProjects\SCeasar\src\system\softwaresTemplates\blender_Template\4.5\Blender_4.5_Basic_setting.blend",
            "to": ["scene", "workfile", "ani", "blender"],
            "default": False,
        }
    ],
    "fx": [
        {
            "name": "Blender",
            "from": r"S:\Pipeline\development\CG_SProjects\SCeasar\src\system\softwaresTemplates\blender_Template\4.5\Blender_4.5_Basic_setting.blend",
            "to": ["scene", "workfile", "fx", "blender"],
            "default": False,
        },
        {
            "name": "AfterEffects",
            "from": r"S:\Pipeline\development\CG_SProjects\SCeasar\src\system\softwaresTemplates\aftereffects_Template\2023\aftereffects_2023_Basic_setting.aep",
            "to": ["scene", "workfile", "fx", "aftereffects"],
            "default": False,
        },
        {
            "name": "Houdini",
            "from": r"S:\Pipeline\development\CG_SProjects\SCeasar\src\system\softwaresTemplates\houdini_Template\19.5\houdini_19.5_Basic_setting.hip",
            "to": ["scene", "workfile", "fx", "houdini"],
            "default": False,
        },
    ],
    "cmp": [
        {
            "name": "Photoshop",
            "from": r"S:\Pipeline\development\CG_SProjects\SCeasar\src\system\softwaresTemplates\photoshop_Template\2021\Photoshop_2021_Basic_setting.psd",
            "to": ["scene", "workfile", "cmp", "photoshop"],
            "default": True,
        }
    ],
    "edt": [
        {
            "name": "AfterEffects",
            "from": r"S:\Pipeline\development\CG_SProjects\SCeasar\src\system\softwaresTemplates\aftereffects_Template\2023\aftereffects_2023_Basic_setting.aep",
            "to": ["scene", "workfile", "edt", "aftereffects"],
            "default": False,
        }
    ],
}

display_names = {
    "ref": "Reference", "mod": "Modeling", "tex": "Texture", "uv": "UV", "lkd": "LookDev",
    "ani": "Animation", "fx": "Fx", "cmp": "Compositing", "edt": "Editorial"
}

left_column = ["ref", "mod", "tex", "uv", "lkd"]
right_column = ["ani", "fx", "cmp", "edt"]

software_vars = {}

# -------- Left-aligned Checkboxes --------
row_start = 5
for idx, cat in enumerate(left_column):
    softwares = software_categories.get(cat, [])
    tk.Label(root, text=f"{display_names[cat]}", font=("Poppins", 12, "bold"), fg=TITLE_COLOR, bg=BG_COLOR).grid(
        row=row_start + idx * 4,
        column=0,
        sticky="w",
        padx=50,
        pady=(10, 0),
    )
    for i, sw in enumerate(softwares):
        var = tk.BooleanVar(value=sw.get("default", True))
        chk = tk.Checkbutton(
            root, text=sw["name"], variable=var, font=("Poppins", 11),
            fg=CHK_COLOR, bg=BG_COLOR, selectcolor=BG_COLOR, activebackground=BG_COLOR
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
    tk.Label(root, text=f"{display_names[cat]}", font=("Poppins", 12, "bold"), fg=TITLE_COLOR, bg=BG_COLOR).grid(
        row=row_start + idx * 4,
        column=1,
        sticky="w",
        padx=50,
        pady=(10, 0),
    )
    for i, sw in enumerate(softwares):
        var = tk.BooleanVar(value=sw.get("default", True))
        chk = tk.Checkbutton(
            root, text=sw["name"], variable=var, font=("Poppins", 11),
            fg=CHK_COLOR, bg=BG_COLOR, selectcolor=BG_COLOR, activebackground=BG_COLOR
        )
        chk.grid(row=row_start + idx * 4 + i + 1, column=1, sticky="w", padx=50, pady=2)
        software_vars[sw["name"] + "_" + cat] = {
            "var": var,
            "from": sw["from"],
            "to": sw["to"],
            "category": cat,
        }

# -------- Versioning Helper & Submit Function --------
def get_next_version(dest_folder, project_name, category, ext, formatted_date):
    existing_versions = []
    if os.path.exists(dest_folder):
        for f in os.listdir(dest_folder):
            if f.startswith(f"{formatted_date}_{project_name}_{category}_v") and f.endswith(ext):
                ver_str = f.split("_v")[-1].split(ext)[0]
                try:
                    existing_versions.append(int(ver_str))
                except:
                    pass
    next_ver = max(existing_versions) + 1 if existing_versions else 1
    return f"v{next_ver:02d}"

def submit_form():
    project_name = entry_project.get().strip()
    if not project_name:
        messagebox.showerror("Error", "Project name is required!")
        return

    date_object = date_entry.get_date()
    formatted_date = date_object.strftime("%y%m%d")
    base_path = os.path.join(os.getcwd(), f"{formatted_date}_{project_name}")

    error_log = []

    for path in folders_to_create:
        try:
            folder_path = os.path.join(base_path, *path)
            os.makedirs(folder_path, exist_ok=True)
        except Exception as e:
            error_log.append(f"Failed to create folder {os.path.join(*path)}: {str(e)}")

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
                error_log.append(f"Failed to copy {name} from {src} to {dest_file}: {str(e)}")

    if error_log:
        messagebox.showerror("Errors Occurred", "\n".join(error_log))
    else:
        messagebox.showinfo("Success", f"Project created successfully:\n{base_path}")

# -------- Rounded Button Function --------
def rounded_button(master, text, command, bg, fg, radius=15, width=200, height=40):
    canvas = tk.Canvas(master, width=width, height=height, bg=BG_COLOR, highlightthickness=0)
    
    # Draw rounded rectangle
    canvas.create_arc((0, 0, radius*2, radius*2), start=90, extent=90, fill=bg, outline=bg)
    canvas.create_arc((width-radius*2, 0, width, radius*2), start=0, extent=90, fill=bg, outline=bg)
    canvas.create_arc((0, height-radius*2, radius*2, height), start=180, extent=90, fill=bg, outline=bg)
    canvas.create_arc((width-radius*2, height-radius*2, width, height), start=270, extent=90, fill=bg, outline=bg)
    canvas.create_rectangle(radius, 0, width-radius, height, fill=bg, outline=bg)
    canvas.create_rectangle(0, radius, width, height-radius, fill=bg, outline=bg)
    
    # Add text
    canvas.create_text(width/2, height/2, text=text, fill=fg, font=("Poppins", 12))
    
    # Bind click
    canvas.bind("<Button-1>", lambda e: command())
    
    return canvas

# -------- Add Rounded Button --------
rounded_btn = rounded_button(root, "Create Project", submit_form, BTN_BG, BTN_FG, radius=15, width=200, height=40)
rounded_btn.grid(row=50, column=0, columnspan=2, pady=20)

root.mainloop()

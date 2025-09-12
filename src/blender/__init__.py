bl_info = {
    "name": "S Ceasar",
    "author": "Ananthan AKA Jokaper 21",
    "version": (1, 0),
    "blender": (4, 5, 0),
    "location": "View3D > Sidebar > S Ceasar",
    "description": "Pipeline Tools for Modeling and Texturing",
    "category": "3D View",
}

from . import operators, ui

def register():
    ui.register()
    operators.register()

def unregister():
    operators.unregister()
    ui.unregister()

if __name__ == "__main__":
    register()
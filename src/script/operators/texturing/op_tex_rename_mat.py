import bpy
from bpy.types import Operator

def index_to_letters(index):
    """Convert a numerical index to a two-letter code (AA, AB, ..., ZZ)."""
    if index < 0:
        return "AA"
    first = chr(65 + (index // 26) % 26)  # wrap around A-Z
    second = chr(65 + (index % 26))       # A-Z
    return first + second

class SCEASAR_OT_rename_mat(Operator):
    bl_idname = "sceasar.rename_materials"
    bl_label = "Rename Materials"
    bl_description = "Rename materials of selected mesh objects to <mesh_name>_<index>_Mat"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return any(obj.type == 'MESH' for obj in context.selected_objects)

    def execute(self, context):
        mesh_objects = [obj for obj in context.selected_objects if obj.type == 'MESH']
        
        if not mesh_objects:
            self.report({'WARNING'}, "No mesh objects selected")
            return {'CANCELLED'}
        
        total_materials = 0
        for obj in mesh_objects:
            base_name = obj.name.replace("_Geo", "")
            for i, slot in enumerate(obj.material_slots):
                if slot.material:
                    # Optional: make a unique copy to avoid renaming shared materials
                    if slot.material.users > 1:
                        slot.material = slot.material.copy()
                    new_name = f"{base_name}_{index_to_letters(i)}_Mat"
                    slot.material.name = new_name
                    total_materials += 1
        
        self.report({'INFO'}, f"Renamed {total_materials} material(s) across {len(mesh_objects)} object(s)")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SCEASAR_OT_rename_mat)

def unregister():
    bpy.utils.unregister_class(SCEASAR_OT_rename_mat)

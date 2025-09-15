import bpy
from bpy.types import Operator, Panel

class SCEASAR_OT_add_geo(Operator):
    bl_idname = "sceasar.add_geo"
    bl_label = "Rename Mesh to Geo"
    bl_description = "Rename selected mesh objects to <name>_Geo if not already named"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return any(obj.type == 'MESH' for obj in context.selected_objects)

    def execute(self, context):
        mesh_objects = [obj for obj in context.selected_objects if obj.type == 'MESH']
        
        if not mesh_objects:
            self.report({'WARNING'}, "No mesh objects selected")
            return {'CANCELLED'}
        
        renamed_count = 0
        for obj in mesh_objects:
            if not obj.name.endswith("_Geo"):
                base_name = obj.name.removesuffix("_Geo")  # safer than replace
                obj.name = f"{base_name}_Geo"
                renamed_count += 1
        
        if renamed_count == 0:
            self.report({'INFO'}, "No objects needed renaming")
        else:
            self.report({'INFO'}, f"Renamed {renamed_count} mesh object(s)")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SCEASAR_OT_add_geo)

def unregister():
    bpy.utils.unregister_class(SCEASAR_OT_add_geo)
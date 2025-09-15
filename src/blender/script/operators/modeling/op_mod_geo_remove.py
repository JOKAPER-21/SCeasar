import bpy
from bpy.types import Operator

class SCEASAR_OT_mod_remove_geo(Operator):
    bl_idname = "sceasar.remove_geo"
    bl_label = "Remove _Geo from Mesh Names"
    bl_description = "Remove '_Geo' suffix from selected mesh objects if present"
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
            if obj.name.endswith("_Geo"):
                obj.name = obj.name.removesuffix("_Geo")
                renamed_count += 1
        
        if renamed_count == 0:
            self.report({'INFO'}, "No objects had '_Geo' to remove")
        else:
            self.report({'INFO'}, f"Removed '_Geo' from {renamed_count} mesh object(s)")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SCEASAR_OT_mod_remove_geo)

def unregister():
    bpy.utils.unregister_class(SCEASAR_OT_mod_remove_geo)

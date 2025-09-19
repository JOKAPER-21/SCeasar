import bpy
from bpy.types import Operator, Panel

class SCEASAR_OT_tex_remove_all_materials(Operator):
    bl_idname = "sceasar.tex_remove_all_mat"
    bl_label = "remove All Materials"
    bl_description = "Remove all material slots from selected mesh objects"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return any(obj.type == 'MESH' for obj in context.selected_objects)

    def execute(self, context):
        # Get all selected mesh objects
        mesh_objects = [obj for obj in context.selected_objects if obj.type == 'MESH']
        
        if not mesh_objects:
            self.report({'WARNING'}, "No mesh objects selected")
            return {'CANCELLED'}
            
        # remove materials from each mesh object
        for obj in mesh_objects:
            obj.data.materials.clear()
            
        self.report({'INFO'}, f"Removed materials from {len(mesh_objects)} object(s)")
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SCEASAR_OT_tex_remove_all_materials)


def unregister():
    bpy.utils.unregister_class(SCEASAR_OT_tex_remove_all_materials)

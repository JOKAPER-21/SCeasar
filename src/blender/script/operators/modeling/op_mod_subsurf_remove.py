import bpy

class SCEASAR_OT_mod_remove_subsurf(bpy.types.Operator):
    bl_idname = "sceasar.remove_subsurf"
    bl_label = "Remove Subsurf"
    
    @classmethod
    def poll(cls, context):
        return context.selected_objects and any(obj.type == 'MESH' and obj.data.uv_layers for obj in context.selected_objects)
    
    def execute(self, context):
        meshes = [obj for obj in context.selected_objects if obj.type == 'MESH']
        count = 0
        for obj in meshes:
            mod = obj.modifiers.get("MySubsurf")
            if mod:
                obj.modifiers.remove(mod)
                count += 1
        
        if count == 0:
            self.report({'ERROR'}, "No Subsurf modifiers found")
        else:
            self.report({'INFO'}, f"Removed Subsurf from {count} object(s)")
        
        return {'FINISHED'}

def register():
    bpy.utils.register_class(SCEASAR_OT_mod_remove_subsurf)

def unregister():
    bpy.utils.unregister_class(SCEASAR_OT_mod_remove_subsurf)
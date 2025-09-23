import bpy

class SCEASAR_OT_mod_apply_subsurf(bpy.types.Operator):
    """Apply all Subdivision Surface modifiers on selected meshes"""
    bl_idname = "sceasar.mod_apply_subsurf_mods"
    bl_label = "Apply Subdivision Surface Modifiers"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.selected_objects and any(obj.type == 'MESH' and obj.data.uv_layers for obj in context.selected_objects)

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                for mod in list(obj.modifiers):  # copy list so we can modify safely
                    if mod.type == 'SUBSURF':
                        # Make object active before applying
                        bpy.context.view_layer.objects.active = obj
                        try:
                            bpy.ops.object.modifier_apply(modifier=mod.name)
                            print(f"[INFO] Applied Subdivision on {obj.name}")
                        except Exception as e:
                            print(f"[ERROR] Could not apply Subdivision on {obj.name}: {e}")
            else:
                print(f"[WARNING] {obj.name} skipped (not a mesh)")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(SCEASAR_OT_mod_apply_subsurf)

def unregister():
    bpy.utils.unregister_class(SCEASAR_OT_mod_apply_subsurf)


# --- Run directly in Script Editor ---
if __name__ == "__main__":
    register()
    bpy.ops.object.apply_subsurf_mods()

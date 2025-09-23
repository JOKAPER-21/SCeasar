import bpy

class SCEASAR_OT_UV_remove_automap(bpy.types.Operator):
    """Find and remove UV map named 'automap' from selected meshes"""
    bl_idname = "sceasar.uv_remove_automap"
    bl_label = "Remove 'automap' UVMap"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        removed_any = False

        # Batch mode: tag objects instead of updating UI per step
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                mesh = obj.data
                to_remove = [uv for uv in mesh.uv_layers if uv.name.lower() == "automap"]
                for uv in to_remove:
                    mesh.uv_layers.remove(uv)
                    removed_any = True
                    self.report({'INFO'}, f"{obj.name}: removed 'automap' UV map")

        # Force single depsgraph/UI update at the end
        if removed_any:
            bpy.context.view_layer.update()  # ensures UI refresh happens once
        else:
            self.report({'WARNING'}, "No 'automap' UV maps found in selection")

        return {'FINISHED'}


def register():
    bpy.utils.register_class(SCEASAR_OT_UV_remove_automap)

def unregister():
    bpy.utils.unregister_class(SCEASAR_OT_UV_remove_automap)

if __name__ == "__main__":
    register()
    bpy.ops.sceasar.uv_remove_automap()

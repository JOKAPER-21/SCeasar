import bpy

class SCEASAR_OT_UV_reset_uvmap(bpy.types.Operator):
    """Remove all UV maps and create a new one named 'UVMap'"""
    bl_idname = "sceasar.uv_reset_uvmap"
    bl_label = "Reset UVMap"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                mesh = obj.data

                # Remove all existing UV maps
                while mesh.uv_layers:
                    mesh.uv_layers.remove(mesh.uv_layers[0])

                # Create a new UV map named "UVMap"
                mesh.uv_layers.new(name="UVMap")

                self.report({'INFO'}, f"{obj.name}: UV maps reset to 'UVMap'")
            else:
                self.report({'WARNING'}, f"{obj.name} skipped (not a mesh)")
        
        return {'FINISHED'}


def register():
    bpy.utils.register_class(SCEASAR_OT_UV_reset_uvmap)

def unregister():
    bpy.utils.unregister_class(SCEASAR_OT_UV_reset_uvmap)

# Run directly when executing in the Text Editor
if __name__ == "__main__":
    register()
    # Auto-run the operator on current selection
    bpy.ops.object.reset_uvmap()

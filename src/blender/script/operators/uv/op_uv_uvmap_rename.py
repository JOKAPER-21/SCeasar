import bpy

class SCEASAR_OT_UV_rename_uvmap(bpy.types.Operator):
    """Rename first UV map to 'UVMap' without changing UV data"""
    bl_idname = "sceasar.uv_rename_uvmap"
    bl_label = "Rename UVMap"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                mesh = obj.data

                if mesh.uv_layers:
                    mesh.uv_layers[0].name = "UVMap"
                    self.report({'INFO'}, f"{obj.name}: UV map renamed to 'UVMap'")
                else:
                    self.report({'WARNING'}, f"{obj.name} has no UV maps")
            else:
                self.report({'WARNING'}, f"{obj.name} skipped (not a mesh)")
        
        return {'FINISHED'}


def register():
    bpy.utils.register_class(SCEASAR_OT_UV_rename_uvmap)

def unregister():
    bpy.utils.unregister_class(SCEASAR_OT_UV_rename_uvmap)

# Run directly when executing in the Text Editor
if __name__ == "__main__":
    register()
    # Auto-run the operator on current selection
    bpy.ops.sceasar.uv_rename_uvmap()

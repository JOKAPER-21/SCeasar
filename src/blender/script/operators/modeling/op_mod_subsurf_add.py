import bpy

class SCEASAR_OT_mod_add_subsurf_popup(bpy.types.Operator):
    """Add Subsurf modifier only if mesh doesn't already have one"""
    bl_idname = "sceasar.add_subsurf_popup"
    bl_label = "Add Subsurf"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.selected_objects and any(obj.type == 'MESH' and obj.data.uv_layers for obj in context.selected_objects)
    
    viewport_levels: bpy.props.IntProperty(
        name="Viewport", default=2, min=0, max=6
    )
    render_levels: bpy.props.IntProperty(
        name="Render", default=2, min=0, max=6
    )

    def execute(self, context):
        meshes = [obj for obj in context.selected_objects if obj.type == 'MESH']
        if not meshes:
            self.report({'ERROR'}, "No mesh objects selected")
            return {'CANCELLED'}

        added_count = 0
        skipped_count = 0

        for obj in meshes:
            # Check if object already has a Subsurf modifier
            subsurf = next((m for m in obj.modifiers if m.type == 'SUBSURF'), None)

            if subsurf:
                skipped_count += 1
                continue  # skip if already has subsurf

            # Add new Subdivision modifier
            mod = obj.modifiers.new(name="Subdivision", type='SUBSURF')
            mod.levels = self.viewport_levels
            mod.render_levels = self.render_levels
            added_count += 1

        self.report({'INFO'}, f"Subsurf added to {added_count} object(s), skipped {skipped_count}.")
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "viewport_levels")
        layout.prop(self, "render_levels")


def register():
    bpy.utils.register_class(SCEASAR_OT_mod_add_subsurf_popup)

def unregister():
    bpy.utils.unregister_class(SCEASAR_OT_mod_add_subsurf_popup)


# --- Run directly in Script Editor ---
if __name__ == "__main__":
    register()
    bpy.ops.sceasar.add_subsurf_popup('INVOKE_DEFAULT')

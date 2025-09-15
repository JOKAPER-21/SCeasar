import bpy

class SCEASAR_OT_mod_add_subsurf_popup(bpy.types.Operator):
    bl_idname = "sceasar.add_subsurf_popup"
    bl_label = "Add Subsurf"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.selected_objects and any(obj.type == 'MESH' and obj.data.uv_layers for obj in context.selected_objects)

    viewport_levels: bpy.props.IntProperty(name="Viewport", default=2, min=0, max=6) # type: ignore
    render_levels: bpy.props.IntProperty(name="Render", default=2, min=0, max=6) # type: ignore

    def execute(self, context):
        meshes = [obj for obj in context.selected_objects if obj.type == 'MESH']
        if not meshes:
            self.report({'ERROR'}, "No mesh objects selected")
            return {'CANCELLED'}

        for obj in meshes:
            if "MySubsurf" not in obj.modifiers:
                mod = obj.modifiers.new(name="MySubsurf", type='SUBSURF')
            else:
                mod = obj.modifiers["MySubsurf"]

            mod.levels = self.viewport_levels
            mod.render_levels = self.render_levels

        self.report({'INFO'}, f"Subsurf applied to {len(meshes)} object(s)")
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.prop(self, "viewport_levels")
        col.prop(self, "render_levels")

def register():
    bpy.utils.register_class(SCEASAR_OT_mod_add_subsurf_popup)

def unregister():
    bpy.utils.unregister_class(SCEASAR_OT_mod_add_subsurf_popup)
import bpy

class SCEASAR_OT_mod_edit_subsurf_popup(bpy.types.Operator):
    bl_idname = "sceasar.edit_subsurf_popup"
    bl_label = "Edit Subsurf"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        return context.selected_objects and any(obj.type == 'MESH' and obj.data.uv_layers for obj in context.selected_objects)

    viewport_levels: bpy.props.IntProperty(name="Viewport", default=2, min=0, max=6) # type: ignore
    render_levels: bpy.props.IntProperty(name="Render", default=3, min=0, max=6) # type: ignore

    def execute(self, context):
        meshes = [obj for obj in context.selected_objects if obj.type == 'MESH']
        count = 0
        for obj in meshes:
            mod = obj.modifiers.get("MySubsurf")
            if mod:
                mod.levels = self.viewport_levels
                mod.render_levels = self.render_levels
                count += 1

        if count == 0:
            self.report({'ERROR'}, "No Subsurf modifiers found on selected objects")
            return {'CANCELLED'}

        self.report({'INFO'}, f"Edited Subsurf on {count} object(s)")
        return {'FINISHED'}

    def invoke(self, context, event):
        obj = context.active_object
        if obj and obj.type == 'MESH':
            mod = obj.modifiers.get("MySubsurf")
            if mod:
                self.viewport_levels = mod.levels
                self.render_levels = mod.render_levels

        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.prop(self, "viewport_levels")
        col.prop(self, "render_levels")

def register():
    bpy.utils.register_class(SCEASAR_OT_mod_edit_subsurf_popup)

def unregister():
    bpy.utils.unregister_class(SCEASAR_OT_mod_edit_subsurf_popup)
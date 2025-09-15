import bpy

class SCEASAR_PT_Layout(bpy.types.Panel):
    bl_label = "Layout"
    bl_idname = "SCEASAR_PT_layout"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'LAYOUT'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Layout / Previs Tools", icon="OUTLINER_OB_CAMERA")

class SCEASAR_PT_Export_Layout(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_export_layout"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_layout"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'LAYOUT'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Options", icon="EXPORT")

def register():
    bpy.utils.register_class(SCEASAR_PT_Layout)
    bpy.utils.register_class(SCEASAR_PT_Export_Layout)

def unregister():
    bpy.utils.unregister_class(SCEASAR_PT_Export_Layout)
    bpy.utils.unregister_class(SCEASAR_PT_Layout)
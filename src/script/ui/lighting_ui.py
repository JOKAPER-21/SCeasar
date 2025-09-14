import bpy

class SCEASAR_PT_Lighting(bpy.types.Panel):
    bl_label = "Lighting"
    bl_idname = "SCEASAR_PT_lighting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'LIGHTING'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Lighting Tools", icon="OUTLINER_OB_LIGHT")

class SCEASAR_PT_Export_Lighting(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_export_lighting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_lighting"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'LIGHTING'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Options", icon="EXPORT")

def register():
    bpy.utils.register_class(SCEASAR_PT_Lighting)
    bpy.utils.register_class(SCEASAR_PT_Export_Lighting)

def unregister():
    bpy.utils.unregister_class(SCEASAR_PT_Export_Lighting)
    bpy.utils.unregister_class(SCEASAR_PT_Lighting)
import bpy

class SCEASAR_PT_Rendering(bpy.types.Panel):
    bl_label = "Rendering"
    bl_idname = "SCEASAR_PT_rendering"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'RENDERING'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Rendering Tools", icon="RENDER_STILL")

class SCEASAR_PT_Export_Rendering(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_export_rendering"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_rendering"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'RENDERING'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Options", icon="EXPORT")

def register():
    bpy.utils.register_class(SCEASAR_PT_Rendering)
    bpy.utils.register_class(SCEASAR_PT_Export_Rendering)

def unregister():
    bpy.utils.unregister_class(SCEASAR_PT_Export_Rendering)
    bpy.utils.unregister_class(SCEASAR_PT_Rendering)
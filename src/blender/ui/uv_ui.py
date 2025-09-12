import bpy

class SCEASAR_PT_Uv(bpy.types.Panel):
    bl_label = "UV Mapping"
    bl_idname = "SCEASAR_PT_uv"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'UV'

    def draw(self, context):
        layout = self.layout
        layout.label(text="UV Tools", icon="GROUP_UVS")

class SCEASAR_PT_Export_Uv(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_export_uv"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_uv"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'UV'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Options", icon="EXPORT")

def register():
    bpy.utils.register_class(SCEASAR_PT_Uv)
    bpy.utils.register_class(SCEASAR_PT_Export_Uv)

def unregister():
    bpy.utils.unregister_class(SCEASAR_PT_Export_Uv)
    bpy.utils.unregister_class(SCEASAR_PT_Uv)
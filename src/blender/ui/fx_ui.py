import bpy

class SCEASAR_PT_Fx(bpy.types.Panel):
    bl_label = "Effects"
    bl_idname = "SCEASAR_PT_fx"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'FX'

    def draw(self, context):
        layout = self.layout
        layout.label(text="FX Tools", icon="OUTLINER_OB_POINTCLOUD")

class SCEASAR_PT_Export_Fx(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_export_fx"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_fx"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'FX'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Options", icon="EXPORT")

def register():
    bpy.utils.register_class(SCEASAR_PT_Fx)
    bpy.utils.register_class(SCEASAR_PT_Export_Fx)

def unregister():
    bpy.utils.unregister_class(SCEASAR_PT_Export_Fx)
    bpy.utils.unregister_class(SCEASAR_PT_Fx)
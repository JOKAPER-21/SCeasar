import bpy

class SCEASAR_PT_Lookdev(bpy.types.Panel):
    bl_label = "Lookdev"
    bl_idname = "SCEASAR_PT_lookdev"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'LOOKDEV'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Look Development Tools", icon="MATERIAL")

class SCEASAR_PT_Export_Lookdev(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_export_lookdev"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_lookdev"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'LOOKDEV'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Options", icon="EXPORT")

def register():
    bpy.utils.register_class(SCEASAR_PT_Lookdev)
    bpy.utils.register_class(SCEASAR_PT_Export_Lookdev)

def unregister():
    bpy.utils.unregister_class(SCEASAR_PT_Export_Lookdev)
    bpy.utils.unregister_class(SCEASAR_PT_Lookdev)
import bpy

class SCEASAR_PT_Rigging(bpy.types.Panel):
    bl_label = "Rigging"
    bl_idname = "SCEASAR_PT_rigging"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'RIGGING'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Rigging Tools", icon="BONE_DATA")

class SCEASAR_PT_Export_Rigging(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_export_rigging"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_rigging"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'RIGGING'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Options", icon="EXPORT")

def register():
    bpy.utils.register_class(SCEASAR_PT_Rigging)
    bpy.utils.register_class(SCEASAR_PT_Export_Rigging)

def unregister():
    bpy.utils.unregister_class(SCEASAR_PT_Export_Rigging)
    bpy.utils.unregister_class(SCEASAR_PT_Rigging)
import bpy

class SCEASAR_PT_Compositing(bpy.types.Panel):
    bl_label = "Compositing"
    bl_idname = "SCEASAR_PT_compositing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'COMPOSITING'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Compositing Tools", icon="NODETREE")

class SCEASAR_PT_Export_Compositing(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_export_compositing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_compositing"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'COMPOSITING'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Options", icon="EXPORT")

def register():
    bpy.utils.register_class(SCEASAR_PT_Compositing)
    bpy.utils.register_class(SCEASAR_PT_Export_Compositing)

def unregister():
    bpy.utils.unregister_class(SCEASAR_PT_Export_Compositing)
    bpy.utils.unregister_class(SCEASAR_PT_Compositing)
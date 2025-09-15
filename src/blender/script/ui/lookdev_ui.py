import bpy

class SCEASAR_PT_Lookdev_Tools(bpy.types.Panel):
    bl_label = "Lookdev Tools"
    bl_idname = "SCEASAR_PT_Lookdev_Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'LOOKDEV'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Shader Editor", icon="NODE_MATERIAL")
        box.label(text="Material Preview", icon="MATERIAL")
        box.label(text="HDRI Lighting", icon="WORLD")


class SCEASAR_PT_Lookdev_Setting(bpy.types.Panel):
    bl_label = "Settings"
    bl_idname = "SCEASAR_PT_Lookdev_Setting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'LOOKDEV'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Viewport Shading", icon="SHADING_RENDERED")
        box.label(text="EEVEE / Cycles", icon="RENDER_STILL")


class SCEASAR_PT_Lookdev_Export(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_Lookdev_Export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'LOOKDEV'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Render Export", icon="RENDER_ANIMATION")
        layout.label(text="Bake Textures", icon="IMAGE_DATA")


def register():
    bpy.utils.register_class(SCEASAR_PT_Lookdev_Tools)
    bpy.utils.register_class(SCEASAR_PT_Lookdev_Setting)
    bpy.utils.register_class(SCEASAR_PT_Lookdev_Export)

def unregister():
    for cls in (
        SCEASAR_PT_Lookdev_Export,
        SCEASAR_PT_Lookdev_Setting,
        SCEASAR_PT_Lookdev_Tools,
    ):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass

import bpy

class SCEASAR_PT_Lighting_Tools(bpy.types.Panel):
    bl_label = "Lighting Tools"
    bl_idname = "SCEASAR_PT_Lighting_Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'LIGHTING'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Add Light", icon="LIGHT_POINT")
        box.label(text="Light Linking", icon="LIGHT_SUN")
        box.label(text="IES Profiles", icon="LIGHT_SPOT")


class SCEASAR_PT_Lighting_Setting(bpy.types.Panel):
    bl_label = "Settings"
    bl_idname = "SCEASAR_PT_Lighting_Setting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'LIGHTING'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Light Intensity", icon="LIGHT_HEMI")
        box.label(text="Shadows", icon="SHADING_SOLID")
        box.label(text="Color Temperature", icon="COLOR")


class SCEASAR_PT_Lighting_Export(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_Lighting_Export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'LIGHTING'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Bake Lighting", icon="RENDER_STILL")
        layout.label(text="Export Light Setup", icon="EXPORT")


def register():
    bpy.utils.register_class(SCEASAR_PT_Lighting_Tools)
    bpy.utils.register_class(SCEASAR_PT_Lighting_Setting)
    bpy.utils.register_class(SCEASAR_PT_Lighting_Export)

def unregister():
    for cls in (
        SCEASAR_PT_Lighting_Export,
        SCEASAR_PT_Lighting_Setting,
        SCEASAR_PT_Lighting_Tools,
    ):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass

import bpy

class SCEASAR_PT_Rendering_Tools(bpy.types.Panel):
    bl_label = "Rendering Tools"
    bl_idname = "SCEASAR_PT_Rendering_Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'RENDERING'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Render Image", icon="RENDER_STILL")
        box.label(text="Render Animation", icon="RENDER_ANIMATION")
        box.label(text="Viewport Render", icon="SHADING_RENDERED")


class SCEASAR_PT_Rendering_Setting(bpy.types.Panel):
    bl_label = "Settings"
    bl_idname = "SCEASAR_PT_Rendering_Setting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'RENDERING'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Render Engine (EEVEE/Cycles)", icon="RENDER_STILL")
        box.label(text="Sampling & Denoising", icon="MOD_NOISE")
        box.label(text="Output Settings", icon="OUTPUT")


class SCEASAR_PT_Rendering_Export(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_Rendering_Export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'RENDERING'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Save Rendered Image", icon="IMAGE_DATA")
        layout.label(text="Export Video", icon="SEQUENCE")


def register():
    bpy.utils.register_class(SCEASAR_PT_Rendering_Tools)
    bpy.utils.register_class(SCEASAR_PT_Rendering_Setting)
    bpy.utils.register_class(SCEASAR_PT_Rendering_Export)

def unregister():
    for cls in (
        SCEASAR_PT_Rendering_Export,
        SCEASAR_PT_Rendering_Setting,
        SCEASAR_PT_Rendering_Tools,
    ):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass

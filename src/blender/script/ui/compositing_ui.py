import bpy

class SCEASAR_PT_Compositing_Tools(bpy.types.Panel):
    bl_label = "Compositing Tools"
    bl_idname = "SCEASAR_PT_Compositing_Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'COMPOSITING'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Open Compositor", icon="NODE_COMPOSITING")
        box.label(text="Add Render Layers", icon="RENDERLAYERS")
        box.label(text="Add Effects", icon="SEQ_PREVIEW")


class SCEASAR_PT_Compositing_Setting(bpy.types.Panel):
    bl_label = "Settings"
    bl_idname = "SCEASAR_PT_Compositing_Setting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'COMPOSITING'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Use Nodes", icon="NODETREE")
        box.label(text="Backdrop Settings", icon="IMAGE_BACKGROUND")
        box.label(text="Render Passes", icon="RENDER_RESULT")


class SCEASAR_PT_Compositing_Export(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_Compositing_Export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'COMPOSITING'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Final Image", icon="IMAGE_DATA")
        layout.label(text="Export Sequence", icon="SEQUENCE")


def register():
    bpy.utils.register_class(SCEASAR_PT_Compositing_Tools)
    bpy.utils.register_class(SCEASAR_PT_Compositing_Setting)
    bpy.utils.register_class(SCEASAR_PT_Compositing_Export)

def unregister():
    for cls in (
        SCEASAR_PT_Compositing_Export,
        SCEASAR_PT_Compositing_Setting,
        SCEASAR_PT_Compositing_Tools,
    ):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass

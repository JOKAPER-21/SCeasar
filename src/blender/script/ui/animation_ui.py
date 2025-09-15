import bpy

class SCEASAR_PT_Animation_Tools(bpy.types.Panel):
    bl_label = "Animation Tools"
    bl_idname = "SCEASAR_PT_Animation_Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'ANIMATION'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Insert Keyframe", icon="KEY_HLT")
        box.label(text="Graph Editor", icon="GRAPH")
        box.label(text="Dope Sheet", icon="ACTION")


class SCEASAR_PT_Animation_Setting(bpy.types.Panel):
    bl_label = "Settings"
    bl_idname = "SCEASAR_PT_Animation_Setting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'ANIMATION'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Frame Range", icon="TIME")
        box.label(text="Frame Rate", icon="RENDER_ANIMATION")
        box.label(text="Playback Settings", icon="PLAY")


class SCEASAR_PT_Animation_Export(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_Animation_Export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'ANIMATION'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Animation", icon="EXPORT")
        layout.label(text="Bake Action", icon="NLA")


def register():
    bpy.utils.register_class(SCEASAR_PT_Animation_Tools)
    bpy.utils.register_class(SCEASAR_PT_Animation_Setting)
    bpy.utils.register_class(SCEASAR_PT_Animation_Export)

def unregister():
    for cls in (
        SCEASAR_PT_Animation_Export,
        SCEASAR_PT_Animation_Setting,
        SCEASAR_PT_Animation_Tools,
    ):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass

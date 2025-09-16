import bpy

class SCEASAR_PT_UV_Tools(bpy.types.Panel):
    bl_label = "UV Tools"
    bl_idname = "SCEASAR_PT_UV_Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'UV'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Unwrap", icon="GROUP_UVS")
        box.label(text="Smart UV Project", icon="MOD_UVPROJECT")
        box.label(text="UV Sculpt", icon="SCULPTMODE_HLT")


class SCEASAR_PT_UV_Setting(bpy.types.Panel):
    bl_label = "Settings"
    bl_idname = "SCEASAR_PT_UV_Setting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'UV'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="UV Stretch Display", icon="STYLUS_PRESSURE")
        box.label(text="Sync Selection", icon="UV_SYNC_SELECT")


class SCEASAR_PT_UV_IO(bpy.types.Panel):
    bl_label = "Asset I/O"
    bl_idname = "SCEASAR_PT_UV_IO"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'UV'

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        box.label(text="UV Stretch Display", icon="STYLUS_PRESSURE")
        box.label(text="Sync Selection", icon="UV_SYNC_SELECT")


def register():
    bpy.utils.register_class(SCEASAR_PT_UV_Tools)
    bpy.utils.register_class(SCEASAR_PT_UV_Setting)
    bpy.utils.register_class(SCEASAR_PT_UV_IO)

def unregister():
    for cls in (
        SCEASAR_PT_UV_IO,
        SCEASAR_PT_UV_Setting,
        SCEASAR_PT_UV_Tools,
    ):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass

import bpy

class SCEASAR_PT_Animation(bpy.types.Panel):
    bl_label = "Animation"
    bl_idname = "SCEASAR_PT_animation"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'ANIMATION'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Animation Tools", icon="OUTLINER_OB_ARMATURE")

class SCEASAR_PT_Export_Animation(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_export_animation"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_animation"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'ANIMATION'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Options", icon="EXPORT")

def register():
    bpy.utils.register_class(SCEASAR_PT_Animation)
    bpy.utils.register_class(SCEASAR_PT_Export_Animation)

def unregister():
    bpy.utils.unregister_class(SCEASAR_PT_Export_Animation)
    bpy.utils.unregister_class(SCEASAR_PT_Animation)
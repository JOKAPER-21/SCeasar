import bpy

class SCEASAR_PT_Rigging_Tools(bpy.types.Panel):
    bl_label = "Rigging Tools"
    bl_idname = "SCEASAR_PT_Rigging_Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'RIGGING'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Add Armature", icon="ARMATURE_DATA")
        box.label(text="Automatic Weights", icon="MOD_ARMATURE")
        box.label(text="Bone Constraints", icon="CONSTRAINT_BONE")


class SCEASAR_PT_Rigging_Setting(bpy.types.Panel):
    bl_label = "Settings"
    bl_idname = "SCEASAR_PT_Rigging_Setting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'RIGGING'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Bone Layers", icon="BONE_DATA")
        box.label(text="Custom Shapes", icon="SHAPEKEY_DATA")
        box.label(text="IK / FK Settings", icon="CONSTRAINT")


class SCEASAR_PT_Rigging_Export(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_Rigging_Export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'RIGGING'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Armature", icon="EXPORT")
        layout.label(text="Bake Animation", icon="ACTION")


def register():
    bpy.utils.register_class(SCEASAR_PT_Rigging_Tools)
    bpy.utils.register_class(SCEASAR_PT_Rigging_Setting)
    bpy.utils.register_class(SCEASAR_PT_Rigging_Export)

def unregister():
    for cls in (
        SCEASAR_PT_Rigging_Export,
        SCEASAR_PT_Rigging_Setting,
        SCEASAR_PT_Rigging_Tools,
    ):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass

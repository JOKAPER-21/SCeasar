import bpy

class SCEASAR_PT_FX_Tools(bpy.types.Panel):
    bl_label = "FX Tools"
    bl_idname = "SCEASAR_PT_FX_Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'FX'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Add Particle System", icon="PARTICLES")
        box.label(text="Fluid / Smoke", icon="MOD_FLUIDSIM")
        box.label(text="Cloth / Softbody", icon="MOD_CLOTH")


class SCEASAR_PT_FX_Setting(bpy.types.Panel):
    bl_label = "Settings"
    bl_idname = "SCEASAR_PT_FX_Setting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'FX'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Cache Settings", icon="FILE_CACHE")
        box.label(text="Domain Resolution", icon="MOD_PHYSICS")
        box.label(text="Collision Settings", icon="MOD_PHYSICS")


class SCEASAR_PT_FX_Export(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_FX_Export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'FX'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Bake Simulation", icon="PHYSICS")
        layout.label(text="Export Alembic / VDB", icon="EXPORT")


def register():
    bpy.utils.register_class(SCEASAR_PT_FX_Tools)
    bpy.utils.register_class(SCEASAR_PT_FX_Setting)
    bpy.utils.register_class(SCEASAR_PT_FX_Export)

def unregister():
    for cls in (
        SCEASAR_PT_FX_Export,
        SCEASAR_PT_FX_Setting,
        SCEASAR_PT_FX_Tools,
    ):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass

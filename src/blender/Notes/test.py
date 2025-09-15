import bpy

class SCEASAR_PT_Modeling_Tools(bpy.types.Panel):
    bl_label = "Modeling Tools"
    bl_idname = "SCEASAR_PT_Modeling_Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'MODELING'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Subdivision Surface", icon="MODIFIER")


class SCEASAR_PT_Modeling_Setting(bpy.types.Panel):
    bl_label = "Setting"
    bl_idname = "SCEASAR_PT_Modeling_Setting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'MODELING'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()
        box.label(text="Subdivision Surface", icon="MODIFIER")
 

class SCEASAR_PT_Modeling_Export(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_Modeling_Export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'MODELING'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Options", icon="EXPORT")

    
def register():
    bpy.utils.register_class(SCEASAR_PT_Modeling_Tools)
    bpy.utils.register_class(SCEASAR_PT_Modeling_Setting)
    bpy.utils.register_class(SCEASAR_PT_Modeling_Export)

def unregister():
    for cls in (
        SCEASAR_PT_Modeling_Export,
        SCEASAR_PT_Modeling_Setting,
        SCEASAR_PT_Modeling_Tools,
    ):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass  # ignore if already unregistered

import bpy

class SCEASAR_PT_Texturing_Tools(bpy.types.Panel):
    bl_label = "Texturing Tools"
    bl_idname = "SCEASAR_PT_Texturing_Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'TEXTURING'

    def draw(self, context):
        layout = self.layout
        
        box = layout.box()         
        box.label(text="Material Tools", icon="NODE_MATERIAL")
        row = box.row(align=True)
        row.operator("sceasar.add_empty_mat", text="Empty Mat", icon="SHADING_TEXTURE")
        row.operator("sceasar.clear_all_mat", text="Clear All", icon="CANCEL")
        
        box = layout.box()
        box.label(text="Basic Setup", icon="OUTLINER_OB_MESH")
        row = box.row(align=True)
        row.operator("sceasar.remove_geo", text="Remove Geo", icon="CURRENT_FILE")


class SCEASAR_PT_Texturing_Setting(bpy.types.Panel):
    bl_label = "Settings"
    bl_idname = "SCEASAR_PT_Texturing_Setting"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'TEXTURING'
    
    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Options", icon="EXPORT")


class SCEASAR_PT_Texturing_Export(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_Texturing_Export"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'TEXTURING'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Options", icon="EXPORT")


def register():
    bpy.utils.register_class(SCEASAR_PT_Texturing_Tools)
    bpy.utils.register_class(SCEASAR_PT_Texturing_Setting)
    bpy.utils.register_class(SCEASAR_PT_Texturing_Export)

def unregister():
    for cls in (
        SCEASAR_PT_Texturing_Export,
        SCEASAR_PT_Texturing_Setting,
        SCEASAR_PT_Texturing_Tools,
    ):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass

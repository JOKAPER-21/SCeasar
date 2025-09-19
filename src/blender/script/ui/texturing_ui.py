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



class SCEASAR_PT_Texturing_Cleanup(bpy.types.Panel):
    bl_label = "Cleanup"
    bl_idname = "SCEASAR_PT_Texturing_Cleanup"
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
        
        box = layout.box()
        box.label(text="Material", icon="SHADING_RENDERED")
        row = box.column(align=True)
        row.operator("sceasar.tex_add_empty_mat", text="Add Mat", icon="PLUS")
        row.operator("sceasar.tex_clear_all_mat", text="Clear Mat", icon="CANCEL")
        row.operator("sceasar.tex_rename_mat", text="Rename Mat", icon="CURRENT_FILE")

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
    bpy.utils.register_class(SCEASAR_PT_Texturing_Cleanup)
    bpy.utils.register_class(SCEASAR_PT_Texturing_Export)

def unregister():
    for cls in (
        SCEASAR_PT_Texturing_Export,
        SCEASAR_PT_Texturing_Cleanup,
        SCEASAR_PT_Texturing_Tools,
    ):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass

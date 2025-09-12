import bpy

class SCEASAR_PT_Texturing(bpy.types.Panel):
    bl_label = "Texturing"
    bl_idname = "SCEASAR_PT_texturing"
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
        row.scale_y = 1.2
        row.operator("sceasar.add_empty_mat", text="Empty Mat", icon="SHADING_TEXTURE")
        row.operator("sceasar.clear_all_mat", text="Clear All", icon="CANCEL")
        
        box = layout.box()
        box.label(text="Basic Setup", icon="OUTLINER_OB_MESH")
        row = box.row(align=True)
        row.scale_y = 1.2
        row.operator("sceasar.remove_geo", text="Remove Geo", icon="CURRENT_FILE")

        
class SCEASAR_PT_Export_Texturing(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_export_texturing"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_texturing"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'TEXTURING'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Options", icon="EXPORT")
        
        row = layout.row(align=True)
        row.scale_y = 1.2

def register():
    bpy.utils.register_class(SCEASAR_PT_Texturing)
    bpy.utils.register_class(SCEASAR_PT_Export_Texturing)

def unregister():
    bpy.utils.unregister_class(SCEASAR_PT_Export_Texturing)
    bpy.utils.unregister_class(SCEASAR_PT_Texturing)
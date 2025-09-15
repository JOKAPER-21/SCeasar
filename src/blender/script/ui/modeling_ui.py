import bpy

class SCEASAR_PT_Basic_Modeling(bpy.types.Panel):
    bl_label = "Basic Settings"
    bl_idname = "SCEASAR_PT_Basic_modeling"
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
        row = box.row(align=True)
        row.operator("sceasar.add_subsurf_popup", text="Add", icon="PLUS")
        row.operator("sceasar.edit_subsurf_popup", text="Edit", icon="GREASEPENCIL")
        row.operator("sceasar.remove_subsurf", text="Remove", icon="CANCEL")
        
        box = layout.box()
        box.label(text="Basic Setup", icon="OUTLINER_OB_MESH")
        row = box.row(align=True)
        row.operator("sceasar.add_geo", text="Add Geo", icon="CURRENT_FILE")
        row.operator("sceasar.remove_geo", text="Remove Geo", icon="CURRENT_FILE")

class SCEASAR_PT_Tools_Modeling(bpy.types.Panel):
    bl_label = "Tools Settings"
    bl_idname = "SCEASAR_PT_Tools_modeling"
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
 

class SCEASAR_PT_Export_Modeling(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_export_modeling"
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
        col = layout.column(align=True)
        col.scale_y = 1.2
    
def register():
    bpy.utils.register_class(SCEASAR_PT_Basic_Modeling)
    bpy.utils.register_class(SCEASAR_PT_Tools_Modeling)
    bpy.utils.register_class(SCEASAR_PT_Export_Modeling)

def unregister():
    for cls in (
        SCEASAR_PT_Export_Modeling,
        SCEASAR_PT_Tools_Modeling,
        SCEASAR_PT_Basic_Modeling,
    ):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass  # ignore if already unregistered

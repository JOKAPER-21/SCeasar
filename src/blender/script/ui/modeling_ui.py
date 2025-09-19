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
        row = box.row(align=True)
        row.operator("sceasar.add_subsurf_popup", text="Add", icon="PLUS")
        row.operator("sceasar.edit_subsurf_popup", text="Edit", icon="GREASEPENCIL")
        row.operator("sceasar.remove_subsurf", text="Remove", icon="CANCEL")

class SCEASAR_PT_Modeling_Cleanup(bpy.types.Panel):
    bl_label = "Cleanup"
    bl_idname = "SCEASAR_PT_Modeling_Cleanup"
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
        box.label(text="Basic Setup", icon="SETTINGS")
        row = box.row(align=True)
        row.operator("sceasar.add_geo", text="Add Geo", icon="ADD")
        row.operator("sceasar.remove_geo", text="Remove Geo", icon="REMOVE")
 

class SCEASAR_PT_Modeling_IO(bpy.types.Panel):
    bl_label = "Asset I/O"
    bl_idname = "SCEASAR_PT_Modeling_IO"
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
        box.label(text="Import", icon="IMPORT")
        
        box = layout.box()
        box.label(text="Export", icon="EXPORT")
        
        row = box.column(align=True)
        row.operator("sceasar.export_mod_version_fbx", text="Fbx", icon="OUTLINER")
        row.operator("sceasar.save_mod_to_master", text="Master", icon="PINNED")
        

    
def register():
    bpy.utils.register_class(SCEASAR_PT_Modeling_Tools)
    bpy.utils.register_class(SCEASAR_PT_Modeling_Cleanup)
    bpy.utils.register_class(SCEASAR_PT_Modeling_IO)

def unregister():
    for cls in (
        SCEASAR_PT_Modeling_IO,
        SCEASAR_PT_Modeling_Cleanup,
        SCEASAR_PT_Modeling_Tools,
    ):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass  # ignore if already unregistered

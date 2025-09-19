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
                
class SCEASAR_PT_UV_Cleanup(bpy.types.Panel):
    bl_label = "Cleanup"
    bl_idname = "SCEASAR_PT_UV_Cleanup"
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
        box.label(text="UVMap", icon="UV")
        
        row = box.column(align=True)
        row.operator("sceasar.uv_reset_uvmap", text="UVMap", icon="PLUS")


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
        box.label(text="Import", icon="IMPORT")
        
        row = box.column(align=True)
        row.operator("sceasar.import_mod_master", text="Import Mod")
        row.operator("sceasar.import_all_collections", text="Updated collection")
        
        box = layout.box()
        box.label(text="Export", icon="EXPORT")
        
        row = box.column(align=True)
        row.operator("sceasar.export_uv_version_fbx", text="Fbx", icon="OUTLINER")
        row.operator("sceasar.save_uv_to_master", text="Master", icon="PINNED")


def register():
    bpy.utils.register_class(SCEASAR_PT_UV_Tools)
    bpy.utils.register_class(SCEASAR_PT_UV_Cleanup)
    bpy.utils.register_class(SCEASAR_PT_UV_IO)

def unregister():
    for cls in (
        SCEASAR_PT_UV_IO,
        SCEASAR_PT_UV_Cleanup,
        SCEASAR_PT_UV_Tools,
    ):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass

from . import (
    op_uv_import_mod_master,
    op_uv_import_mod_collection_master,
    op_uv_export_master,
    op_uv_export_version_fbx,
    op_uv_uvmap_rename,
    op_uv_automap_remove
)

modules = [op_uv_import_mod_master, 
           op_uv_import_mod_collection_master, 
           op_uv_export_master, 
           op_uv_export_version_fbx, 
           op_uv_uvmap_rename, 
           op_uv_automap_remove]

def register():
    for m in modules:
        m.register()

def unregister():
    for m in reversed(modules):
        m.unregister()

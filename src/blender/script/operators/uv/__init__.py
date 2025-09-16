from . import op_uv_export_master, op_uv_import_mod_master

def register():
    op_uv_export_master.register()
    op_uv_import_mod_master.register()

def unregister():
    op_uv_import_mod_master.unregister()
    op_uv_export_master.unregister()
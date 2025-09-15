from . import op_mod_geo_add, op_mod_geo_remove, op_mod_subsurf_add, op_mod_subsurf_edit, op_mod_subsurf_remove

def register():
    op_mod_subsurf_add.register()
    op_mod_subsurf_edit.register()
    op_mod_subsurf_remove.register()
    op_mod_geo_add.register()
    op_mod_geo_remove.register()

def unregister():
    op_mod_geo_remove.unregister()
    op_mod_geo_add.unregister()
    op_mod_subsurf_remove.unregister()
    op_mod_subsurf_edit.unregister()
    op_mod_subsurf_add.unregister()
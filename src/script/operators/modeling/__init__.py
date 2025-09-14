from . import op_mod_add_geo, op_mod_remove_geo, op_mod_subsurf_add, op_mod_subsurf_edit, op_mod_subsurf_remove

def register():
    op_mod_subsurf_add.register()
    op_mod_subsurf_edit.register()
    op_mod_subsurf_remove.register()
    op_mod_add_geo.register()
    op_mod_remove_geo.register()

def unregister():
    op_mod_remove_geo.unregister()
    op_mod_add_geo.unregister()
    op_mod_subsurf_remove.unregister()
    op_mod_subsurf_edit.unregister()
    op_mod_subsurf_add.unregister()
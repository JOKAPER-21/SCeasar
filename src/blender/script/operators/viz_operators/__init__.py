from . import op_geo_add, op_geo_remove

def register():
    op_geo_add.register()
    op_geo_remove.register()

def unregister():
    op_geo_remove.unregister()
    op_geo_add.unregister()
from . import op_tex_remove_all_mat, op_tex_rename_mat

modules = [op_tex_remove_all_mat, op_tex_rename_mat]

def register():
    for m in modules:
        m.register()

def unregister():
    for m in reversed(modules):
        m.unregister()

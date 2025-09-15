from . import op_tex_remove_all_mat, op_tex_rename_mat

def register():
    op_tex_remove_all_mat.register()
    op_tex_rename_mat.register()

def unregister():
    op_tex_rename_mat.unregister()
    op_tex_remove_all_mat.unregister()
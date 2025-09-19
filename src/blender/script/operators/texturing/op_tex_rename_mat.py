import bpy

# ------------------------
# Helper
# ------------------------
def index_to_letters(index: int) -> str:
    """Convert 0 -> 'AA', 1 -> 'AB', ..."""
    letters = ""
    index += 26  # start at 'AA' for index 0
    while index >= 0:
        letters = chr(index % 26 + ord('A')) + letters
        index = index // 26 - 1
    return letters


def rename_material_slots_for_selected(context, verbose=True):
    selected_meshes = [o for o in context.selected_objects if o.type == 'MESH']
    if not selected_meshes:
        if verbose:
            print("No mesh objects selected.")
        return 0

    renamed_count = 0
    skipped_count = 0

    for obj in selected_meshes:
        base_name = obj.name.replace("_Geo", "")
        for idx, mat in enumerate(obj.data.materials):
            if mat is None:
                skipped_count += 1
                if verbose:
                    print(f"{obj.name} slot {idx}: empty - skipped.")
                continue

            new_name = f"{base_name}_{index_to_letters(idx)}_Mat"

            if mat.name == new_name:
                skipped_count += 1
                if verbose:
                    print(f"{obj.name} slot {idx}: already '{new_name}' - skipped.")
                continue

            if mat.users > 1 and verbose:
                print(f"⚠ Warning: material '{mat.name}' is used by {mat.users} users.")

            try:
                mat.name = new_name
                renamed_count += 1
                if verbose:
                    print(f"✔ Renamed {obj.name} slot {idx} -> '{new_name}'")
            except Exception as e:
                skipped_count += 1
                print(f"❌ Failed to rename material for {obj.name} slot {idx}: {e}")

    if verbose:
        print(f"Done. Renamed: {renamed_count}, Skipped: {skipped_count}.")
    return renamed_count


# ------------------------
# Operator
# ------------------------
class SCEASAR_OT_TEX_rename_mat(bpy.types.Operator):
    """Rename all material slots of selected meshes to <mesh>_<AA>_Mat"""
    bl_idname = "sceasar.tex_rename_mat"
    bl_label = "Rename Material Slots to <obj>_<AA>_Mat"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return any(obj.type == 'MESH' for obj in context.selected_objects)
    
    def execute(self, context):
        count = rename_material_slots_for_selected(context, verbose=True)
        self.report({'INFO'}, f"Renamed {count} materials (see console for details).")
        return {'FINISHED'}


# ------------------------
# Registration helpers
# ------------------------
classes = [SCEASAR_OT_TEX_rename_mat]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass

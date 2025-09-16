import bpy
from pathlib import Path


class SCEASAR_OT_import_mod_master(bpy.types.Operator):
    """Append collections from mod/blender/master/<.blend> into current file.
       If a collection already exists, delete it before importing."""
    bl_idname = "sceasar.import_mod_master"
    bl_label = "Import Mod Master"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Ensure file is saved
        current_file = Path(bpy.data.filepath)
        if not current_file:
            self.report({'ERROR'}, "Please save the current Blender file first.")
            return {'CANCELLED'}

        # Navigate to master folder
        try:
            root_path = current_file.parents[3]
        except IndexError:
            self.report({'ERROR'}, "Invalid folder structure. Expected: scene/workfile/mod/blender/local")
            return {'CANCELLED'}

        mod_master_folder = root_path / "mod" / "blender" / "master"

        # Find .blend files
        blend_files = list(mod_master_folder.glob("*.blend"))
        if not blend_files:
            self.report({'ERROR'}, f"No .blend file found in {mod_master_folder}")
            return {'CANCELLED'}

        # Use the first .blend (or extend later with picker)
        mod_master_file = blend_files[0]
        self.report({'INFO'}, f"Appending collections from {mod_master_file.name}")

        # Get names of collections to import
        with bpy.data.libraries.load(str(mod_master_file), link=False) as (data_from, data_to):
            collections_to_import = list(data_from.collections)

        # --- Remove existing collections with same names ---
        for col_name in collections_to_import:
            if col_name in bpy.data.collections:
                col = bpy.data.collections[col_name]

                # Unlink from scenes
                for scene in bpy.data.scenes:
                    if col.name in scene.collection.children:
                        scene.collection.children.unlink(col)

                # Unlink from parent collections
                for parent_col in bpy.data.collections:
                    if col.name in parent_col.children:
                        parent_col.children.unlink(col)

                # Remove collection
                bpy.data.collections.remove(col)

        # Purge orphan data
        bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)

        # --- Append collections ---
        with bpy.data.libraries.load(str(mod_master_file), link=False) as (data_from, data_to):
            data_to.collections = data_from.collections

        # Link imported collections to active scene
        for col in data_to.collections:
            if col is not None and col.name not in bpy.context.scene.collection.children:
                bpy.context.scene.collection.children.link(col)

        self.report({'INFO'}, "✅ Collections replaced and imported successfully.")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(SCEASAR_OT_import_mod_master)


def unregister():
    bpy.utils.unregister_class(SCEASAR_OT_import_mod_master)


if __name__ == "__main__":
    register()
    # Run immediately
    bpy.ops.sceasar.import_mod_master()

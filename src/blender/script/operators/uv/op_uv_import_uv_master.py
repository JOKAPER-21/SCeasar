import bpy
from pathlib import Path


class SCEASAR_OT_import_uv_master(bpy.types.Operator):
    """Replace the active collection with the version from mod/blender/master/<.blend>"""
    bl_idname = "sceasar.import_mod_master"
    bl_label = "Import UV Master Collection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Ensure current file is saved
        current_file = Path(bpy.data.filepath)
        if not current_file:
            self.report({'ERROR'}, "Please save the current Blender file first.")
            return {'CANCELLED'}

        # Get selected collection
        layer_col = context.view_layer.active_layer_collection
        if not layer_col:
            self.report({'ERROR'}, "No collection selected in the Outliner.")
            return {'CANCELLED'}
        col_name = layer_col.collection.name
        self.report({'INFO'}, f"Selected collection: {col_name}")

        # Path to master .blend
        try:
            root_path = current_file.parents[3]
        except IndexError:
            self.report({'ERROR'}, "Invalid folder structure. Expected: scene/workfile/mod/blender/local")
            return {'CANCELLED'}

        master_folder = root_path / "mod" / "blender" / "master"
        blend_files = list(master_folder.glob("*.blend"))
        if not blend_files:
            self.report({'ERROR'}, f"No .blend file found in {master_folder}")
            return {'CANCELLED'}
        master_file = blend_files[0]

        # Check if collection exists in master file
        with bpy.data.libraries.load(str(master_file), link=False) as (data_from, _):
            if col_name not in data_from.collections:
                self.report({'ERROR'}, f"Collection '{col_name}' not found in {master_file.name}")
                return {'CANCELLED'}

        # --- Remove old collection ---
        old_col = bpy.data.collections.get(col_name)
        if old_col:
            # Unlink from scenes
            for scene in bpy.data.scenes:
                if col_name in scene.collection.children.keys():
                    scene.collection.children.unlink(old_col)

            # Unlink from parent collections
            for parent in bpy.data.collections:
                if col_name in parent.children.keys():
                    parent.children.unlink(old_col)

            # Remove it completely
            bpy.data.collections.remove(old_col)

        # Purge orphans (cleans unused datablocks)
        bpy.ops.outliner.orphans_purge(
            do_local_ids=True,
            do_linked_ids=True,
            do_recursive=True
        )

        # --- Append fresh collection ---
        with bpy.data.libraries.load(str(master_file), link=False) as (data_from, data_to):
            data_to.collections = [col_name]

        # Link to current scene
        new_col = bpy.data.collections.get(col_name)
        if new_col and col_name not in context.scene.collection.children.keys():
            context.scene.collection.children.link(new_col)

        self.report({'INFO'}, f"✅ Collection '{col_name}' refreshed from {master_file.name}")
        return {'FINISHED'}


# ---------------- Register ----------------
classes = [SCEASAR_OT_import_uv_master]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

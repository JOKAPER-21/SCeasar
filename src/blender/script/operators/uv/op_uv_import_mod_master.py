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

        # Get selected (active) collection
        layer_col = context.view_layer.active_layer_collection
        if not layer_col:
            self.report({'ERROR'}, "No collection selected in the Outliner.")
            return {'CANCELLED'}
        col_name = layer_col.collection.name
        self.report({'INFO'}, f"Selected collection: {col_name}")

        # Path to master .blend
        try:
            root_path = current_file.parents[4]
        except IndexError:
            self.report({'ERROR'}, "Invalid folder structure. Expected: scene/workfile/mod/blender/local")
            return {'CANCELLED'}

        master_folder = root_path / "mod" / "blender" / "local" / "master"
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

        # --- Remove old collection but remember parents ---
        old_col = bpy.data.collections.get(col_name)
        parents = []

        if old_col:
            # Save parent collections
            for parent in bpy.data.collections:
                if col_name in parent.children:
                    parents.append(parent)

            # Save scene root only if no other parents exist
            if not parents and col_name in context.scene.collection.children:
                parents.append(context.scene.collection)

            # Unlink from all parents
            for parent in parents:
                if col_name in parent.children:
                    parent.children.unlink(old_col)

            # Remove it completely
            bpy.data.collections.remove(old_col)

        # Purge orphans until nothing left
        while bpy.ops.outliner.orphans_purge(
            do_local_ids=True,
            do_linked_ids=True,
            do_recursive=True
        ) != {'CANCELLED'}:
            pass

        # --- Append fresh collection ---
        with bpy.data.libraries.load(str(master_file), link=False) as (data_from, data_to):
            data_to.collections = [col_name]

        # Link back to previous parent(s)
        new_col = bpy.data.collections.get(col_name)
        if new_col:
            for parent in parents:
                if col_name not in parent.children:
                    parent.children.link(new_col)

        # ✅ Always return a set
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

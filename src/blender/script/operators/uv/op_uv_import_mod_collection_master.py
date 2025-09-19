import bpy
from pathlib import Path

class SCEASAR_OT_import_all_collections(bpy.types.Operator):
    """Import all collections from mod/blender/master/<.blend>, preserving empty hierarchy"""
    bl_idname = "sceasar.import_all_collections"
    bl_label = "Import All Master Collections (Empty Only)"
    bl_options = {'REGISTER', 'UNDO'}

    def get_collection_paths(self, collection, parent_path=""):
        """Return full paths of collection and children"""
        path = f"{parent_path}/{collection.name}" if parent_path else collection.name
        paths = [path]
        for child in collection.children:
            paths.extend(self.get_collection_paths(child, path))
        return paths

    def execute(self, context):
        # Ensure current file is saved
        current_file = Path(bpy.data.filepath)
        if not current_file:
            self.report({'ERROR'}, "Please save the current Blender file first.")
            return {'CANCELLED'}

        # Determine master folder path
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

        # Get collections in master file
        with bpy.data.libraries.load(str(master_file), link=False) as (data_from, _):
            master_collections = data_from.collections  # list of strings

        if not master_collections:
            self.report({'ERROR'}, f"No collections found in {master_file.name}")
            return {'CANCELLED'}

        # Get existing hierarchy paths
        existing_paths = set()
        for col in bpy.data.collections:
            existing_paths.update(self.get_collection_paths(col))

        # Determine which collections to import
        collections_to_import = [col_name for col_name in master_collections if col_name not in existing_paths]

        if not collections_to_import:
            self.report({'INFO'}, "No new collections to import (all hierarchies exist)")
            return {'FINISHED'}

        # Import collections
        with bpy.data.libraries.load(str(master_file), link=False) as (data_from, data_to):
            data_to.collections = collections_to_import

        # Ensure only string names
        collections_to_import = [c if isinstance(c, str) else c.name for c in collections_to_import]

        # First pass: link to scene and remove objects (make empty)
        for col_name in collections_to_import:
            col = bpy.data.collections.get(col_name)
            if not col:
                continue

            # Remove all objects
            for obj in list(col.objects):
                col.objects.unlink(obj)

            # Link to scene collection if not already
            if col.name not in [c.name for c in context.scene.collection.children]:
                context.scene.collection.children.link(col)

        # Second pass: restore parent-child relationships
        parent_map = {}
        for col_name in collections_to_import:
            col = bpy.data.collections.get(col_name)
            if not col:
                continue
            # Track master parents
            parents = [parent.name for parent in bpy.data.collections
                       if col.name in [c.name for c in parent.children]]
            if not parents:
                parents = [context.scene.collection.name]  # fallback
            parent_map[col_name] = parents

        for col_name in collections_to_import:
            col = bpy.data.collections.get(col_name)
            if not col:
                continue
            for parent_name in parent_map.get(col_name, []):
                parent = context.scene.collection if parent_name == context.scene.collection.name else bpy.data.collections.get(parent_name)
                if parent and col.name not in [c.name for c in parent.children]:
                    parent.children.link(col)

        self.report({'INFO'}, f"✅ Imported {len(collections_to_import)} empty collections from {master_file.name}")
        return {'FINISHED'}


# ---------------- Register ----------------
classes = [SCEASAR_OT_import_all_collections]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()

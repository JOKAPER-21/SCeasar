import bpy
import os
import re

class SCEASAR_OT_uv_export_version_fbx(bpy.types.Operator):
    """Export selected collections as FBX with version number"""
    bl_idname = "sceasar.export_uv_version_fbx"
    bl_label = "Export Collection FBX (Versioned)"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        collection = context.view_layer.active_layer_collection.collection
        if not collection:
            self.report({'ERROR'}, "No collection selected!")
            return {'CANCELLED'}

        blend_path = bpy.data.filepath
        if not blend_path:
            self.report({'ERROR'}, "Please save your Blender file first!")
            return {'CANCELLED'}

        blend_dir = os.path.dirname(blend_path)
        blend_name = os.path.splitext(os.path.basename(blend_path))[0]

        export_dir = os.path.join(blend_dir, "export", blend_name)
        os.makedirs(export_dir, exist_ok=True)

        # Versioning logic
        base_name = f"{collection.name}_v"
        existing_versions = [
            f for f in os.listdir(export_dir)
            if re.match(rf"{re.escape(collection.name)}_v\d+\.fbx", f)
        ]

        if existing_versions:
            versions = [int(re.search(r'v(\d+)', f).group(1)) for f in existing_versions]
            next_version = max(versions) + 1
        else:
            next_version = 1

        export_path = os.path.join(export_dir, f"{collection.name}_v{next_version:02d}.fbx")

        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')

        # Select objects in collection
        for obj in collection.all_objects:
            obj.select_set(True)

        # Export FBX
        bpy.ops.export_scene.fbx(
            filepath=export_path,
            use_selection=True,
            apply_unit_scale=True,
            bake_space_transform=True
        )

        self.report({'INFO'}, f"Exported {collection.name} to {export_path}")
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(SCEASAR_OT_uv_export_version_fbx.bl_idname)


def register():
    bpy.utils.register_class(SCEASAR_OT_uv_export_version_fbx)
    bpy.types.TOPBAR_MT_file_export.append(menu_func)


def unregister():
    bpy.utils.unregister_class(SCEASAR_OT_uv_export_version_fbx)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func)

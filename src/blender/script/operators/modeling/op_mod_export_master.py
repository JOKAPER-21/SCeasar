import bpy
from pathlib import Path


class SCEASAR_OT_MOD_MASTER(bpy.types.Operator):
    """Save current Blender file into a 'master' subfolder next to the current file"""
    bl_idname = "sceasar.save_to_master"
    bl_label = "Save to master"
    bl_options = {'REGISTER', 'UNDO'}

    filename_override: bpy.props.StringProperty(
        name="Filename",
        description="Optional override for filename (including .blend). Leave empty to reuse current filename.",
        default=""
    )

    def execute(self, context):
        # 🔎 Check if file has been saved
        current_fp = bpy.data.filepath
        if not current_fp:
            self.report({'ERROR'}, "❌ Please save the current Blender file before using 'Save to master'.")
            return {'CANCELLED'}

        base_dir = Path(current_fp).parent

        # 📂 Ensure master directory exists
        master_dir = base_dir / "master"
        try:
            master_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            self.report({'ERROR'}, f"❌ Could not create master folder: {e}")
            return {'CANCELLED'}

        # 📝 Determine target filename
        if self.filename_override.strip():
            target_name = self.filename_override.strip()
            if not target_name.lower().endswith(".blend"):
                target_name += ".blend"
        else:
            target_name = Path(current_fp).name

        target_path = master_dir / target_name

        # 💾 Save a copy into master folder (don’t switch open file)
        try:
            bpy.ops.wm.save_as_mainfile(filepath=str(target_path), copy=True)
        except Exception as e:
            self.report({'ERROR'}, f"❌ Failed to save to master: {e}")
            return {'CANCELLED'}

        self.report({'INFO'}, f"✅ Saved copy to: {str(target_path)}")
        return {'FINISHED'}


# Add operator to File menu
def menu_func(self, context):
    self.layout.operator(SCEASAR_OT_MOD_MASTER.bl_idname, text="Save to master")


classes = (SCEASAR_OT_MOD_MASTER,)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_file.append(menu_func)


def unregister():
    bpy.types.TOPBAR_MT_file.remove(menu_func)
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

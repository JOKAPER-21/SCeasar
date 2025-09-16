import bpy
from bpy.types import Operator
from pathlib import Path
from datetime import datetime
import re

class SCEASAR_OT_MOD_MASTER(Operator):
    """Automatically save current Blender file into a 'master' folder next to 'local/'"""
    bl_idname = "sceasar.save_to_master"
    bl_label = "Save to Master"
    bl_options = {'REGISTER', 'UNDO'}

    enable_backups: bpy.props.BoolProperty(
        name="Enable Backups",
        description="Create timestamped backups in the master folder",
        default=False
    ) # type: ignore

    use_relative_paths: bpy.props.BoolProperty(
        name="Use Relative Paths",
        description="Save file with relative paths for portability",
        default=True
    ) # type: ignore

    @classmethod
    def poll(cls, context):
        return bool(bpy.data.filepath)

    def execute(self, context):
        current_fp = bpy.data.filepath
        if not current_fp:
            self.report({'ERROR'}, "❌ Please save the current Blender file first.")
            return {'CANCELLED'}

        # Go up one level from 'local/' to 'Blender/'
        base_dir = Path(current_fp).parent.parent
        master_dir = base_dir / "master"
        master_dir.mkdir(parents=True, exist_ok=True)

        # Original filename
        original_name = Path(current_fp).stem  # without extension

        # Modify filename: replace _mod with _mst and remove _vXX
        mod_name = re.sub(r'_mod', '_mst', original_name, flags=re.IGNORECASE)
        mod_name = re.sub(r'_v\d{2,}', '', mod_name, flags=re.IGNORECASE)

        target_name = f"{mod_name}.blend"
        target_path = master_dir / target_name

        # Create backup if enabled and file exists
        if target_path.exists() and self.enable_backups:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = master_dir / f"{Path(target_name).stem}_backup_{timestamp}.blend"
            try:
                bpy.ops.wm.save_as_mainfile(filepath=str(backup_path), copy=True)
                self.report({'INFO'}, f"Created backup at: {backup_path}")
            except Exception as e:
                self.report({'WARNING'}, f"Failed to create backup: {e}")

        # Save copy to master folder
        try:
            bpy.ops.wm.save_as_mainfile(
                filepath=str(target_path),
                copy=True,
                relative_remap=self.use_relative_paths
            )
        except Exception as e:
            self.report({'ERROR'}, f"❌ Failed to save to master: {e}")
            return {'CANCELLED'}

        self.report({'INFO'}, f"✅ Saved copy to: {target_path}")
        return {'FINISHED'}

# Register operator
def register():
    bpy.utils.register_class(SCEASAR_OT_MOD_MASTER)

def unregister():
    bpy.utils.unregister_class(SCEASAR_OT_MOD_MASTER)

if __name__ == "__main__":
    register()
    bpy.ops.sceasar.save_to_master()

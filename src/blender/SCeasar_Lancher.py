import os
import shutil
import subprocess
import sys

# Source and destination paths
src = r"S:\Pipeline\development\CG_SProjects\SCeasar\src\blender\script"
dst = r"C:\Users\ANANTHAN\AppData\Roaming\Blender Foundation\Blender\4.5\scripts\addons\SCeasar"

# Path to Blender executable
blender_exe = r"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe"

def replace_folder(src, dst):
    if not os.path.exists(src):
        print(f"Source folder does not exist: {src}")
        return

    if os.path.exists(dst):
        print(f"Removing existing folder: {dst}")
        shutil.rmtree(dst)

    print(f"Copying {src} to {dst}")
    shutil.copytree(src, dst)
    print("✅ Folder replaced successfully.")

def enable_addon_in_blender(blender_path, addon_name):
    # Blender Python script to enable addon
    enable_script = f"""import bpy
bpy.ops.preferences.addon_enable(module="{addon_name}")
bpy.ops.wm.save_userpref()
"""

    # Save temporary script
    temp_script_path = os.path.join(os.environ.get("TEMP", "."), "enable_addon.py")
    with open(temp_script_path, "w") as f:
        f.write(enable_script)

    # Run Blender in background to execute script
    subprocess.run([blender_path, "--background", "--python", temp_script_path])
    os.remove(temp_script_path)
    print(f"✅ Addon '{addon_name}' enabled.")

def open_blender(blender_path):
    if os.path.exists(blender_path):
        print(f"Launching Blender: {blender_path}")
        subprocess.Popen([blender_path])
    else:
        print(f"Blender executable not found: {blender_path}")

if __name__ == "__main__":
    replace_folder(src, dst)
    enable_addon_in_blender(blender_exe, "SCeasar")
    open_blender(blender_exe)

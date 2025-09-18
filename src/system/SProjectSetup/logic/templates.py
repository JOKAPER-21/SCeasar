import shutil
import os
from .versioning import get_next_version

def copy_template(template_info, project_path, project_name):
    """Copy and version template into project structure"""
    to_folder = os.path.join(project_path, *template_info["to"])
    os.makedirs(to_folder, exist_ok=True)

    ext = os.path.splitext(template_info["from"])[1]
    versioned_path = get_next_version(to_folder, project_name, ext)

    src = template_info["from"]
    if not os.path.exists(src):
        raise FileNotFoundError(f"Template not found: {src}")
    shutil.copy(src, versioned_path)
    return versioned_path

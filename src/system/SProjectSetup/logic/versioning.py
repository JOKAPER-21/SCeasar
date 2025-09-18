import os

def get_next_version(path, prefix, ext):
    """
    Returns next version filename (v01, v02, etc.)
    """
    version = 1
    while True:
        filename = f"{prefix}_v{version:02d}{ext}"
        full_path = os.path.join(path, filename)
        if not os.path.exists(full_path):
            return full_path
        version += 1

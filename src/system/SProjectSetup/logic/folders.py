import os

def create_folders(base_path, folder_structure):
    """Create nested folder structure"""
    created = []
    for parts in folder_structure:
        path = os.path.join(base_path, *parts)
        os.makedirs(path, exist_ok=True)
        created.append(path)
    return created

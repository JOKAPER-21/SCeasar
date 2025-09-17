import bpy

def index_to_letters(index):
    """Convert 0 → AA, 1 → AB, 25 → AZ, 26 → BA..."""
    letters = ""
    index += 26  # Start from AA instead of A
    while index >= 0:
        letters = chr(index % 26 + ord('A')) + letters
        index = index // 26 - 1
    return letters


class SCEASAR_OT_Add_Empty_Material(bpy.types.Operator):
    """Assign one new empty material per selected mesh (override old ones)"""
    bl_idname = "sceasar.add_empty_mat"
    bl_label = "Assign Empty Material"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        selected_meshes = [obj for obj in context.selected_objects if obj.type == 'MESH']

        for obj in selected_meshes:
            # Remove "_Geo" from object name if present
            base_name = obj.name.replace("_Geo", "")
            
            # Always use slot index 0 (since only one material is kept)
            slot_letters = index_to_letters(0)  # "AA"
            
            # Build material name
            mat_name = f"{base_name}_{slot_letters}_Mat"
            
            # Create new material (reuse if already exists)
            if mat_name in bpy.data.materials:
                mat = bpy.data.materials[mat_name]
            else:
                mat = bpy.data.materials.new(name=mat_name)
                mat.use_nodes = False  # keep empty
            
            # Clear all material slots from the object
            obj.data.materials.clear()
            
            # Assign the new material
            obj.data.materials.append(mat)
            
            self.report({'INFO'}, f"Assigned {mat_name} to {obj.name}")
        
        return {'FINISHED'}


# Register / Unregister
def register():
    bpy.utils.register_class(SCEASAR_OT_Add_Empty_Material)

def unregister():
    bpy.utils.unregister_class(SCEASAR_OT_Add_Empty_Material)


if __name__ == "__main__":
    register()

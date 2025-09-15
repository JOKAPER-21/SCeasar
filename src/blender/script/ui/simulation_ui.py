import bpy

class SCEASAR_PT_Simulation(bpy.types.Panel):
    bl_label = "Simulation"
    bl_idname = "SCEASAR_PT_simulation"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_main"

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'SIMULATION'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Simulation Tools", icon="EXPERIMENTAL")

class SCEASAR_PT_Export_Simulation(bpy.types.Panel):
    bl_label = "Export"
    bl_idname = "SCEASAR_PT_export_simulation"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"
    bl_parent_id = "SCEASAR_PT_simulation"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene.sceasar_props.mode == 'SIMULATION'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Export Options", icon="EXPORT")

def register():
    bpy.utils.register_class(SCEASAR_PT_Simulation)
    bpy.utils.register_class(SCEASAR_PT_Export_Simulation)

def unregister():
    bpy.utils.unregister_class(SCEASAR_PT_Export_Simulation)
    bpy.utils.unregister_class(SCEASAR_PT_Simulation)
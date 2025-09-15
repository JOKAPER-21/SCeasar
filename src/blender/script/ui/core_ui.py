import bpy

class SCEASAR_Properties(bpy.types.PropertyGroup):
    mode: bpy.props.EnumProperty(
        name="Department",
        items=[
            ('MODELING', "Modeling", "Modeling Tools", 'GHOST_ENABLED', 0),
            ('UV', "UV Mapping", "UV Tools", 'GROUP_UVS', 1),
            ('TEXTURING', "Texturing", "Texturing Tools", 'TEXTURE', 2),
            ('LOOKDEV', "Lookdev", "Look Development Tools", 'MATERIAL', 3),
            ('RIGGING', "Rigging", "Rigging Tools", 'BONE_DATA', 4),
            ('LAYOUT', "Layout", "Layout / Previs Tools", 'OUTLINER_OB_CAMERA', 5),
            ('ANIMATION', "Animation", "Animation Tools", 'OUTLINER_OB_ARMATURE', 6),
            ('SIMULATION', "Simulation", "Simulation Tools", 'EXPERIMENTAL', 7),
            ('FX', "Effects", "FX Tools", 'OUTLINER_OB_POINTCLOUD', 8),
            ('LIGHTING', "Lighting", "Lighting Tools", 'OUTLINER_OB_LIGHT', 9),
            ('COMPOSITING', "Compositing", "Compositing Tools", 'NODETREE', 10),
            ('RENDERING', "Rendering", "Rendering Tools", 'RENDER_STILL', 11),
        ],
        default='MODELING'
    ) # type: ignore

class SCEASAR_PT_Main(bpy.types.Panel):
    bl_label = "S Ceasar"
    bl_idname = "SCEASAR_PT_main"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "S Ceasar"

    def draw(self, context):
        layout = self.layout
        props = context.scene.sceasar_props
        row = layout.row()
        row.scale_y = 1.5
        row.prop(props, "mode", text="")

classes = (SCEASAR_Properties, SCEASAR_PT_Main)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.sceasar_props = bpy.props.PointerProperty(type=SCEASAR_Properties)

def unregister():
    del bpy.types.Scene.sceasar_props
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
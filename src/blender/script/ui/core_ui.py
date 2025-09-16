import bpy

class SCEASAR_Properties(bpy.types.PropertyGroup):
    mode: bpy.props.EnumProperty(
        name="Department",
        items=[
            ('MODELING', "Modeling", "Modeling Tools", 'GHOST_ENABLED', 0),
            ('UV', "UV Mapping", "UV Tools", 'UV', 1),
            ('TEXTURING', "Texturing", "Texturing Tools", 'BRUSHES_ALL', 2),
            ('LOOKDEV', "Lookdev", "Look Development Tools", 'MATSHADERBALL', 3),
            ('RIGGING', "Rigging", "Rigging Tools", 'BONE_DATA', 4),
            ('ANIMATION', "Animation", "Animation Tools", 'OUTLINER_OB_ARMATURE', 5),
            ('FX', "Effects", "FX Tools", 'OUTLINER_OB_POINTCLOUD', 6),
            ('LIGHTING', "Lighting", "Lighting Tools", 'OUTLINER_OB_LIGHT', 7),
            ('COMPOSITING', "Compositing", "Compositing Tools", 'NODETREE', 8),
            ('RENDERING', "Rendering", "Rendering Tools", 'RENDER_STILL', 9),
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
        row.prop(props, "mode", expand=True) # type: ignore

classes = (SCEASAR_Properties, SCEASAR_PT_Main)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.sceasar_props = bpy.props.PointerProperty(type=SCEASAR_Properties)

def unregister():
    del bpy.types.Scene.sceasar_props
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
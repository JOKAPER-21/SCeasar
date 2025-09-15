from . import (
    core_ui,
    modeling_ui,
    uv_ui,
    texturing_ui,
    lookdev_ui,
    rigging_ui,
    animation_ui,
    fx_ui,
    lighting_ui,
    compositing_ui,
    rendering_ui
)

def register():
    core_ui.register()
    modeling_ui.register()
    uv_ui.register()
    texturing_ui.register()
    lookdev_ui.register()
    rigging_ui.register()
    animation_ui.register()
    fx_ui.register()
    lighting_ui.register()
    compositing_ui.register()
    rendering_ui.register()

def unregister():
    rendering_ui.unregister()
    compositing_ui.unregister()
    lighting_ui.unregister()
    fx_ui.unregister()
    animation_ui.unregister()
    rigging_ui.unregister()
    lookdev_ui.unregister()
    texturing_ui.unregister()
    uv_ui.unregister()
    modeling_ui.unregister()
    core_ui.unregister()
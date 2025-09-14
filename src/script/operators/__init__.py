from . import modeling, uv, texturing, lookdev, rigging, layout, animation, simulation, fx, lighting, compositing, rendering

def register():
    modeling.register()
    uv.register()
    texturing.register()
    lookdev.register()
    rigging.register()
    layout.register()
    animation.register()
    simulation.register()
    fx.register()
    lighting.register()
    compositing.register()
    rendering.register()

def unregister():
    rendering.unregister()
    compositing.unregister()
    lighting.unregister()
    fx.unregister()
    simulation.unregister()
    animation.unregister()
    layout.unregister()
    rigging.unregister()
    lookdev.unregister()
    texturing.unregister()
    uv.unregister()
    modeling.unregister()
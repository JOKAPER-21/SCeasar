from . import modeling, uv, texturing, lookdev, rigging, animation, fx, lighting, compositing, rendering, viz_operators

def register():
    modeling.register()
    uv.register()
    texturing.register()
    lookdev.register()
    rigging.register()
    animation.register()
    fx.register()
    lighting.register()
    compositing.register()
    rendering.register()
    viz_operators.register()

def unregister():
    viz_operators.unregister()
    rendering.unregister()
    compositing.unregister()
    lighting.unregister()
    fx.unregister()
    animation.unregister()
    rigging.unregister()
    lookdev.unregister()
    texturing.unregister()
    uv.unregister()
    modeling.unregister()
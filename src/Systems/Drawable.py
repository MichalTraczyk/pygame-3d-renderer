from src.Systems.Drawer import Drawer


class Drawable:

    def __init__(self):
        super().__init__()
        Drawer.RegisterDrawable(self)

    def draw(self, screen, camera):
        pass
    def kill(self):
        if hasattr(super(), 'kill'):
            super().kill()
        Drawer.unregister_drawable(self)
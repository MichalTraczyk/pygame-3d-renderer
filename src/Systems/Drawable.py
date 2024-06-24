from src.Systems.Drawer import Drawer


class Drawable:

    def __init__(self):
        super().__init__()
        Drawer.RegisterDrawable(self)

    def draw(self, screen, camera):
        """
        Event function that is called whenever we want to draw object on the screen
        """
        pass
    def kill(self):
        """
        Destroys the object and all parents classes
        """
        if hasattr(super(), 'kill'):
            super().kill()
        Drawer.unregister_drawable(self)
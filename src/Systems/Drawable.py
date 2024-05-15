from src.Systems.Drawer import Drawer


class Drawable:
    def __init__(self):
        super().__init__()
        Drawer.RegisterDrawable(self)

    def Draw(self,screen):
        pass

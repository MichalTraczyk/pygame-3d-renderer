from src.Systems.Drawable import Drawable
from src.Systems.Updatable import Updatable


class Editor(Updatable,Drawable):
    def __init__(self,position):
        super().__init__()
    def get_height(self):
        return 70
    def kill(self):
        super().kill()
from Systems.Updater import Updater


class Updatable:
    def __init__(self):
        super().__init__()
        Updater.RegisterDrawable(self)
    def Update(self,deltaTime):
        pass

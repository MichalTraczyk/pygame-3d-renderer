from src.Systems.Updater import Updater


class Updatable:
    def __init__(self):
        super().__init__()
        Updater.RegisterUpdatable(self)
    def Update(self,deltaTime):
        pass

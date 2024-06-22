from src.Systems.Updater import Updater


class Updatable:
    def __init__(self):
        super().__init__()
        Updater.register_updatable(self)

    def update(self, deltaTime):
        pass

    def kill(self):
        if hasattr(super(), 'kill'):
            super().kill()
        Updater.unregister_updatable(self)
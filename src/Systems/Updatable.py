from src.Systems.Updater import Updater


class Updatable:
    def __init__(self):
        super().__init__()
        Updater.register_updatable(self)

    def _update(self, deltaTime):
        """
        Event function that is called eventy frame
        @param deltaTime: Time since last frame
        @type deltaTime: float
        """
        pass

    def kill(self):
        """
        Destroys the object and all parents classes
        """
        if hasattr(super(), 'kill'):
            super().kill()
        Updater.unregister_updatable(self)
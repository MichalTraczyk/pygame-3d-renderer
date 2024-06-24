class Updater:

    updatables = []
    @classmethod
    def register_updatable(cls, updatable):
        """
        Registers a updatable so update() event is called
        @param updatable: Updatable to register
        @type updatable: Updatable
        """
        cls.updatables.append(updatable)

    @classmethod
    def unregister_updatable(cls, updatable):
        """
        Unregisters a updatable so update() event is no longer called
        @param updatable: Updatable to unregister
        @type updatable: Updatable
        """
        if updatable in cls.updatables:
            cls.updatables.remove(updatable)

    @classmethod
    def update(cls, dt):
        """
        Calls update() method on all registered updatables
        @param dt: Time in seconds since the last frame
        @type dt: float
        """
        for d in cls.updatables:
            d.update(dt)

class Updater:

    updatables = []
    @classmethod
    def register_updatable(cls, updatable):
        cls.updatables.append(updatable)

    @classmethod
    def unregister_updatable(cls, updatable):
        if updatable in cls.updatables:
            cls.updatables.remove(updatable)

    @classmethod
    def update(cls, dt):
        for d in cls.updatables:
            d.update(dt)

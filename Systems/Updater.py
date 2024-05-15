class Updater:

    updatables = []
    @classmethod
    def RegisterDrawable(cls,updatable):
        cls.updatables.append(updatable)

    @classmethod
    def UnregisterDrawable(cls,updatable):
        if updatable in cls.updatables:
            cls.updatables.remove(updatable)

    @classmethod
    def Update(cls,dt):
        for d in cls.updatables:
            d.Update(dt)

class Drawer:

    drawables = []
    @classmethod
    def RegisterDrawable(cls,drawable):
        cls.drawables.append(drawable)

    @classmethod
    def UnregisterDrawable(cls,drawable):
        if drawable in cls.drawables:
            cls.drawables.remove(drawable)

    @classmethod
    def Draw(cls,screen):
        for d in cls.drawables:
            d.Draw(screen)

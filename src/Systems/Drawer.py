class Drawer:
    drawables = []
    is_dirty = True  # na True jeśli była jakakolwiek zmiana na scenie

    @classmethod
    def RegisterDrawable(cls, drawable):
        cls.drawables.append(drawable)

    @classmethod
    def unregister_drawable(cls, drawable):
        if drawable in cls.drawables:
            cls.drawables.remove(drawable)

    @classmethod
    def draw(cls, screen, camera):
        for d in cls.drawables:
            d.draw(screen, camera)

class Drawer:
    drawables = []
    is_dirty = True  # na True jeśli była jakakolwiek zmiana na scenie

    @classmethod
    def RegisterDrawable(cls, drawable):
        """
        Registers a drawable so it's allowed to be on the screen
        @param drawable: Drawable to register
        @type drawable: Drawable
        """
        cls.drawables.append(drawable)

    @classmethod
    def unregister_drawable(cls, drawable):
        """
        Unregisters a drawable so it's no more drawn on the screen
        @param drawable: Drawable to unregister
        @type drawable: Drawable
        """
        if drawable in cls.drawables:
            cls.drawables.remove(drawable)

    @classmethod
    def draw(cls, screen, camera):
        """
        Draws all registered drawables to the given screen using given camera
        @param screen: Screen to draw
        @type screen: pygame.Surface
        @param camera: Camera to draw
        @type camera: Camera
        """
        for d in cls.drawables:
            d.draw(screen, camera)

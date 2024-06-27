from src.Systems.Updatable import Updatable
from src.UI.UIElements.Label import Label


class FpsLabel(Label, Updatable):

    def __init__(self, size, position):
        super().__init__(size, position, "")

    def _draw(self, screen, camera):
        super(FpsLabel, self)._draw(screen, camera)

    def _update(self, deltaTime):
        self.change_text(f'Fps: {int(1 / deltaTime)}')

from src.MeshSystem.MeshRenderer import MeshRenderer
from src.Systems.Updatable import Updatable
from src.UI.UIElements.Label import Label


class PerformanceLabel(Label, Updatable):

    def __init__(self, size, position):
        super().__init__(size, position, "")

    def _draw(self, screen, camera):
        super(PerformanceLabel, self)._draw(screen, camera)

    def _update(self, dt):
        self.change_text(f'Face count: {len(MeshRenderer.faces)}   Fps: {int(1 / dt)}')

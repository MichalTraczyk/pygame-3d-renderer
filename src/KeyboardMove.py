from pygame import Vector3

from src.Math.Transform import Transform
from src.ModelPool import ModelPool
from src.Systems.EventSystem import EventSystem
from src.Systems.Updatable import Updatable


class KeyboardMove(Updatable):
    def __init__(self):
        super().__init__()
        self.parent = Transform()
        self.speed = 100
        ModelPool.add_change_listener(self.modelpool_changed)
    def modelpool_changed(self,pool):
        for i in pool:
            if i.get_parent() is None:
                i.set_parent(self.parent)

    def _update(self, deltaTime):
        _input = EventSystem.get_axis()
        self.parent.move(Vector3(_input.x, 0, _input.y))

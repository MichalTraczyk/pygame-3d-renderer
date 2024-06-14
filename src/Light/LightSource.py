from pygame import Vector3
from src.Math.Transform import Transform
from src.MeshSystem.WorldFace import WorldFace


class LightSource(Transform):

    def __init__(self, pos: Vector3, intensity: float):
        super().__init__(pos)
        self.intensity = intensity

    def get_light_level(self, face: WorldFace):
        return 0

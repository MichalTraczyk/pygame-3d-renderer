from pygame import Vector3

from src.Light.LightSource import LightSource
from src.Math.VectorMath import VectorMath
from src.MeshSystem.WorldFace import WorldFace


class DirectionalLight(LightSource):

    def __init__(self, pos: Vector3, direction: Vector3, intensity: float):
        super().__init__(pos, intensity)
        self.direction = direction

    def get_light_level(self, face: WorldFace):
        normal = VectorMath.face_normal(face)
        direction = VectorMath.normalize_vector(self.transform_point(self.direction) - self.get_position())  # do sprawdzenia

        dot = VectorMath.Dot(normal, direction)
        if dot < 0:
            dot = 0
        return self.intensity * dot
    def __str__(self):
        return "Directional Light"


class PointLight(LightSource):
    def __init__(self, pos: Vector3, intensity: float):
        super().__init__(pos, intensity)

    def get_light_level(self, face: WorldFace):
        normal = VectorMath.face_normal(face)
        middle = VectorMath.face_middle(face)
        direction = VectorMath.normalize_vector(super().get_position() - middle)

        dot = VectorMath.Dot(normal, direction)
        if dot < 0:
            dot = 0

        return self.intensity * dot / VectorMath.Length(VectorMath.face_middle(face))
    def __str__(self):
        return "Point Light"


class SkyboxLight(LightSource):
    def __init__(self, pos: Vector3, intensity: float):
        super().__init__(pos, intensity)

    def get_light_level(self, face: WorldFace):
        return self.intensity

    def __str__(self):
        return "Skybox Light"

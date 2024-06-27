from pygame import Vector3, Color
from src.Math.Transform import Transform
from src.MeshSystem.WorldFace import WorldFace


class LightSource(Transform):

    def __init__(self, pos: Vector3, intensity: float, color: Color):
        super().__init__(pos)
        self.intensity = intensity
        self.color = color

    def get_light_level(self, face: WorldFace):
        """
        Calculates color of light that influence given face
        @param face: Face to calculate light level on
        @rtype Color
        @return: Color that influence given face
        """
        return Color(0,0,0)

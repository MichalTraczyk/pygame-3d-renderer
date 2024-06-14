from pygame import Color

from src.Light import LightSource
from src.MeshSystem.WorldFace import WorldFace


class LightManager:
    lights: [LightSource] = []

    @staticmethod
    def register_light(light: LightSource):
        LightManager.lights.append(light)

    @staticmethod
    def calculate_light(face: WorldFace):
        lightcolor = Color(0,0,0)
        for light in LightManager.lights:
            lightcolor += light.get_light_level(face)
        return lightcolor

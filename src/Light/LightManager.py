from src.Light import LightSource
from src.WorldFace import WorldFace


class LightManager:
    lights: [LightSource] = []

    @staticmethod
    def register_light(light: LightSource):
        LightManager.lights.append(light)

    @staticmethod
    def calculate_light(face: WorldFace):
        lightlevel = 0
        for light in LightManager.lights:
            lightlevel += light.get_light_level(face)
        if lightlevel < 0:
            lightlevel = 0
        if lightlevel > 1:
            lightlevel = 1
        return lightlevel

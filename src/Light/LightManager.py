from src.Light import LightSource
from src.MeshSystem.WorldFace import WorldFace


class LightManager:
    lights: [LightSource] = []
    lights_changed_listeners = []

    @staticmethod
    def add_change_listener(listener):
        LightManager.lights_changed_listeners.append(listener)
    @staticmethod
    def register_light(light: LightSource):
        LightManager.lights.append(light)
        for listener in LightManager.lights_changed_listeners:
            listener(LightManager.lights)

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

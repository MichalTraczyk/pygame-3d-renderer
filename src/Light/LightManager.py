from pygame import Color

from src.Light import LightSource
from src.MeshSystem.WorldFace import WorldFace


class LightManager:
    lights: [LightSource] = []
    lights_changed_listeners = []

    @staticmethod
    def add_change_listener(listener):
        """
        Adds listener that listens when a light count changes
        @param listener: method to call when a lights count changes
        """
        LightManager.lights_changed_listeners.append(listener)
    @staticmethod
    def register_light(light: LightSource):
        LightManager.lights.append(light)
        for listener in LightManager.lights_changed_listeners:
            listener(LightManager.lights)

    @staticmethod
    def unregister_light(light: LightSource):
        if light in LightManager.lights:
            LightManager.lights.remove(light)
            for listener in LightManager.lights_changed_listeners:
                listener(LightManager.lights)
    @staticmethod
    def calculate_light(face: WorldFace):
        lightcolor = Color(0,0,0)
        for light in LightManager.lights:
            lightcolor += light.get_light_level(face)
        return lightcolor

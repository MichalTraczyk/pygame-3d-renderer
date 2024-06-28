import pygame
from pygame import Vector2

from src.Camera import Camera
from src.KeyboardMove import KeyboardMove
from src.Light.LightManager import LightManager
from src.Light.LightSourcesTypes import *
from src.MeshSystem.DrawableMesh import DrawableMesh
from src.MeshSystem.MeshRenderer import MeshRenderer
from src.MeshSystem.Primitives import Primitives
from src.ModelPool import ModelPool
from src.UI.Screens.MainCanvas import MainCanvas
from src.Systems.Updater import Updater
from src.Systems.Drawer import Drawer
from src.Systems.EventSystem import EventSystem


class Screen:

    def __init__(self, res):

        """
        Initializes the Screen with the given resolution

        Sets up the Pygame display, initializes the camera, and sets up the main game loop

        @param res: The screen resolution (width, height)
        @type res: tuple
        """
        self.resolution = res
        pygame.init()

        self.screen = pygame.display.set_mode([self.resolution[0], self.resolution[1]])
        self.camera = Camera(40, self.resolution[0], self.resolution[1])

        self.running = True
        self.getTicksLastFrame = 0

        canvas = MainCanvas(Vector2(self.resolution[0], self.resolution[1]))
        LightManager.add_change_listener(canvas.hierarchy.lights_changed)
        ModelPool.add_change_listener(canvas.hierarchy.models_changed)
        kMove = KeyboardMove()
        obj = DrawableMesh(Vector3(0, -2, 1))
        obj.assign_mesh(Primitives.generate_plane(10, 1))
        LightManager.register_light(SkyboxLight(Vector3(0, 0, 0), 0.1, Color(255, 255, 255)))
        LightManager.register_light(DirectionalLight(Vector3(0, 0, 0),Vector3(1, -1, 0), 0.25, Color(255, 255, 255)))
        mesh = Primitives.generate_box()
        obj = DrawableMesh(Vector3(-1, 1, 1.7))
        obj.assign_mesh(mesh)
        obj.rotate(45)
        '''
        mesh = Primitives.generate_box()
        obj = DrawableMesh(Vector3(2, 0, 2))
        obj.assign_mesh(mesh)
        obj.rotate(10)
        obj = DrawableMesh(Vector3(-1, 1, 1.7))
        obj.assign_mesh(mesh)
        obj.rotate(45)
        obj = DrawableMesh(Vector3(-0.5, -2, 0.8))
        obj.assign_mesh(mesh)
        obj = DrawableMesh(Vector3(1, 2, 2))
        obj.assign_mesh(Primitives.generate_rotated_pyramid())
        obj = DrawableMesh(Vector3(0, -2, 1))
        obj.assign_mesh(Primitives.generate_plane(10, 1))

        LightManager.register_light(PointLight(Vector3(-1, 0.5, 0.5), 0.9, Color(255, 0, 0)))
        LightManager.register_light(PointLight(Vector3(2, 0.5, 0.5), 0.9, Color(0, 255, 0)))
        LightManager.register_light(SkyboxLight(Vector3(0, 0, 0), 1, Color(255, 255, 255)))
        LightManager.register_light(DirectionalLight(Vector3(0, 0, 0), Vector3(1, -1, 1), 0.5, Color(255, 255, 255)))
        '''
        EventSystem.add_on_quit_listener(self.on_quit)
        while self.running:
            self.t = pygame.time.get_ticks()
            self.deltaTime = (self.t - self.getTicksLastFrame) / 1000.0
            self.getTicksLastFrame = self.t

            EventSystem.update()

            if EventSystem.get_key_down(pygame.K_ESCAPE):
                self.on_quit()

            Updater.update(self.deltaTime)

            # obj.set_position(Vector3(math.sin(self.t / 400), math.cos(self.t / 400)-0.5, 3))
            # obj.rotate(self.deltaTime*200)
            if Drawer.is_dirty:
                self.screen.fill((0, 0, 0))
                MeshRenderer.draw_buffor(self.screen)
                Drawer.draw(self.screen, self.camera)
                pygame.display.flip()
                # Drawer.is_dirty = False

        pygame.quit()

    def on_quit(self):
        self.running = False

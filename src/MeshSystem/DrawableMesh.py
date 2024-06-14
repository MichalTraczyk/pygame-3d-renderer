import pygame
from pygame import Vector3, Color

from src import Camera
from src.Light.LightManager import LightManager
from src.Math.Transform import Transform
from src.Systems.Drawable import Drawable
from src.MeshSystem import Mesh
from src.Systems.Updatable import Updatable
from src.MeshSystem.WorldFace import WorldFace


class DrawableMesh(Updatable, Drawable, Transform):

    def __init__(self, pos):
        super().__init__()
        self.set_position(pos)
        self.mesh = None

    def assignMesh(self, mesh: Mesh):
        self.mesh = mesh

    def world_face_to_screen(self, face: WorldFace, camera: Camera):
        points = []
        for point in face.vectors():
            #world_pos = self.TransformPoint(point)
            points.append(camera.world_pos_to_screen(point))
        return points

    def draw(self, screen, camera: Camera):
        worldfaces: [WorldFace] = []
        for localFace in self.mesh.get_faces():
            worldface = WorldFace(
                self.transform_point(Vector3(localFace[0]))
                , self.transform_point(Vector3(localFace[1]))
                , self.transform_point(Vector3(localFace[2])))

            if camera.will_face_be_rendered(worldface):  # jeśli i tak nie będzie widać to pomijamy
                worldfaces.append(worldface)

        for face in worldfaces:
            lightlevel = LightManager.calculate_light(face)
            rendered_color = self.mesh.get_rendered_color(lightlevel)
            points = self.world_fac
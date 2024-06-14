import pygame

from src import Camera
from src.Light.LightManager import LightManager
from src.Math.Transform import Transform
from src.Systems import Drawable
from src.MeshSystem import Mesh
from src.Systems.Updatable import Updatable
from src.MeshSystem.WorldFace import WorldFace


class DrawableMesh(Updatable, Drawable, Transform):

    def __init__(self, pos):
        super().__init__()
        self.SetPosition(pos)
        self.mesh = None

    def assignMesh(self, mesh: Mesh):
        self.mesh = mesh

    def local_face_to_screen(self, face: WorldFace, camera: Camera):
        points = []
        for point in face.vectors():
            world_pos = self.TransformPoint(point)
            points.append(camera.world_pos_to_screen(world_pos))
        return points

    def Draw(self, screen, camera: Camera):
        worldFaces: [WorldFace] = []
        for localFace in self.mesh.get_faces():
            worldface = WorldFace(
                self.TransformPoint(localFace.v1), self.TransformPoint(localFace.v2), self.TransformPoint(localFace.v3))
            if camera.will_face_be_rendered(worldface):  # jeśli i tak nie będzie widać to pomijamy
                worldFaces.append(worldface)

        for face in worldFaces:
            lightlevel = LightManager.calculate_light(face)
            rendered_color = self.mesh.get_rendered_color(lightlevel)
            points = self.local_face_to_screen(face, camera)
            pygame.draw.polygon(screen, rendered_color, points)
        pass

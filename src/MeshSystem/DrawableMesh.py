import random

from pygame import Vector3
from src import Camera
from src.Light.LightManager import LightManager
from src.Math.Transform import Transform
from src.Math.VectorMath import VectorMath
from src.MeshSystem.MeshRenderer import MeshRenderer
from src.MeshSystem.QueuedFace import QueuedFace
from src.ModelPool import ModelPool
from src.Systems.Drawable import Drawable
from src.MeshSystem import Mesh
from src.Systems.Updatable import Updatable
from src.MeshSystem.WorldFace import WorldFace


class DrawableMesh(Updatable, Drawable, Transform):

    def __init__(self, pos,rot = 0,mesh = None):
        super().__init__()
        ModelPool.register_model(self)
        self.set_position(pos)
        self.mesh = mesh

    def assign_mesh(self, mesh: Mesh):
        self.mesh = mesh

    @staticmethod
    def world_face_to_screen(face: WorldFace, camera: Camera):
        """
        Projects a face onto the screen of the camera
        @param face: face as three vertices in world position
        @param camera: camera that renders given face
        @return: points on screen that represents given face
        """
        points = []
        for point in face.vectors():
            points.append(camera.world_pos_to_screen(point))
        return points

    def _draw(self, screen, camera: Camera):
        worldfaces: [WorldFace] = []
        for localFace in self.mesh.get_faces():
            worldface = WorldFace(
                self.transform_point(Vector3(localFace[0]))
                , self.transform_point(Vector3(localFace[1]))
                , self.transform_point(Vector3(localFace[2])))

            if camera.will_face_be_rendered(worldface):
                worldfaces.append(worldface)

        for face in worldfaces:
            lightlevel = LightManager.calculate_light(face)
            rendered_color = self.mesh.get_rendered_color(lightlevel)
            points = self.world_face_to_screen(face, camera)
            to_queue = QueuedFace(points, rendered_color, VectorMath.face_middle(face).z)
            MeshRenderer.enqueue_face(to_queue)
        pass

    def __str__(self):
        return "Model" + str(random.randint(0, 10))


    def kill(self, unregister = True):
        if(unregister):
            ModelPool.unregister_model(self)
        super().kill()


    def __repr__(self):
        return (f"{self.__class__.__name__}(Vector3({self.get_local_position()})"
                f",{self.get_local_rotation()},{self.mesh.__repr__()})")
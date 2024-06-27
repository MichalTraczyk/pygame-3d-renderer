from pygame import Vector3, Vector2
import math

from src.Math.VectorMath import VectorMath
from src.MeshSystem.WorldFace import WorldFace

main_camera = None
class Camera:

    def __init__(self, fov: float, screen_x, screen_y, near_clip: float = 0.1):
        self.fov = fov
        self.screen_y = screen_y
        self.screen_x = screen_x
        self.near_clip = near_clip
        if main_camera is None:
            Camera.main_camera = self
    def world_pos_to_screen(self, vertex_pos: Vector3):
        """
        Projects single vertex onto the screen
        @param vertex_pos: Position of vertex as Vector3 in world space
        @rtype Vector2
        @return: 2D position of given vertex in screen space
        """
        pos = vertex_pos.copy()
        if pos.z == 0:
            pos.z = self.near_clip

        near_plane_x = self.near_clip * math.tan(math.radians(self.fov))
        near_plane_y = self.near_clip * math.tan(math.radians(self.fov)) * self.screen_y / self.screen_x

        dx = pos.x / pos.z * self.near_clip
        dy = pos.y / pos.z * self.near_clip

        dx /= near_plane_x
        dy /= near_plane_y

        screen_x = (1 + dx) * self.screen_x / 2
        screen_y = (1 - dy) * self.screen_y / 2
        return Vector2(screen_x, screen_y)

    def is_vertex_in_frustum(self, pos: Vector3):
        """
        @param pos: Position of vertex in world space
        @return: True if given vertex is in frustum of the camera
        """
        if pos.z < self.near_clip:
            return False

        screen_pos = self.world_pos_to_screen(pos)
        if screen_pos.x < 0 or screen_pos.x >= self.screen_x:
            return False
        return 0 <= screen_pos.y < self.screen_y

    def is_face_in_frustum(self, face: WorldFace):
        """
        @param face: Face in world space to be rendered
        @return: True if given face is in frustum of the camera
        """
        for vertex in face.vectors():  # checking near plane
            if vertex.z < self.near_clip:
                return False
        for vertex in face.vectors():  # checking if at leas one is in frustum
            if self.is_vertex_in_frustum(vertex):
                return True
        #  possible face passing if the center can be rendered
        return self.is_vertex_in_frustum(VectorMath.face_middle(face))

    def will_face_be_rendered(self, face: WorldFace):
        """
        Calculates if given WorldFace can and will be rendered
        @param face: Face in world space to be rendered
        @return: True if given face will be rendered
        """
        if not self.is_face_in_frustum(face):
            return False
        normal = VectorMath.face_normal(face)
        cameranormal = VectorMath.normalize_vector(VectorMath.face_middle(face))
        dot = VectorMath.dot(normal, cameranormal)
        return dot < 0

    def set_fov(self, fov: float):
        self.fov = fov
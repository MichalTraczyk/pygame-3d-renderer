from pygame import Vector3, Vector2
import math

from src.Math.VectorMath import VectorMath
from src.MeshSystem.WorldFace import WorldFace


class Camera:

    def __init__(self, fov: float, screen_x, screen_y, near_clip: float = 0.1):
        self.fov = fov
        self.screen_y = screen_y
        self.screen_x = screen_x
        self.near_clip = near_clip

    def world_pos_to_screen(self, vertex_pos: Vector3):
        pos = vertex_pos.copy()
        if pos.z == 0:
            pos.z = self.near_clip

        near_pane_x = self.near_clip * math.tan(math.radians(self.fov))
        near_pane_y = self.near_clip * math.tan(math.radians(self.fov)) * self.screen_y / self.screen_x

        dx = pos.x / pos.z * self.near_clip
        dy = pos.y / pos.z * self.near_clip

        dx /= near_pane_x
        dy /= near_pane_y

        screen_x = (1 + dx) * self.screen_x / 2
        screen_y = (1 - dy) * self.screen_y / 2
        return Vector2(screen_x, screen_y)

    def is_vertex_in_frustrum(self, pos: Vector3):

        if pos.z < self.near_clip:
            return False

        screen_pos = self.world_pos_to_screen(pos)
        if screen_pos.x < 0 or screen_pos.x >= self.screen_x:
            return False
        return 0 <= screen_pos.y < self.screen_y

    def is_face_in_frustrum(self, face: WorldFace):
        for vertex in face.vectors():
            if self.is_vertex_in_frustrum(vertex):
                return True
        return self.is_vertex_in_frustrum(VectorMath.face_middle(face))

    def will_face_be_rendered(self, face: WorldFace):
        if not self.is_face_in_frustrum(face):
            return False
        normal = VectorMath.face_normal(face)
        cameranormal = VectorMath.normalize_vector(VectorMath.face_middle(face))
        dot = VectorMath.Dot(normal, cameranormal)
        return dot <= 0

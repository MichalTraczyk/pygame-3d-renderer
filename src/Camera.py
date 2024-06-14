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

        dx = Vector2(pos.x, pos.z) / pos.z
        dy = Vector2(pos.y, pos.z) / pos.z

        dx /= near_pane_x
        dy /= near_pane_y

        screen_x = (1 + dx.x) * self.screen_x / 2
        screen_y = (1 - dy.x) * self.screen_y / 2
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
        return False

    def will_face_be_rendered(self, face: WorldFace):
        if not self.is_face_in_frustrum(face):
            return False
        normal = VectorMath.face_normal(face)
        cameraNormal = Vector3(0, 0, 1)
        dot = VectorMath.Dot(normal, cameraNormal)
        return dot <= 0

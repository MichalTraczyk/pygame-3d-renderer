import pygame
from src.MeshSystem.QueuedFace import QueuedFace


class MeshRenderer:
    faces: [QueuedFace] = []

    @classmethod
    def enqueue_face(cls, face: QueuedFace):
        cls.faces.append(face)

    @classmethod
    def draw_buffor(cls, screen):
        cls.faces = sorted(cls.faces, key=lambda f: f.depth, reverse=True)
        for face in cls.faces:
            pygame.draw.polygon(screen, face.color, face.points)
        cls.faces.clear()

import os

from src.KeyboardMove import KeyboardMove
from src.Light.LightManager import LightManager
from src.Light.LightSource import LightSource
from src.Light.LightSourcesTypes import *
from src.MeshSystem.DrawableMesh import DrawableMesh
from src.MeshSystem.Mesh import Mesh
from src.ModelPool import ModelPool


class SaveSystem:
    __filename = "save"
    @staticmethod
    def save_to_file():
        f = open(SaveSystem.__filename, "w")
        for m in ModelPool.get_pool():
            f.write(m.__repr__() + "\n")
        for l in LightManager.lights:
            f.write(l.__repr__() + "\n")

    @staticmethod
    def load_from_file():

        if not os.path.exists(SaveSystem.__filename):
            return
        ModelPool.kill_all()
        LightManager.kill_all()
        KeyboardMove.parent.set_local_position(Vector3(0,0,0))
        KeyboardMove.parent.set_local_rotation(0)
        KeyboardMove.parent.clear_children()
        f = open(SaveSystem.__filename, "r")
        for line in f:
            x = eval(line)
            if "light" in line.lower():
                print(line)
                LightManager.register_light(x)
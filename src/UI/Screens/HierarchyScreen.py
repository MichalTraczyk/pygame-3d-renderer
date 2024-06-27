from pygame import Vector2
import tkinter as tk
from tkinter import filedialog

from src.Light.LightManager import LightManager
from src.MeshSystem.DrawableMesh import DrawableMesh
from src.MeshSystem.Mesh import Mesh
from src.MeshSystem.Primitives import Primitives
from src.Reader.OBJFileReader import OBJFileReader
from src.Light.LightSourcesTypes import *
from src.Systems.Drawable import Drawable
from src.Systems.Updatable import Updatable
from src.UI.UIElements.Button import Button
from src.UI.UIElements.ExpandableList import ExpandableList
from src.UI.UIElements.PerformanceLabel import PerformanceLabel
from src.UI.UIElements.Label import Label


class HierarchyScreen(Updatable, Drawable):
    def __init__(self, size: Vector2, position: Vector2):
        super().__init__()
        elementWidth = size.x - 20
        elementHeight = 20
        self.position = position
        padding = 20
        self.element_size = (elementWidth, elementHeight)
        import_button = Button((elementWidth, elementHeight),
                               (self.position.x + padding, self.position.y + 40), "Import")

        import_button.add_listener(self.on_import_clicked)

        Button((elementWidth / 4, elementHeight), (self.position.x + padding, self.position.y + 760), "Box") \
            .add_listener(lambda: DrawableMesh(Vector3(0, 0, 2)).assign_mesh(Primitives.generate_box()))
        Button((elementWidth / 4, elementHeight), (self.position.x + 80, self.position.y + 760), "Pyramid") \
            .add_listener(lambda: DrawableMesh(Vector3(0, 0, 2)).assign_mesh(Primitives.generate_rotated_pyramid()))
        Button((elementWidth / 3, elementHeight), (self.position.x + 140, self.position.y + 760), "Plane10x10") \
            .add_listener(lambda: DrawableMesh(Vector3(0, -1, 0)).assign_mesh(Primitives.generate_plane(10, 0.5)))
        Button((elementWidth / 3, elementHeight), (self.position.x + 220, self.position.y + 760), "Plane20x20") \
            .add_listener(lambda: DrawableMesh(Vector3(0, -1, 0)).assign_mesh(Primitives.generate_plane(20, 0.5)))

        Button((elementWidth / 3, elementHeight), (self.position.x + padding, self.position.y + 730), "Point") \
            .add_listener(lambda: LightManager.register_light(PointLight(Vector3(0, 0, 2), 0.5, Color(255, 255, 255))))
        Button((elementWidth / 3, elementHeight), (self.position.x + padding+100, self.position.y + 730), "Directional") \
            .add_listener(lambda: LightManager.register_light(DirectionalLight(Vector3(0, 0, 2),Vector3(0, -1, 0), 0.5, Color(255, 255, 255))))
        Button((elementWidth / 3, elementHeight), (self.position.x + padding+200, self.position.y + 730), "Skybox") \
            .add_listener(lambda: LightManager.register_light(SkyboxLight(Vector3(0, 0, 2), 0.1, Color(255, 255, 255))))


        delete_button = Button((elementWidth, elementHeight),
                        (self.position.x + padding, self.position.y + 65),"Delete")

        delete_button.add_listener(self.on_delete_clicked)

        models_label = Label((elementWidth, elementHeight), (padding, self.position.y + 100),
                             "Models")

        fps_counter = PerformanceLabel((elementWidth, elementHeight), (padding, self.position.y + padding / 2))

        self.modelsList = ExpandableList((elementWidth, 300),
                                         (self.position.x + padding, self.position.y + 120))

        self.modelsList.add_select_listener(self.select_element)
        self.modelsList.add_select_listener(self.select_element)

        lights_label = Label((elementWidth, elementHeight), (padding, self.position.y + 300),
                             "Lights")
        self.lightsList = ExpandableList((elementWidth, 300),
                                         (self.position.x + padding, self.position.y + 330))
        self.lightsList.add_select_listener(self.select_element)

        self.selected_element = None
        self.selected_object = None
        self.selected_object_changed_listeners = []

    def lights_changed(self, lights):
        self.lightsList.clear()

        for l in lights:
            e = ExpandableList.get_default_element(self.element_size, l.__str__())
            e.target = l
            self.lightsList.add_element(e)

    def models_changed(self, models):
        self.modelsList.clear()

        for m in models:
            e = ExpandableList.get_default_element(self.element_size, m.__str__())
            e.target = m
            self.modelsList.add_element(e)

    def select_element(self, element):
        if self.selected_element is not None:
            self.selected_element.unselect()
        self.selected_element = element
        self.selected_object = self.selected_element.target
        for l in self.selected_object_changed_listeners:
            l(self.selected_object)

    def add_select_changed_listener(self, listener):
        self.selected_object_changed_listeners.append(listener)

    def on_import_clicked(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(
            filetypes=[("OBJ Files", "*.obj")],
            title="Select an OBJ File")

        if file_path:
            try:
                vertices, faces = OBJFileReader.read_file(file_path)
                mesh = Mesh(vertices, faces)
                obj = DrawableMesh(Vector3(1, 2, 3.6))
                obj.assign_mesh(mesh)
                print(f"Successfully imported {file_path}")
            except Exception as e:
                print(f"Error importing file: {e}")

    def on_delete_clicked(self):
        if self.selected_element is None:
            return
        obj_to_remove = self.selected_element.target
        if isinstance(obj_to_remove, LightSource):
            LightManager.unregister_light(obj_to_remove)
        else:
            obj_to_remove.kill()
        self.selected_element = None
        for listener in self.selected_object_changed_listeners:
            listener(None)

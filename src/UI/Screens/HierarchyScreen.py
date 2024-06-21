from pygame import Vector2

from src.Systems.Drawable import Drawable
from src.Systems.Updatable import Updatable
from src.UI.UIElements.Button import Button
from src.UI.UIElements.ExpandableList import ExpandableList
from src.UI.UIElements.ExpandableListElement import ExpandableListElement
from src.UI.UIElements.Label import Label


class HierarchyScreen(Updatable, Drawable):
    def __init__(self, size: Vector2, position: Vector2):
        super().__init__()
        elementWidth = size.x - 20
        elementHeight = 20
        self.position = position
        padding = 20
        element_size = (elementWidth, elementHeight)
        import_button = Button((elementWidth, elementHeight),
                             (self.position.x + padding, self.position.y + padding), "Import")

        import_button.add_listener(self.on_import_clicked)

        models_label = Label((elementWidth, elementHeight), (padding, self.position.y + 100),
                                  "Models")

        self.modelsList = ExpandableList((elementWidth, 300),
                                         (self.position.x + padding, self.position.y + 120))

        self.modelsList.add_select_listener(self.select_element)
        el = ExpandableList.get_default_element(element_size, "Model1")
        el1 = ExpandableList.get_default_element(element_size, "Model2")
        el2 = ExpandableList.get_default_element(element_size, "Model3")
        self.modelsList.add_element(el)
        self.modelsList.add_element(el1)
        self.modelsList.add_element(el2)

        lights_label = Label((elementWidth, elementHeight), (padding, self.position.y + 300),
                                  "Lights")
        self.lightsList = ExpandableList((elementWidth, 300),
                                         (self.position.x + padding, self.position.y + 330))
        self.lightsList.add_select_listener(self.select_element)
        ell = ExpandableList.get_default_element(element_size, "Directional Light")
        ell1 = ExpandableList.get_default_element(element_size, "Point Light")
        ell2 = ExpandableList.get_default_element(element_size, "Skybox Light")
        self.lightsList.add_element(ell)
        self.lightsList.add_element(ell1)
        self.lightsList.add_element(ell2)

        self.selected_element = None
        self.selected_object = None

    def select_element(self, element):
        print(element)
        if self.selected_element is not None:
            self.selected_element.unselect()
        self.selected_element = element
        self.selected_object = self.selected_element.target
    def on_import_clicked(self):
        print("import")
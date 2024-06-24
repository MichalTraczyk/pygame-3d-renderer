from pygame import Vector2

from src.UI.UIElements.ExpandableListElement import ExpandableListElement
from src.UI.UIElements.UIElement import UIElement


class ExpandableList(UIElement):
    def __init__(self, size, position):
        super().__init__(size, position)
        self.elements = []
        self.indent = 10
        self.listeners = []

    def clear(self):
        """
        Clears the list
        """
        for e in self.elements:
            e.kill()
        self.elements = []

    def add_element(self, element):
        """
        Adds an element to the list
        @param element: Element to add
        @type element: ExpandableListElement
        """
        self.elements.append(element)
        self.__update_positions()
        for listener in self.listeners:
            element.add_listener(listener)

    def remove_element(self, element):
        """
        Removes element from the list
        @param element: Element to remove
        @type element: ExpandableListElement
        """
        self.elements.remove(element)
        self.__update_positions()
        for listener in self.listeners:
            element.remove_listener(listener)

    def __update_positions(self):
        curr_pos = Vector2(self.position[0] + self.indent, self.position[1] + 5)
        for element in self.elements:
            element.set_position((curr_pos.x, curr_pos.y))
            curr_pos.y += element.size[1] + self.indent

    def set_position(self, position):
        super().set_position(position)
        self.__update_positions()

    def add_select_listener(self, listener):
        """
        Adds a listener to call when list element is selected
        @param listener: Method to call
        """
        self.listeners.append(listener)
        for element in self.elements:
            element.add_listener(listener)

    @staticmethod
    def get_default_element(size, text):
        """
        Returns a default element with given size and text
        @param size: Size of the element
        @param text: Text of the element
        @rtype: ExpandableListElement
        """
        return ExpandableListElement(size, (0, 0), text)

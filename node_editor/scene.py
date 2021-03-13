from collections import OrderedDict
from node_editor.serializable import Serializable
from node_editor.elements.node import Node
from node_editor.elements.edge import Edge
from node_editor.graphics.graphics_scene import GraphicsScene
from node_editor.scene_history import SceneHistory
from node_editor.clipboard import SceneClipboard
from node_editor.utils import dumpException
import os
import json

class InvalidFile(Exception): pass


class Scene(Serializable):
    def __init__(self):
        super().__init__()
        self.nodes = []
        self.edges = []
        self._last_selected_items = []

        self._selected_listeners = []
        self._deselected_listeners = []

        self.node_class_selector = None

        self.initUI()
        self.history = SceneHistory(self)
        self.clipboard = SceneClipboard(self)

        self.grScene.itemSelected.connect(self.onItemSelected)
        self.grScene.itemsDeselected.connect(self.onItemsDeselected)

    def initUI(self):
        self.grScene = GraphicsScene(self)
        self.grScene.setGrScene(32000, 32000)

    def onItemSelected(self):
        current_selected_items = self.getSelectedItems()
        if current_selected_items != self._last_selected_items:
            self._last_selected_items = current_selected_items
            self.history.storeHistory("Selection Changed")
            for callback in self._selected_listeners: callback()

    def onItemsDeselected(self):
        self.resetLastSelectedStates()
        if self._last_selected_items != []:
            self._last_selected_items = []
            self.history.storeHistory("Deselected Everything")
            for callback in self._deselected_listeners: callback()

    def getSelectedItems(self):
        return self.grScene.selectedItems()

    # listeners

    def addItemSelectedListener(self, callback):
        self._selected_listeners.append(callback)

    def addItemsDeselectedListener(self, callback):
        self._deselected_listeners.append(callback)

    def addDragEnterListener(self, callback):
        self.grScene.views()[0].addDragEnterListener(callback)

    def addDropListener(self, callback):
        self.grScene.views()[0].addDropListener(callback)

    # custom flag to detect node or edge has been selected....
    def resetLastSelectedStates(self):
        for node in self.nodes:
            node.grNode._last_selected_state = False
        for edge in self.edges:
            edge.grEdge._last_selected_state = False

    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, edge):
        self.edges.append(edge)


    def removeNode(self, node):
        if node in self.nodes: self.nodes.remove(node)

    def removeEdge(self, edge):
        if edge in self.edges: self.edges.remove(edge)


    def clear(self):
        while len(self.nodes) > 0:
            self.nodes[0].remove()


    def saveToFile(self, filename):
        with open(filename, "w") as file:
            file.write( json.dumps( self.serialize(), indent=4 ) )
            print("saving to", filename, "was successfull.")

    def loadFromFile(self, filename):
        with open(filename, "r") as file:
            raw_data = file.read()
            try:
                data = json.loads(raw_data, encoding='utf-8')
                self.deserialize(data)
            except json.JSONDecodeError:
                raise InvalidFile("%s is not a valid JSON file" % os.path.basename(filename))
            except Exception as e:
                dumpException(e)

    def setNodeClassSelector(self, class_selecting_function):
        """ When the function self.node_class_selector is set, we can use different Node Classes """
        self.node_class_selector = class_selecting_function

    def getNodeClassFromData(self, data):
        return Node if self.node_class_selector is None else self.node_class_selector(data)


    def serialize(self):
        nodes, edges = [], []
        for node in self.nodes: nodes.append(node.serialize())
        for edge in self.edges: edges.append(edge.serialize())
        return OrderedDict([
            ('id', self.id),
            ('scene_width', 32000),
            ('scene_height', 32000),
            ('nodes', nodes),
            ('edges', edges),
        ])

    def deserialize(self, data, hashmap={}, restore_id=True):
        self.clear()
        hashmap = {}

        if restore_id: self.id = data['id']

        # create nodes
        for node_data in data['nodes']:
            self.getNodeClassFromData(node_data)(self).deserialize(node_data, hashmap, restore_id)

        # create edges
        for edge_data in data['edges']:
            Edge(self).deserialize(edge_data, hashmap, restore_id)


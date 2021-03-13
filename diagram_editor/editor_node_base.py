from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from node_editor.elements.node import Node
from node_editor.graphics.graphics_node import GraphicsNode
from node_editor.content_widget import QDMNodeContentWidget
from node_editor.elements.socket import LEFT_CENTER, RIGHT_CENTER


class DiagramEditorGraphicsNode(GraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 160
        self.height = 74
        self.edge_roundness = 6
        self.edge_padding = 0
        self.title_horizontal_padding = 8
        self.title_vertical_padding = 10

    def initAssets(self):
        super().initAssets()
        self._brush_background = QBrush(QColor("#008A8A"))


# class DiagramContent(QDMNodeContentWidget):
#     def initUI(self):
#         pass
#         # lbl = QLabel(self.node.content_label, self)


class DiagramNode(Node):
    icon = ""
    op_code = 0
    op_title = "Undefined"
    content_label = ""

    def __init__(self, scene, inputs=[2,2], outputs=[1]):
        super().__init__(scene, self.__class__.op_title, inputs, outputs)

    def initInnerClasses(self):
        self.grNode = DiagramEditorGraphicsNode(self)

    def initSettings(self):
        super().initSettings()
        self.input_socket_position = LEFT_CENTER
        self.output_socket_position = RIGHT_CENTER

    def serialize(self):
        res = super().serialize()
        res['op_code'] = self.__class__.op_code
        return res

    # def deserialize(self, data, hashmap={}, restore_id=True):
    #     res = super().deserialize(data, hashmap, restore_id)
    #     return res
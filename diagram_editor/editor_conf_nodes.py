from PyQt5.QtCore import *
from diagram_editor.editor_conf import *
from diagram_editor.editor_node_base import *
from node_editor.utils import dumpException

class InputContent(DiagramEditorGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 90
        self.height = 90
        self.edge_roundness = 3

    def initAssets(self):
        super().initAssets()
        self._brush_background = QBrush(QColor("#650799"))

class OutputContent(DiagramEditorGraphicsNode):
    def initSizes(self):
        super().initSizes()
        self.width = 90
        self.height = 90
        self.edge_roundness = 10

    def initAssets(self):
        super().initAssets()
        self._brush_background = QBrush(QColor("#217A00"))


@register_node(OP_CODE_INPUT_1)
class DiagramNode_Input(DiagramNode):
    icon = "icons/vegetables.png"
    op_code = OP_CODE_INPUT_1
    op_title = "Vegetables"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[3])

    def initInnerClasses(self):
        # self.content = DiagramContent(self)
        self.grNode = InputContent(self)

# class CalcOutputContent(QDMNodeContentWidget):
#     def initUI(self):
#         self.lbl = QLabel("42", self)
#         self.lbl.setAlignment(Qt.AlignLeft)
#         self.lbl.setObjectName(self.node.content_label_objname)


@register_node(OP_CODE_INPUT_2)
class DiagramNode_Add(DiagramNode):
    icon = "icons/fruits.png"
    op_code = OP_CODE_INPUT_2
    op_title = "Fruits"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[3])

    def initInnerClasses(self):
        # self.content = DiagramContent(self)
        self.grNode = InputContent(self)


@register_node(OP_CODE_INPUT_3)
class DiagramNode_Add(DiagramNode):
    icon = "icons/meat.png"
    op_code = OP_CODE_INPUT_3
    op_title = "Meat"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[3])

    def initInnerClasses(self):
        # self.content = DiagramContent(self)
        self.grNode = InputContent(self)


@register_node(OP_CODE_OUTPUT_1)
class DiagramNode_Sub(DiagramNode):
    icon = "icons/packer.png"
    op_code = OP_CODE_OUTPUT_1
    op_title = "Packing"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[])

    def initInnerClasses(self):
        # self.content = DiagramContent(self)
        self.grNode = OutputContent(self)


@register_node(OP_CODE_WASHER)
class DiagramNode_Mul(DiagramNode):
    icon = "icons/washer.png"
    op_code = OP_CODE_WASHER
    op_title = "Washer"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[2])


@register_node(OP_CODE_PEELING)
class DiagramNode_Div(DiagramNode):
    icon = "icons/peeler.png"
    op_code = OP_CODE_PEELING
    op_title = "Skin/Seed Remove"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[2])


@register_node(OP_CODE_INPUT_4)
class DiagramNode_Add(DiagramNode):
    icon = "icons/ingredients.png"
    op_code = OP_CODE_INPUT_4
    op_title = "Ingredients"

    def __init__(self, scene):
        super().__init__(scene, inputs=[], outputs=[3])

    def initInnerClasses(self):
        # self.content = DiagramContent(self)
        self.grNode = InputContent(self)


@register_node(OP_CODE_PASTEURIZER)
class DiagramNode_Div(DiagramNode):
    icon = "icons/pasteurizer.png"
    op_code = OP_CODE_PASTEURIZER
    op_title = "Pasteurizer"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[2])


@register_node(OP_CODE_EVAPORATOR)
class DiagramNode_Div(DiagramNode):
    icon = "icons/evaporator.png"
    op_code = OP_CODE_EVAPORATOR
    op_title = "Evaporator"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[2])


@register_node(OP_CODE_REFINER)
class DiagramNode_Div(DiagramNode):
    icon = "icons/refinery.png"
    op_code = OP_CODE_REFINER
    op_title = "Refiner"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[2])


@register_node(OP_CODE_MIXER)
class DiagramNode_Div(DiagramNode):
    icon = "icons/mixer.png"
    op_code = OP_CODE_MIXER
    op_title = "Mixer"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1, 1], outputs=[2])


@register_node(OP_CODE_HEATER)
class DiagramNode_Div(DiagramNode):
    icon = "icons/heater.png"
    op_code = OP_CODE_HEATER
    op_title = "Heater"

    def __init__(self, scene):
        super().__init__(scene, inputs=[1], outputs=[2])
# class CalcInputContent(QDMNodeContentWidget):
#     def initUI(self):
#         self.edit = QLineEdit("1", self)
#         self.edit.setAlignment(Qt.AlignRight)
#         self.edit.setObjectName(self.node.content_label_objname)
#
#     def serialize(self):
#         res = super().serialize()
#         res['value'] = self.edit.text()
#         return res
#
#     def deserialize(self, data, hashmap={}):
#         res = super().deserialize(data, hashmap)
#         try:
#             value = data['value']
#             self.edit.setText(value)
#             return True & res
#         except Exception as e:
#             dumpException(e)
#         return res

# @register_node(OP_CODE_OUTPUT_2)
# class DiagramNode_Output(DiagramNode):
#     icon = "icons/out.png"
#     op_code = OP_CODE_OUTPUT_2
#     op_title = "Packer"
#     content_label_objname = "calc_node_output"
#
#     def __init__(self, scene):
#         super().__init__(scene, inputs=[1], outputs=[])
#
#     # def initInnerClasses(self):
#     #     self.content = CalcOutputContent(self)
#     #     self.grNode = DiagramEditorGraphicsNode(self)
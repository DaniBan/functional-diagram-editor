import os
import sys
from PyQt5.QtWidgets import *

from diagram_editor.editor_window import DiagramEditorWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyle('Fusion')

    wnd = DiagramEditorWindow()
    wnd.show()

    # wnd2 = QMainWindow()
    # wnd2.show()

    sys.exit(app.exec_())

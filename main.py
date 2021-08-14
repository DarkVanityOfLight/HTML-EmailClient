# This Python file uses the following encoding: utf
import sys, os
from pathlib import Path

from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtQuick import QQuickView, QQuickItem
from PySide2.QtCore import QUrl, QObject

from main_view import MainView


if __name__ == "__main__":
    app = QApplication([])


    view = MainView()

    if len(sys.argv) > 1:
        if sys.argv[1] == "editor":
            view.makeEditor()

    view.show()

    sys.exit(app.exec_())

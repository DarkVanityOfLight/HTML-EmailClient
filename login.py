
import sys, os
from pathlib import Path

from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtQuick import QQuickView, QQuickItem
from PySide6.QtCore import QUrl, QObject




class Login(QQuickView):
    email = ""
    password = ""
    smtp = ""

    def __init__(self):
        super().__init__()

        self.setResizeMode(QQuickView.SizeRootObjectToView)

        login_view_file = Path(__file__).parent / "login.qml"
        self.setSource(QUrl.fromLocalFile(os.fspath(login_view_file.resolve())))


        self.root_win = self.rootObject()
        self.page = self.root_win.childItems()[0]
        self.column = self.page.childItems()[0]

        self.findLoginFields(self.column)
        self.login_button.clicked.connect(self.setCreds)

    def setCreds(self):
        self.email = self.email_field.property("text")
        self.password = self.password_field.property("text")
        self.smtp = self.smtp_field.property("text")


    def findLoginFields(self, parent):
        self.email_field = parent.findChild(QObject, "emailField")
        self.password_field = parent.findChild(QObject, "passwordField")
        self.smtp_field = parent.findChild(QObject, "smtpField")
        self.login_button = parent.findChild(QObject, "loginButton")




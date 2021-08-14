
import sys, os
from pathlib import Path

from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtQuick import QQuickView, QQuickItem
from PySide2.QtCore import QUrl, QObject, Qt

from send_email import *


class MainView(QQuickView):
    email = ""
    password = ""
    smtp = ""

    def __init__(self):
        super().__init__()

        self.setResizeMode(QQuickView.SizeRootObjectToView)

        self.login_view_file = Path(__file__).parent / "login.qml"
        self.editor_view_file = Path(__file__).parent / "editor.qml"

        self.makeLogin()

    def setCreds(self):
        self.email = self.email_field.property("text")
        self.password = self.password_field.property("text")
        self.smtp = self.smtp_field.property("text")

        if self.handle_smtp_login():
            self.makeEditor()

    def handle_smtp_login(self):
        try:
            server = create_server(self.smtp)
        except Exception as e:
            self.handle_server_creation_error(e)
            return False
        try:
            login_to_smtp(server, self.email, self.password)
        except Exception as e:
            self.handle_login_error(e)
            return False

        return True

    def handle_login_error(self, e):
        self.error_text.setProperty("visible", True)
        self.error_text.setProperty("text", "Incorrect username or password!")

    def handle_server_creation_error(self, e):
        self.error_text.setProperty("visible", True)
        self.error_text.setProperty("text", "Incorrect SMTP server!")

    def findLoginFields(self, parent):
        self.email_field = parent.findChild(QObject, "emailField")
        self.password_field = parent.findChild(QObject, "passwordField")
        self.smtp_field = parent.findChild(QObject, "smtpField")
        self.login_button = parent.findChild(QObject, "loginButton")
        self.error_text = parent.findChild(QObject, "errorText")

    def findEditorFields(self, parent):
        self.editor = parent.findChild(QObject, "textEditor")
        self.display = parent.findChild(QObject, "textDisplay")

    def transferText(self):
        to_transfer = self.editor.property("text")
        self.display.loadHtml(to_transfer, "")


    def makeEditor(self):
        self.setSource(QUrl.fromLocalFile(os.fspath(self.editor_view_file.resolve())))

        self.root_item = self.rootObject()
        self.findEditorFields(self.root_item)
        self.editor.textChanged.connect(self.transferText)


    def makeLogin(self):
        self.setSource(QUrl.fromLocalFile(os.fspath(self.login_view_file.resolve())))

        self.column = self.rootObject()

        self.findLoginFields(self.column)
        self.login_button.clicked.connect(self.setCreds)

    def debug_call(self):
        print("Foo")

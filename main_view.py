
import sys, os
from pathlib import Path

from PySide2.QtWidgets import QApplication, QWidget, QPushButton
from PySide2.QtQuick import QQuickView, QQuickItem
from PySide2.QtCore import QUrl, QObject, Qt

from send_email import *

import create_message


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


        self.server = server
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
        self.to_field = parent.findChild(QObject, "toField")
        self.subject_field = parent.findChild(QObject, "subjectField")
        self.send_button = parent.findChild(QObject, "sendButton")
        self.info_text = parent.findChild(QObject, "infoText")

    def transferText(self):
        to_transfer = self.editor.property("text")
        self.display.loadHtml(to_transfer, "")


    def makeEditor(self):
        self.setSource(QUrl.fromLocalFile(os.fspath(self.editor_view_file.resolve())))

        self.root_item = self.rootObject()
        self.findEditorFields(self.root_item)
        self.editor.textChanged.connect(self.transferText)
        self.send_button.clicked.connect(self.prep_email)


    def makeLogin(self):
        self.setSource(QUrl.fromLocalFile(os.fspath(self.login_view_file.resolve())))

        self.column = self.rootObject()

        self.findLoginFields(self.column)
        self.login_button.clicked.connect(self.setCreds)

    def prep_email(self):
        msg = create_message.create_new_message()
        create_message.set_plain_text(msg, "placeholderText")
        create_message.set_html_alt(msg, self.editor.property("text"))
        msg["Subject"] = self.subject_field.property("text")
        msg["To"] = self.to_field.property("text")
        msg["From"] = self.email

        try:
            send_message_to_smtp(self.server, msg)
            self.info_text.setProperty("color", "#2596be")
            self.info_text.setProperty("visible", True)
            self.info_text.setProperty("text", "Email send successfully!")

        except Exception as e:
            self.info_text.setProperty("color", "#dc143c")
            self.info_text.setProperty("visible", True)
            self.info_text.setProperty("text", getattr(e, 'message', repr(e)))


    def debug_call(self):
        print("Foo")

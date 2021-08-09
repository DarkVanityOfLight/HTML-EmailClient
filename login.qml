/****************************************************************************
**
** Copyright (C) 2019 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of the examples of Qt for Python.
**
** $QT_BEGIN_LICENSE:BSD$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** BSD License Usage
** Alternatively, you may use this file under the terms of the BSD license
** as follows:
**
** "Redistribution and use in source and binary forms, with or without
** modification, are permitted provided that the following conditions are
** met:
**   * Redistributions of source code must retain the above copyright
**     notice, this list of conditions and the following disclaimer.
**   * Redistributions in binary form must reproduce the above copyright
**     notice, this list of conditions and the following disclaimer in
**     the documentation and/or other materials provided with the
**     distribution.
**   * Neither the name of The Qt Company Ltd nor the names of its
**     contributors may be used to endorse or promote products derived
**     from this software without specific prior written permission.
**
**
** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
**
** $QT_END_LICENSE$
**
****************************************************************************/

import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.11

ColumnLayout {
    id: columnLayout
    anchors.left: parent.left
    anchors.right: parent.right
    anchors.top: parent.top
    spacing: 5

    Text {
        id: title
        width: 229
        height: 78
        text: qsTr("Login")
        font.pixelSize: 50
        horizontalAlignment: Text.AlignHCenter
        fontSizeMode: Text.Fit
        Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
        minimumPixelSize: 16

    }

    TextField {
        id: emailField
        objectName: "emailField"
        Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
        placeholderText: qsTr("Email")
    }

    TextField {
        id: passwordField
        objectName: "passwordField"
        echoMode: TextInput.Password
        Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
        placeholderText: qsTr("Password")
    }

    TextField {
        id: smtpField
        objectName: "smtpField"
        Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
        placeholderText: qsTr("SMTP Server")
    }

    Text{
        id: errorText
        objectName: "errorText"
        visible: false
        text: qsTr("Foo")
        color: "#dc143c"
        Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
    }

    Button {
        id: loginButton
        objectName: "loginButton"
        text: qsTr("Login")
        Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
    }
}

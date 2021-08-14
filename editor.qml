import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.11
import QtWebEngine 1.10

ColumnLayout{

  Row {
      id: rows
      Layout.fillWidth: true
      height: 50


      TextField {
          id: toField
          placeholderText: qsTr("To")
      }

      TextField {
          id: subjectField
          placeholderText: qsTr("Subject")
      }
  }

  Row{
    id: editorRow
    Layout.fillWidth: true
    Layout.fillHeight: true

    Rectangle {
        id: rectangle
        width: parent.width/2
        height: parent.height
        color: "#00000000"
        border.color: "black"

        TextArea {
            id: textEdit
            objectName: "textEditor"
            anchors.fill: parent
            font.pixelSize: 12
            wrapMode: Text.Wrap
            placeholderTextColor: "#000000"
            placeholderText: "Message here"
            textFormat: Text.PlainText

        }

    }

    Rectangle{
        id: rectangle1
        width: parent.width/2
        height: parent.height
        color: "#00000000"
        border.color: "black"

        WebEngineView {
            id: webView
            property var foo: 42
            objectName: "textDisplay"
            anchors.fill: parent
            url: ""
        }
    }
  }

  Button {
      id: button
      height: 50
      text: qsTr("Send")
      Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
      onClicked: view.debug_call()
  }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/

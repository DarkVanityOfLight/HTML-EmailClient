import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.11
import QtWebEngine 1.10

ColumnLayout{

  Column {
      id: rows
      Layout.fillWidth: true
      spacing: 2


      TextField {
          id: toField
          objectName: "toField"
          placeholderText: qsTr("To")
          width: parent.width
          selectByMouse: true
      }

      TextField {
          id: subjectField
          objectName: "subjectField"
          placeholderText: qsTr("Subject")
          width: parent.width
          selectByMouse: true
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
            selectByMouse: true

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
      id: sendButton
      objectName: "sendButton"
      height: 50
      text: qsTr("Send")
      Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
  }

}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/

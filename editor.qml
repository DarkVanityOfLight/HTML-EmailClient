import QtQuick 2.12

Item{
    TextEdit {
        id: textEdit
        objectName: "textEditor"
        x: 8
        y: 8
        width: 315
        height: 464
        text: ""
        font.pixelSize: 12
        wrapMode: Text.Wrap
        textFormat: Text.PlainText
    }

    Text {
        id: text1
        objectName: "textDisplay"
        x: 329
        y: 8
        width: 315
        height: 464
        text: qsTr("")
        font.pixelSize: 12
        textFormat: Text.RichText
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/

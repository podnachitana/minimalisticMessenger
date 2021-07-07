from datetime import datetime

import requests
from PyQt5 import QtWidgets, QtCore
import client_ui


class ExampleApp(QtWidgets.QMainWindow, client_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #to run on button click:
        self.pushButton.pressed.connect(self.send_message)

        #to run by timer:
        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_message)
        self.timer.start(1000)

    def send_message(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()
        try:
            r = requests.post(
                'http://127.0.0.1:5000/send',
                json={'text': text, 'name': name}
            )
        except:
            self.textBrowser.append('Сервер не доступен')
            self.textBrowser.append('')
            return

        if r.status_code !=200:
            self.textBrowser.append('Неправильные имя или текст')
            self.textBrowser.append('')
            return

        self.textEdit.clear()

    def show_messages(self, messages):
        for message in messages:
            dt = datetime.fromtimestamp(message['time']).strftime('%H:%M:%S')
            self.textBrowser.append(dt + ' ' + message['name'])
            self.textBrowser.append(message['text'])
            self.textBrowser.append('')

    def get_message(self):
        try:
            r = requests.get(
                'http://127.0.0.1:5000/messages',
                params={'after': self.after}
            )
        except:
            return

        if r.status_code != 200:
            return

        messages = r.json()['messages']
        if messages:
            self.show_messages(messages)
            self.after = messages[-1]['time']


app = QtWidgets.QApplication([])
window = ExampleApp()
window.show()
app.exec()

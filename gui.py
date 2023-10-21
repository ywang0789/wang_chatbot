import sys
import os
import api_keys as keys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
    QLineEdit,
    QLabel,
    QInputDialog,
)

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer

import bot as b


class ChatbotGUI(QWidget):
    def __init__(self, API_KEY):
        super().__init__()
        self.API_KEY = API_KEY
        self.bot = b.bot(self.API_KEY)
        self.initUI()

    def initUI(self):
        # Create the main layout
        layout = QVBoxLayout()

        # Text Edit for conversation
        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)
        layout.addWidget(self.textEdit)

        # Line Edit for user input
        self.inputLineEdit = QLineEdit(self)
        layout.addWidget(self.inputLineEdit)

        # Send Button
        self.sendBtn = QPushButton("Send", self)
        self.sendBtn.setShortcut("Return")
        self.sendBtn.clicked.connect(self.sendMessage)
        layout.addWidget(self.sendBtn)

        # Set the main layout
        self.setLayout(layout)

        self.setWindowTitle("Chatbot GUI")
        self.setGeometry(100, 100, 400, 300)
        self.show()

    def sendMessage(self):
        # Get the user message
        message = self.inputLineEdit.text().strip()
        # Clear the input field
        self.inputLineEdit.clear()

        # print the user message
        self.textEdit.append(f"You: {message}")

        # You can replace this with your chatbot's response
        response = f"Chatbot:{self.bot.chat(message)}"
        self.textEdit.append(response)

        # Play the response
        def playAudio(file_name):
            path = os.path.join(os.getcwd(), file_name)
            url = QUrl.fromLocalFile(path)
            content = QMediaContent(url)

            self.player.setMedia(content)
            self.player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    run = ChatbotGUI(keys.gpt_api_key)
    sys.exit(app.exec_())

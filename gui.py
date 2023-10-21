import sys
import os
import api_keys as keys
import tts as tts
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
    def __init__(self):
        super().__init__()
        self.bot = b.bot(keys.gpt_api_key)
        self.player = QMediaPlayer()
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
        user_input = self.inputLineEdit.text().strip()
        
        # Clear the input field
        self.inputLineEdit.clear()

        # print the user message
        self.textEdit.append(f"You: {user_input}")

        # reply to the user message
        reply = self.bot.chat(user_input)
        self.textEdit.append(f"Chatbot:{reply}")
        
        # play audio
        tts.createAudio(reply)
        self.playAudio()


    # Play the response
    def playAudio(self):
        # get path to audio file
        path = os.path.join(os.getcwd(), "voice.mp3")
        url = QUrl.fromLocalFile(path)
        content = QMediaContent(url)
        
        # play the audio
        self.player.setMedia(content)
        self.player.play()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = ChatbotGUI()
    myApp.show()
    sys.exit(app.exec_())

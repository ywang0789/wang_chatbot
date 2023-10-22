import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

# threads
import threading
import time

# my api keys :)
import api_keys as keys

# gpt 
import bot


# class for app
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        # load ui file
        loadUi("gui.ui", self)
        
        # initiate bot
        self.bot = bot.bot(keys.gpt_api_key)

        # button clicked events
        self.home_button.clicked.connect(self.showHome)
        self.chat_button.clicked.connect(self.showChat)
        self.settings_button.clicked.connect(self.showSettings)
        self.chat_send_button.clicked.connect(self.sendMessage)


    # functions for home button
    def showHome(self):
        self.stackedWidget.setCurrentIndex(0)

    # functions for chat button
    def showChat(self):
        self.stackedWidget.setCurrentIndex(1)
    
    # functions for settings button
    def showSettings(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def sendMessage(self):
        # Get the user message
        user_input = self.chat_input_lineedit.text().strip()
        
        # Clear the input field
        self.chat_input_lineedit.clear()
        
        # print the user message
        self.chat_output_textedit.append(f"You: {user_input}")

        QApplication.processEvents() # update the gui (or else it will 'freeze')

        # reply to the user message
        reply = self.bot.chat(user_input)

        self.chat_output_textedit.append(f"Chatbot: {reply}")
        
        # play audio
        # self.player.stop()
        # path = tts.createAudio(reply)
        # self.playAudio(path)

    # Play the response
    # def playAudio(self,path):
    #     url = QUrl.fromLocalFile(path)
    #     content = QMediaContent(url)
        
    #     # play the audio
    #     self.player.setMedia(content)
    #     self.player.play()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UI()
    ui.show()

    
    app.exec_()

    
    



# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()

# clicked events


        # def showHome(self):
        #         self.stackedWidget.setCurrentIndex(0)

        # def showChat(self):
        #         self.stackedWidget.setCurrentIndex(1)






#     sys.exit(app.exec_())

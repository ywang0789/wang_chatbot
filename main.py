import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi

import api_keys as keys

import bot





# class for app
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        loadUi("gui.ui", self)

        self.home_button.clicked.connect(self.showHome)
        self.chat_button.clicked.connect(self.showChat)
        self.settings_button.clicked.connect(self.showSettings)

    # functions for home button
    def showHome(self):
        self.stackedWidget.setCurrentIndex(0)

    # functions for chat button
    def showChat(self):
        self.stackedWidget.setCurrentIndex(1)
    
    # functions for settings button
    def showSettings(self):
        self.stackedWidget.setCurrentIndex(2)
    

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

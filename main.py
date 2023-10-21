from gui import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = ChatbotGUI()
    myApp.show()
    sys.exit(app.exec_())
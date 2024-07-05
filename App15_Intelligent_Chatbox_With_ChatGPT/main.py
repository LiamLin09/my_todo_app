import sys

from PyQt6 import *
from PyQt6.QtWidgets import *


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        # add chat area widget
        self.chat_area = QTextEdit(self)

        # add the input field widget
        self.input_area = QLineEdit(self)

        # add the button
        self.button = QPushButton('SEND', self)

        self.show()


class Chatbot:
    pass


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
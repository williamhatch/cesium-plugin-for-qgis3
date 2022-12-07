import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('local html')
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()

        self.browser.setHtml('''<!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <title>Title</title>
                                </head>
                                <body>
                                <h1>Hello PyQt5</h1>
                                <h1>Hello PyQt5</h1>
                                <h1>Hello PyQt5</h1>
                                <h1>Hello PyQt5</h1>
                                <h1>Hello PyQt5</h1>

                                </body>
                                </html>''')
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exit(app.exec_())

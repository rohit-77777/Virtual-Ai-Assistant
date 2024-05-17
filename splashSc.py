import sys
import time
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QLabel, QFrame, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer, center

class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Jarvis AI')
        self.setFixedSize(1100, 500)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.counter = 0
        self.n = 300 # total instance

        self.initUI()

        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.frame = QFrame()
        layout.addWidget(self.frame)

        # self.labelTitle = QLabel(self.frame)
        # self.labelTitle.setObjectName('LabelTitle')

        self.labelDescription = QLabel(self.frame)
        
        self.movies = QtGui.QMovie("newloading.gif")
        self.labelDescription.setMovie(self.movies)
        self.movies.start()

        
        # self.labelDescription.resize(1500,1500)
        # self.labelDescription.move(0, self.labelTitle.height())
        self.labelDescription.setObjectName('LabelDesc')

        # self.labelDescription.resize(2000, 400)
        self.labelDescription.move(350,50)
        # self.labelDescription.setText('<strong>Working on Voice Recognition</strong>')
        # self.labelDescription.setAlignment(Qt.AlignCenter)


        # # center labels
        # self.labelTitle.resize(self.width() - 10, 150)
        # self.labelTitle.move(0, 40) # x, y
        # self.labelTitle.setText('Jarvis AI')
        # self.labelTitle.setAlignment(Qt.AlignCenter)


        # self.progressBar = QProgressBar(self.frame)
        # self.progressBar.resize(self.width() - 200 - 10, 50)
        # self.progressBar.move(100, self.labelDescription.y() + 130)
        # self.progressBar.setAlignment(Qt.AlignCenter)
        # self.progressBar.setFormat('%p%')
        # self.progressBar.setTextVisible(True)
        # self.progressBar.setRange(0, self.n)
        # self.progressBar.setValue(20)

        # self.labelLoading = QLabel(self.frame)
        # self.labelLoading.resize(self.width() - 10, 50)
        # self.labelLoading.move(0, self.progressBar.y() + 70)
        # self.labelLoading.setObjectName('LabelLoading')
        # self.labelLoading.setAlignment(Qt.AlignCenter)
        # self.labelLoading.setText('Loading...')

    def loading(self):
        # self.progressBar.setValue(self.counter)

        if self.counter == int(self.n * 0.3):
            pass
            # self.labelDescription.setText('<strong> Checking for errors</strong>')
        elif self.counter == int(self.n * 0.6):
            pass
            # self.labelDescription.setText('<strong>Initializing Jarvis AI</strong>')
        elif self.counter >= self.n:
            self.timer.stop()
            self.close()

            time.sleep(1)
            from gui import Gui_Start
            self.myApp = Gui_Start()
            self.myApp.show()

        self.counter += 1



if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    app = QApplication(sys.argv)    
    splash = SplashScreen()
    splash.show()


    sys.exit(app.exec_())


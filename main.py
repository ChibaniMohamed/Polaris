
import sys,time
from splash import *
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMainWindow,QApplication,QGraphicsDropShadowEffect
counter = 0
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        from gui import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_ = Ui_self()
        self.ui_.setupUi_(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        self.show()
        self.center()
    def center(self):
        geo_frame = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        geo_frame.moveCenter(cp)
        self.move(geo_frame.topLeft())
    def progress(self):

        global counter
        if counter > 200:

            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()
        counter += 1
if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())

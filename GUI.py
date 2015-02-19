from PySide import QtGui
from MainWindow import MainWindow


class GUI(object):
    def __init__(self, args):
        self.qApplication = QtGui.QApplication(args)
        self.mainWindow = MainWindow()

    def run(self):
        return self.qApplication.exec_()
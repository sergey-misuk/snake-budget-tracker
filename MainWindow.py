from PySide import QtGui


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(300, 300)
        self.center()
        self.show()

    def center(self):
        geometry = self.frameGeometry()
        screen_center = QtGui.QDesktopWidget().availableGeometry().center()
        geometry.moveCenter(screen_center)
        self.move(geometry.topLeft())
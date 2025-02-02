from PyQt5 import uic, QtWidgets, QtCore



class TableWindow(QtWidgets.QMainWindow):
    """
    основное окно
    """
    def __init__(self):
        super().__init__()
        uic.loadUi('TableWindow.ui', self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = TableWindow()
    window.show()

    app.exec_()

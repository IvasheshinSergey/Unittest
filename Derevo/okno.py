from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QPixmap

class Okno(QtWidgets.QMainWindow):
    _presenter = None
    saveID = -1
    def __init__(self, presenter):
        super(Okno, self).__init__()
        uic.loadUi('ui\\file1.ui', self)
        self._presenter = presenter
        self.pushButton.clicked.connect(self.InsertTrack)
        self.pushButton_2.clicked.connect(self.Close)
    def Show(self, ID):
        self.saveID = ID
        self.lineEdit_3.setText(str(ID))
        self.show()
    def InsertTrack(self):
        ID_Game = self.lineEdit_3.text()
        Title =self.lineEdit.text()
        LenTrack = self.lineEdit_2.text()
        Songs = self.lineEdit_4.text()
        self._presenter.updateTrack(ID_Game, Title, LenTrack, Songs)
    def Close(self):
        self.close()


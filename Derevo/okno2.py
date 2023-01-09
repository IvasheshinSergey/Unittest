from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap

class Okno(QtWidgets.QMainWindow):
    _presenter = None
    saveID = -1
    frame=""
    frame2=""
    def __init__(self, presenter):
        super(Okno, self).__init__()
        uic.loadUi('ui\\file2.ui', self)
        self._presenter = presenter
        self.pushButton.clicked.connect(self.InsertTrack)
        self.pushButton_2.clicked.connect(self.Close)
        self.pushButton_3.clicked.connect(self.showDialog)
        self.pushButton_4.clicked.connect(self.showDialog2)
    def showDialog(self):
        self.frame = QFileDialog.getOpenFileName(self, 'Get Image', '', "JPEG (*.jpg *.jpeg)")[0]

    def showDialog2(self):
        self.frame2 = QFileDialog.getOpenFileName(self, 'Get Mp4', '', "MP4 (*.mp4 *.vid)")[0]

    def Show2(self):
        self.show()
        id=self._presenter.GetLastID()
        self.lineEdit_3.setText(str(id+1))

    def InsertTrack(self):
        ID = self.lineEdit_3.text()
        Title =self.lineEdit.text()
        self._presenter.updateAlbum(ID, Title)
        self._presenter.GetImage(self.frame, Title)
        self._presenter.GetVideo(self.frame2, Title)

    def Close(self):
        self.close()
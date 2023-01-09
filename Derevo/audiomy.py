from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaContent,QMediaPlayer
from PyQt5.QtCore import QUrl, QUrlQuery
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
import okno
import okno2
import okno3

class Audiomy(QtWidgets.QMainWindow):
    _presenter = None
    saveAID = -1
    saveID = -1
    saveUrl = -1
    _okno = None 
    _okno2 = None
    _okno3 = None
    _ID_Games=[]
    def __init__(self, presenter):
        self._okno = okno.Okno(presenter)
        self._okno2 = okno2.Okno(presenter)
        self._okno3 = okno3.Okno(presenter)
        self._presenter = presenter
        super(Audiomy, self).__init__()
        uic.loadUi('ui\\audio.ui', self)
        self.playlist = []
        self.position = 0
        self.state = "Play"


        self.player = QMediaPlayer()
        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)
        self.player.stateChanged.connect(self.state_changed)
        self.pushButton.clicked.connect(self.move_backward)
        self.pushButton_2.clicked.connect(self.play_mp3)
        self.pushButton_3.clicked.connect(self.move_forward)
        self.pushButton_4.clicked.connect(self.open_mp3_file)
        self.pushButton_5.clicked.connect(self.OnButtonClick2)
        self.pushButton_6.clicked.connect(self.OnButtonClick3)
        self.pushButton_7.clicked.connect(self.OnButtonClick4)
        self.pushButton_8.clicked.connect(self.OnButtonClick5)
        self.initComboBox()
        self.tableWidget.itemClicked.connect(self.clickRow)
        self.horizontalSlider.sliderMoved.connect(self.set_position)
        
        self.show()

    def open_mp3_file(self):
        self._okno2.Show2()
        return

    def play_mp3(self):
        self.saveUrl = self.tableWidget.item(self.tableWidget.currentRow(), 3).text()
        if self.state == "Play":
            self.pushButton_2.setText("Pause")
            self.state = "Pause"
            path = self.saveUrl
            if path[0:4] == 'http':
                url = QUrl(path) # web
            else:
                url = QUrl.fromLocalFile(path) # file pc
            content = QMediaContent(url)
            self.player.setMedia(content)
            self.player.setPosition(self.position)
            self.playlist.append(path)
            if len(self.playlist) > 2:
                self.playlist.pop(0)
            if self.tableWidget.currentItem().text() != self.playlist[0]:
                self.position = 0
                self.player.setPosition(self.position)
            self.player.play()
        else:
            self.pushButton_2.setText("Play")
            self.state = "Play"
            self.player.pause()
            paused = self.player.position()
            self.position = paused


    def set_position(self, position):
        self.player.setPosition(position)


    def position_changed(self,position):
        self.horizontalSlider.setValue(position)

    def duration_changed(self, duration):
        self.horizontalSlider.setRange(0, duration)

    def state_changed(self, state):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.pushButton_2.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.pushButton_2.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def move_forward(self):
        self.player.setPosition(int(self.player.position()) + 2000)

    def move_backward(self):
        self.player.setPosition(int(self.player.position()) - 2000)

    def clickRow(self):


        self.saveID = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()

        print(self.saveID)


    def OnButtonClick(self):
        album_title = self.comboBox.currentText()
        track_list = self._presenter.getTrackList(album_title)
        self.tableWidget.setRowCount(len(track_list)-1)
        self.tableWidget.setColumnCount(len(track_list[0]))
        self.tableWidget.setHorizontalHeaderLabels(track_list[0])
        self.tableWidget.setColumnWidth(0, 35)
        self.tableWidget.setColumnWidth(1, 300)
        self.tableWidget.setColumnWidth(2, 79)
        self.tableWidget.verticalHeader().hide()

        for y in range(1, len(track_list)):
            for x in range(len(track_list[0])):
                self.tableWidget.setItem(y-1, x, QTableWidgetItem(track_list[y][x]))

    
    def OnButtonClick2(self):
        album_title = self.comboBox.currentText()
        track_list = self._presenter.deleteTrack(album_title, self.saveID)
        self.tableWidget.setRowCount(len(track_list)-1)
        self.tableWidget.setColumnCount(len(track_list[0]))
        self.tableWidget.setHorizontalHeaderLabels(track_list[0])
        self.tableWidget.setColumnWidth(0, 35)
        self.tableWidget.setColumnWidth(1, 300)
        self.tableWidget.setColumnWidth(2, 79)
        self.tableWidget.verticalHeader().hide()

        for y in range(1, len(track_list)):
            for x in range(len(track_list[0])):
                self.tableWidget.setItem(y-1, x, QTableWidgetItem(track_list[y][x]))

    def OnButtonClick4(self):
        n = int(self.comboBox.currentIndex()) + 1
        self._presenter.deleteAlbum(n)
        self.initComboBox()


    def OnButtonClick5(self):
        self._okno3.Show3()
        return

    def OnButtonClick3(self):
        qwe= self._ID_Games[self.comboBox.currentIndex()]
        self._okno.Show(qwe)
        return

    def initComboBox(self):   
        self.comboBox.activated.connect(self.GetCover)

        albums = self._presenter.getAlbums()
        self.comboBox.clear() 
        self._ID_Games.clear() 
        for row in albums:
            self.comboBox.addItem(row[0])
            self._ID_Games.append(row[1])
        print(row)
        self.GetCover(0)

    def GetCover(self, index):
        album_title = self.comboBox.currentText()
        self.pixmap = QPixmap(self._presenter.GetCoverImage(album_title)[0])
        self.pixmap = self.pixmap.scaled(400, 280)
        self.label.setPixmap(self.pixmap) 
        self.OnButtonClick()


    def closeEvent(self, event):
        self._okno.close()

    
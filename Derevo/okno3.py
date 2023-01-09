import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView
from PyQt5.QtCore import  Qt, QSize
from PyQt5.QtGui import QFont, QColor, QImage, QStandardItemModel, QStandardItem, QPixmap
from PIL import Image
from PIL.ImageQt import ImageQt
from os import path
import videoplayer

class StandardItem(QStandardItem):
    def __init__(self, txt='', image_path='', font_size=12, set_bold=False, color=QColor(0, 0, 0), dataItem = ""):
        super().__init__()       

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)

        self.dataItem = dataItem

        if image_path:
            if (not path.exists(f"thumbnail\\{image_path}") and path.exists(f"image\\{image_path}")):
                image = Image.open(f"image\\{image_path}")
                MAX_SIZE = (100, 100)            
                image.thumbnail(MAX_SIZE)
                image.save(f"thumbnail\\{image_path}")
                image.close()

            image = QImage(f"thumbnail\\{image_path}")
            self.setData(image, Qt.DecorationRole)



class Okno(QMainWindow):
    _presenter = None
    saveID = -1
    frame=""
    _videoplayer = None
    def __init__(self, presenter):
        self._videoplayer = videoplayer.VideoWindow(presenter)
        super(Okno, self).__init__()
        uic.loadUi('ui\\untitled.ui', self)
        self._presenter = presenter

        self.treeView.setHeaderHidden(True)
        self.treeView.header().setStretchLastSection(True)
        self.treeView.clicked.connect(self.onClickItem)

        self.treeModel = QStandardItemModel()
        rootNode = self.treeModel.invisibleRootItem()

        GAME = StandardItem('GAMES', '', 16, dataItem="")

        albums = self._presenter.getAlbums()

        for row in albums:
            text_info = StandardItem(row[0], f'{row[0]}.jpg', 16, dataItem=f"video\\{row[0]}.mp4")
            GAME.appendRow(text_info)
            tracks = self._presenter.getTrackList(row[0])

            for rowt in tracks[1:]:
                tr = StandardItem(rowt[1], '', 16, dataItem= "")
                text_info.appendRow(tr)


        rootNode.appendRow(GAME)
        self.treeView.setModel(self.treeModel)



    def onClickItem(self, sender):
        item = self.treeModel.itemFromIndex(sender)
        urlmp4= item.dataItem
        print(urlmp4)
        self._videoplayer.Show(urlmp4)

    def Show3(self):
        self.show()



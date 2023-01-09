import Model
import audiomy
class Presenter:
    def __init__(self):
        self._model = Model.Model()
        self._audio = audiomy.Audiomy(self)
    def GetCoverImage(self, name):
        return self._model.getImage(name), 

    def getAlbums(self):
        return self._model.getAlbumsSQL()
        

    def getTrackList(self, album_title):
        return self._model.getTrackListSQL(album_title)

    def deleteTrack(self, album_title, id):
        return self._model.deleteTracklist(album_title, id)

    def deleteAlbum(self, ID):
        return self._model.deleteAlbums(ID)

    def updateTrack(self, ID_Game, Title, LenTrack, Songs):
        self._model.updateTracklist(ID_Game, Title, LenTrack, Songs)
        self._audio.OnButtonClick()
    
    def updateAlbum(self, ID, Title):
        self._model.updateAlbums(ID, Title)
        self._audio.initComboBox()
    
    def GetImage(self, path, Title):
        self._model.getimagejpg(path, Title)

    def GetVideo(self, path, Title):
        self._model.getvideomp4(path, Title)
    
    def GetLastID(self):
        return self._model.getlastid()


import sqlite3
import shutil
class Model:
    _connect = None
    _cursor = None

    def __init__(self):
        self._connect = sqlite3.connect('db\\GameSoundtrack2.db')
        self._cursor = self._connect.cursor()


    def getTrackListSQL(self, album_title):
        table, sql = self.getSQLQuery('sql\\test.sql')
        for row in self._cursor.execute(sql, [album_title]):
            line = []
            for colum in row:
                line.append(str(colum))
            table.append(line)
        
        return table

    def getSQLQuery(self, name):
        header = []
        sqlread = ''
        with open(name, 'r') as file:
            header = file.readline().split(', ')        
            for line in file.readlines():
                sqlread += line
        
        return [header], sqlread


    def getAlbumsSQL(self):
        table = []
        for row in self._cursor.execute("SELECT Title, ID FROM Game;"):
            line = []
            for colum in row:
                line.append (colum)
            table.append(line)
        
        return table

    def getImage(self, name):
        return 'image\\' + name + '.jpg'
    
    def deleteTracklist(self, album_title, id):
        table = [["Title", "Time"]]
        sql = '''DELETE FROM Soundtracks WHERE ID=?;'''
        self._cursor.execute(sql, [id])

        self._connect.commit()
        table = self.getTrackListSQL(album_title)
        return table
    
    def deleteAlbums(self, ID):
        table = [["Title", "Time"]]
        sql = '''DELETE FROM Game WHERE ID=?;'''
        self._cursor.execute(sql, [ID])

        self._connect.commit()

    def updateTracklist(self, ID_Game, Title, LenTrack, Songs):
        table = [["Title", "Time"]]
        sql = '''INSERT INTO Soundtracks (ID_Game, Title, LenTrack, Songs) VALUES (?, ?, ?, ?);'''
        self._cursor.execute(sql, [ ID_Game, Title, LenTrack, Songs])

        self._connect.commit()
    def updateAlbums(self, ID, Title):
        table = [["Title", "Time"]]
        sql = '''INSERT INTO Game (ID, Title) VALUES (?, ?);'''
        self._cursor.execute(sql, [ID, Title])

        self._connect.commit()
    
    def getimagejpg(self, path, Title):
        shutil.copy2(path, f'image\\{Title}.jpg') 

    def getvideomp4(self, path, Title):
        shutil.copy2(path, f'video\\{Title}.mp4') 

    def getlastid(self):
        sql = '''SELECT ID FROM Game ORDER BY ID DESC LIMIT 1;'''
        self._cursor.execute(sql)
        Tb=self._cursor.fetchone()
        return(Tb[0])

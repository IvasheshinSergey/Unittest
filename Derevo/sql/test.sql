ID, Title, Time", URL
SELECT 
    Soundtracks.ID,
    Soundtracks.Title,
    Soundtracks.LenTrack,
    Soundtracks.Songs
FROM Soundtracks INNER JOIN Game
ON Soundtracks.ID_Game = Game.ID
WHERE Game.Title = ?
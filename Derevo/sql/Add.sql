CREATE TABLE Game (
ID INTEGER,
Title TEXT);


CREATE TABLE Soundtracks (
ID INTEGER Primary Key AUTOINCREMENT,
ID_Game INTEGER,
Title TEXT,
LenTrack TEXT,
Songs TEXT);
   

INSERT INTO Game 
(ID, Title) 
VALUES
(1, "Final Fantasy 8"),
(2, "Nier Automata");

INSERT INTO Soundtracks 
(ID_Game, Title, LenTrack, Songs) 
VALUES
(1, "Liberi Fatali", "3:08", "https://fi.zophar.net/soundfiles/playstation-psf/final-fantasy-viii/101%20Liberi%20Fatali.mp3"),
(1, "Balamb GARGEN", "3:47", "https://fi.zophar.net/soundfiles/playstation-psf/final-fantasy-viii/102%20Balamb%20Garden.mp3"),
(1, "Blue Fields", "4:34", "https://fi.zophar.net/soundfiles/playstation-psf/final-fantasy-viii/103%20Blue%20Fields.mp3"),
(1, "The winner", "4:38", "https://fi.zophar.net/soundfiles/playstation-psf/final-fantasy-viii/105%20The%20Winner.mp3"),

(2, "Significance", "3:41", "https://audio.itunes.apple.com/apple-assets-us-std-000001/AudioPreview111/v4/f5/52/be/f552be8e-d049-d1b8-43c7-dfa9a2c3c232/mzaf_5877559613266904005.plus.aac.p.m4a"),
(2, "Peaceful Sleep", "3:29", "http://audio.itunes.apple.com/apple-assets-us-std-000001/AudioPreview122/v4/0d/c7/52/0dc75299-8408-5fa4-ee1b-75a6b020d9e8/mzaf_813138670878660225.plus.aac.p.m4a");


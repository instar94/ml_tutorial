from mp3player import mp3 as m
from mp3player import song as s

s1 = s.Song("노래1","가수1",3)
s2 = s.Song("노래2","가수2",4)
s3 = s.Song("노래3","가수3",2)
s4 = s.Song("노래4","가수4",1)
s5 = s.Song("노래5","가수5",3)

player=m.Player()
player.addSong(s1)
player.addSong(s2)
player.addSong(s4)
player.addSong(s3)
player.addSong(s5)

player.suffle()

player.play()
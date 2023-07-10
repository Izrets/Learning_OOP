class MediaPlayer:
    def open(self, file):
        self.filename = file
        return file

    def play(self):
        print('Воспроизведение', tr)


media1 = MediaPlayer()
tr = media1.open('filemedia1')
media1.play()

media2 = MediaPlayer()
tr2 = media2.open('filemedia2')
media1.play()


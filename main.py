import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt, QUrl

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.media = QMediaPlayer(self)
        self.media.setVideoOutput(self.widget)
        self.button_start.clicked.connect(self.media_play)
        self.button_stop.clicked.connect(self.media_stop)
        self.calendarWidget.selectionChanged.connect(self.get_date)

    def media_play(self):
        self.media.play()
    def media_stop(self):
        self.media.stop()
    def get_date(self):
        self.media.stop()
        day=str(self.calendarWidget.selectedDate().day())


        self.media.setMedia(QMediaContent(QUrl.fromLocalFile(f'Video\\{day}.avi')))
        if self.checkBox.isChecked():
            self.media.play()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=App()
    ex.show()
    sys.exit(app.exec())

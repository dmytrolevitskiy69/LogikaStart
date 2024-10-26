import os
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Діалог відкриття файлів (і папок)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image

app=QApplication([])
win=QWidget()
win.resize(700,500)
win.setWindowTitle('Easy Editor')
lb_image=QLabel('Тут буде картинка')
btn_dir=QPushButton('Папка')
lw_files=QListWidget()


btn_left=QPushButton('Вліво')
btn_right=QPushButton('Вправо')
btn_flip=QPushButton('Дзеркало')
btn_sharp=QPushButton('Різкість')
btn_grey=QPushButton('Ч/Б')

row=QHBoxLayout()
col1=QVBoxLayout()
col2=QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image,95)

row_tools=QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_grey)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)
win.show()

workdir=''
def filter(filenames, extensions):
    result=[]
    for filename in filenames:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result
        

def chooseWorkdir():
    global workdir
    workdir=QFileDialog.getExistingDirectory()
def showFilenamesList():
    extensions=['.png', '.jpg', '.jpeg', '.bmp', '.gif', '.avif']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir),extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)

btn_dir.clicked.connect(showFilenamesList)

class ImageProcessor():
    def __init__(self):
        self.image=None
        self.dir=None
        self.filename=None
        self.save_dir="Modified/"
    def loadImage(self, filename):
        self.dir=workdir
        self.filename=filename
        image_path=os.path.join(workdir,filename)
        self.image=Image.open(image_path)
    
    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
         os.mkdir()
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(workdir,self.save_dir, self.filename)
        self.showImage(image_path)




    def showImage(self, path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)

        lb_image.show()

workimage = ImageProcessor()
def showChoosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(filename)
        image_path=os.path.join(workimage.dir,workimage.filename)
        workimage.showImage(image_path)

lw_files.currentRowChanged.connect(showChoosenImage)
btn_grey.clicked.connect(workimage.do_bw)
app.exec()
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
#from PIL.ImageQt import ImageQt # Для перенесення графіки з Pillow до QT
from PIL import ImageFilter
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
   GaussianBlur, UnsharpMask
)

app = QApplication([])
win = QWidget()       
win.resize(700, 500) 
win.setWindowTitle('Easy Editor')
lb_image = QLabel("Тут буде картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()


btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_flip = QPushButton("Дзеркало")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")


row = QHBoxLayout()              # Основний рядок
col1 = QVBoxLayout()             # ділиться на два стовпці
col2 = QVBoxLayout()    
col1.addWidget(btn_dir)          # у першому – кнопка вибору директорії
col1.addWidget(lw_files)         # та список файлів
col2.addWidget(lb_image, 95)     # у другому - картинка
row_tools = QHBoxLayout()        # та рядок кнопок
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)


row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)
win.show()

workdir='' #шлях до фапки з файлами
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
    extensions=['.png','.jpg','.jpeg','.bmp','.gif','.avif']
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
    def loadImage(self, dir, filename):

       self.dir = dir##
       self.filename = filename
       image_path = os.path.join(dir, filename)
       self.image = Image.open(image_path)
    def saveImage(self):

       path = os.path.join(self.dir, self.save_dir)
       if not(os.path.exists(path) or os.path.isdir(path)):
           os.mkdir(path)
       image_path = os.path.join(path, self.filename)
       self.image.save(image_path)

    def do_bw(self):
        if self.image is not None:
            self.image = self.image.convert("L") #робить картинку сірою
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showImage(image_path)

    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def do_sharpen(self):
        self.image = self.image.filter(SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)



    def showImage(self, path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w,h=lb_image.width(), lb_image.height()
        pixmapimage=pixmapimage.scaled(w,h,Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)

        lb_image.show()
    
workimage = ImageProcessor()
def showChoisenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir,filename)###
        image_path=os.path.join(workimage.dir,workimage.filename)
        workimage.showImage(image_path)

lw_files.currentRowChanged.connect(showChoisenImage)    
btn_bw.clicked.connect(workimage.do_bw)
btn_flip.clicked.connect(workimage.do_flip)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_sharp.clicked.connect(workimage.do_sharpen)
app.exec()
from PIL import Image
from PIL import ImageFilter
with Image.open('riba.jpg') as original:
    original.show()
    print('Розмір зображення:', original.size)
    print('Формат:', original.format)
    print('Тип Файлу:', original.mode)
    original.show()
    
    pic_gray = original.convert('L')
    pic_gray.save('gray1.jpg')
    print('Розмір зображення:', pic_gray.size)
    print('Формат:', pic_gray.format)
    print('Тип Файлу:', pic_gray.mode)
    pic_gray.show()
    
    pic_blur=original.filter(ImageFilter.BLUR)
    pic_blur.save('blur.jpg')
    pic_blur.show()
    
    pic_up=original.transpose(Image.ROTATE_90)
    pic_up.save('rotate.jpg')
    pic_up.show()
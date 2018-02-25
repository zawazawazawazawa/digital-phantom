# coding: utf-8
from PIL import Image
import numpy as np
import dicom

for i in range(1, 50):
    #tif画像読み込み
    img = Image.open('C:\Python27\matsuzawa\Cube\Cube_post\\3mm\cube3mm_{}.tif'.format(i))
    width, height = img.size
    img_pixels = []

    for y in range(height):
        row = []
        for x in range(width):
            row.append(img.getpixel((x, y)))
        img_pixels.append(row)

    img_pixels = np.array(img_pixels)

    #dicom画像読み込み
    ds = dicom.read_file("C:\Python27\matsuzawa\Cube\Cube_pre\\3mm\cube3mm_{}.dcm".format(i))

    for y in range(height):
        for x in range(width):
            ds.pixel_array[y][x] = img_pixels[y][x]

    ds.PixelData = ds.pixel_array.tostring()
    ds.save_as("C:\Python27\matsuzawa\cube\\add_noise\\3mm\cube3mm_noise_{}.dcm".format(i))

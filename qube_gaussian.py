# coding: utf-8
import dicom
from scipy import ndimage

# 画像読み込み
ds = dicom.read_file("C:\Python27\matsuzawa\qube\qube_1.dcm")

blurred_image = ndimage.gaussian_filter(ds.pixel_array, sigma = 2)


ds.PixelData = blurred_image

ds.save_as("C:\Python27\matsuzawa\qube_FWHM1mm\FWHM1mm_1.dcm")

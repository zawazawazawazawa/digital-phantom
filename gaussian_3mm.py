# coding: utf-8
import dicom
from scipy import ndimage

for h in range(1, 9):
    for i in range(1, 13):
        # 画像読み込み
        ds = dicom.read_file("C:\Python27\matsuzawa\qube\qube_{}.dcm".format(i))
        # ヘッダー書き換え
        ds[0x10, 0x10].value = "gaussian_{}mm".format(h)
        ds.PatientID = "gaussian_{}mm".format(h)

        # 各FWHMに対するσの値
        sigmas = [0.106, 0.213, 0.319, 0.426, 0.532, 0.638, 0.745, 0.851]

        blurred_image = ndimage.gaussian_filter(ds.pixel_array, sigma = sigmas[h-1])

        ds.PixelData = blurred_image

        ds.save_as("C:\Python27\matsuzawa\qube_FWHM{}mm\FWHM{}mm_{}.dcm".format(h, h, i))

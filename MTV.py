# coding:utf-8

import dicom
import os

os.mkdir("C:\Python27\matsuzawa\MTV_suv")
slicenumber = 0
for a, b, c in zip(range(139, 130, -1), range(49319, 49202, -13), range(4, 36, 4)):
    #画像の読み込み
    ds = dicom.read_file("C:\Python27\matsuzawa\\2bed\\2BED_SCAN.PT.PET_PETCT_WB_(ADULT).0004.0{}.2017.11.24.15.43.27.521875.70{}.IMA".format(a,b))

    slicenumber += 1

    # ヘッダー情報の書き換え
    ds.SliceThickness = "4"  # スライス厚
    ds.PixelSpacing = "4.0\\4.0"  # ピクセルサイズ
    ds.RescaleSlope = "1.0"
    ds[0x20, 0x32].value = "-341.597137451172\\-486.458740234375\\-{}".format(c)  # ImageLocation
    ds.SliceLocation = "-{}".format(c)  # SliceLocation
    ds[0x10, 0x1030].value = "10"  # Patient's Weight (kg)
    ds[0x10, 0x40].value = "M" # Patient's Sex
    ds.RadionuclideTotalDose = "10000000"  # TotalDose (Bq)
    ds[0x10, 0x10].value = "MTV" #Patient's name
    ds.PatientID = "MTV"
    ds.ImageNumber = str(slicenumber)

    # 全画素値を0に
    for n, val in enumerate(ds.pixel_array.flat):
        ds.pixel_array.flat[n] = 0

    for m in range(81, 88):
        for n in range(81, 88):
            ds.pixel_array[m][n] = 2188  # SUV2.2

    for m in range(82, 87):
        for n in range(82, 87):
            ds.pixel_array[m][n] = 2288  # SUV2.3

    for m in range(83, 86):
        for n in range(83, 86):
            ds.pixel_array[m][n] = 2387  # SUV2.4

    ds.pixel_array[84][84] = 2487  # SUV2.5

    ds.PixelData = ds.pixel_array.tostring()
    ds.save_as("C:\Python27\matsuzawa\MTV_suv\MTV_suv_{}.dcm".format(slicenumber))


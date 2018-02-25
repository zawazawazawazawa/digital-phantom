# coding:utf-8

import dicom
import os

os.mkdir("C:\Python27\matsuzawa\SUVpeak2")
slicenumber = 0
for a, b, c in zip(range(139, 117, -1), range(49319, 49033, -13), range(4, 4 * 21, 4)):
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
    ds[0x10, 0x10].value = "SUVpeak2" #Patient's name
    ds.PatientID = "SUVpeak2"
    ds.ImageNumber = str(slicenumber)

    # 全画素値
    for n, val in enumerate(ds.pixel_array.flat):
        ds.pixel_array.flat[n] = 0


    if 5 <= slicenumber <= 16:
        for n in range(125, 134):
            for m in range(125, 131):
                ds.pixel_array[n][m] = 995 #SUV1.0 (正確には0.99998)

    if 9 <= slicenumber <= 12:
        if slicenumber == 11:
            ds.pixel_array[126][127] = 4974  # SUV5.0
        for n in range(129, 133):
            for m in range(126, 130):
                ds.pixel_array[n][m] = 3979 #SUV4.0



    ds.PixelData = ds.pixel_array.tostring()
    ds.save_as("C:\Python27\matsuzawa\SUVpeak2\SUVpeak2_{}.dcm".format(slicenumber))

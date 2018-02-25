# coding:utf-8

import dicom
import os

for thickness in range(1, 9):
    os.mkdir("C:\Python27\matsuzawa\slicethickness_{}mm".format(thickness))
    slicenumber = 0
    for a, b, c in zip(range(139, 130, -1), range(49319, 49202, -13), range(thickness, thickness * 10, thickness)):
        ds = dicom.read_file("C:\Python27\matsuzawa\\2bed\\2BED_SCAN.PT.PET_PETCT_WB_(ADULT).0004.0{}.2017.11.24.15.43.27.521875.70{}.IMA".format(a,b))

        slicenumber += 1

        # ヘッダー情報の書き換え
        ds.SliceThickness = str(thickness)  # スライス厚
        ds.PixelSpacing = "4.0\\4.0"  # ピクセルサイズ
        ds.RescaleSlope = "1.0"
        ds[0x20, 0x32].value = "-341.597137451172\\-486.458740234375\\-{}".format(c)  # ImageLocation
        ds.SliceLocation = "-{}".format(c)  # SliceLocation
        ds[0x10, 0x1030].value = "10"  # Patient's Weight (kg)
        ds[0x10, 0x40].value = "M" # Patient's Sex
        ds.RadionuclideTotalDose = "10000000"  # TotalDose (Bq)
        ds[0x10, 0x10].value = "slicethickness_{}mm".format(thickness) #Patient's name
        ds.PatientID = "slicethickness_{}mm".format(thickness)
        ds.ImageNumber = str(slicenumber)

        # 全画素値
        for n, val in enumerate(ds.pixel_array.flat):
            ds.pixel_array.flat[n] = 0

        if slicenumber == 1 or slicenumber == 2 or slicenumber == 9:
            for n in range(125, 130 ):
                for m in range(125, 130):
                    ds.pixel_array[n][m] = 995 #SUV1.0 (正確には0.99998)
        elif slicenumber == 3 or slicenumber == 4 or slicenumber == 7 or slicenumber == 8:
            for n in range(125, 130 ):
                for m in range(125, 130):
                    ds.pixel_array[n][m] = 1990 #SUV2.0
        else:
            for n in range(125, 130):
                for m in range(125, 130):
                    ds.pixel_array[n][m] = 3979  # SUV4.0

        ds.PixelData = ds.pixel_array.tostring()
        ds.save_as("C:\Python27\matsuzawa\slicethickness_{}mm\slicethickness_{}mm_{}.dcm".format(thickness, thickness, slicenumber))

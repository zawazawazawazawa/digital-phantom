# coding: utf-8
import dicom

slicenumber = 0

for a, b, c in zip(range(139, 78, -1), range(49319, 48526, -13), range(3, 3 * 50, 3)):
    ds = dicom.read_file("C:\Python27\matsuzawa\\2bed\\2BED_SCAN.PT.PET_PETCT_WB_(ADULT).0004.0{0:03d}.2017.11.24.15.43.27.521875.70{1}.IMA".format(a,b))

    slicenumber += 1

    # ヘッダー情報の書き換え

    ds.SliceThickness = "3"  # スライス厚
    ds.PixelSpacing = "4.0\\4.0"  # ピクセルサイズ
    ds.RescaleSlope = "1.0"
    ds[0x20, 0x32].value = "-341.597137451172\\-486.458740234375\\-{}".format(c)  # ImageLocation
    ds.SliceLocation = "-{}".format(c)  # SliceLocation
    ds[0x10, 0x1030].value = "10"  # Patient's Weight (kg)
    ds[0x10, 0x40].value = "M" # Patient's Sex
    ds.RadionuclideTotalDose = "10000000"  # TotalDose (Bq)
    ds[0x10, 0x10].value = "cube3mm" #Patient's name
    ds.PatientID = "cube3mm"
    ds.ImageNumber = str(slicenumber)

    # 全画素値
    for n, val in enumerate(ds.pixel_array.flat):
        ds.pixel_array.flat[n] = 0

    """
    cube4つ
    1. 11 * 11
    2. 9 * 9
    3. 7 * 7
    4. 5 * 5
    """
    #SUV1.0 (正確には0.99998)
    if 11 <= slicenumber <= 40:
        for n in range(10, 250):
            for m in range(10, 250):

                if 11 <= slicenumber <= 20:
                    ds.pixel_array[n][m] = 995  # SUV1.0

                #4の終わりまで
                if 21 <= slicenumber <= 25:
                    if 105 <= n <= 113 and 105 <= m <= 113:
                        ds.pixel_array[n][m] = 3979  #2
                    elif 104 <= n <= 114 and 145 <= m <= 155:
                        ds.pixel_array[n][m] = 3979  #
                    elif 145 <= n <= 151 and 106 <= m <= 112:
                        ds.pixel_array[n][m] = 3979  # 3
                    elif 148 <= n <= 152 and 148 <= m <= 152:
                        ds.pixel_array[n][m] = 3979  # 4
                    else:
                        ds.pixel_array[n][m] = 995 #SUV1.0

                #3の終わりまで
                if 26 <= slicenumber <= 27:
                    if 105 <= n <= 113 and 105 <= m <= 113:
                        ds.pixel_array[n][m] = 3979  #2
                    elif 104 <= n <= 114 and 145 <= m <= 155:
                        ds.pixel_array[n][m] = 3979  #1
                    elif 145 <= n <= 151 and 106 <= m <= 112:
                        ds.pixel_array[n][m] = 3979  # 3
                    else:
                        ds.pixel_array[n][m] = 995 #SUV1.0

                # 2の終わりまで
                if 28 <= slicenumber <= 29:
                    if 105 <= n <= 113 and 105 <= m <= 113:
                        ds.pixel_array[n][m] = 3979  #2
                    elif 104 <= n <= 114 and 145 <= m <= 155:
                        ds.pixel_array[n][m] = 3979  #1
                    else:
                        ds.pixel_array[n][m] = 995 #SUV1.0

                # 1の終わりまで
                if 30 <= slicenumber <= 31:
                    if 104 <= n <= 114 and 145 <= m <= 155:
                        ds.pixel_array[n][m] = 3979  #1
                    else:
                        ds.pixel_array[n][m] = 995 #SUV1.0

                if 32 <= slicenumber <= 40:
                    ds.pixel_array[n][m] = 995  # SUV1.0



    ds.PixelData = ds.pixel_array.tostring()
    ds.save_as("C:\Python27\matsuzawa\cube3mm_{}.dcm".format(slicenumber))

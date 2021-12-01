import sys
import os
"""
class SP3:
    def __init__(self,a):
        self.a = a

    def convertVideoContainer(a):
        while True:  # Creo un menú para interactuar con el user
            try:
                result = int(
                    input(
                        "Choose one of Video Container to convert it. '1','2','3' or '4' (0=return to main menu): \n"
                        "1. VP8 \n"
                        "2. VP9 \n"
                        "3. h265 \n"
                        "4. AV1 \n"))
            except ValueError:
                print("You must to enter a number.")
                continue
            if result == 1:
                os.system("ffmpeg -i BBBvideo.mp4 -c:v libvpx -b:v 1M -c:a libvorbis VP8.webm")
                # https://trac.ffmpeg.org/wiki/Encode/VP8
                continue
            elif result == 2:
                os.system("ffmpeg -i BBBvideo.mp4 -c:v libvpx-vp9 -crf 30 -b:v 0 VP9.webm")
                # https://trac.ffmpeg.org/wiki/Encode/VP9
                continue
            elif result == 3:
                os.system("ffmpeg -i BBBvideo.mp4 -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k h265.mp4")
                # https://trac.ffmpeg.org/wiki/Encode/H.265
                continue
            elif result == 4:
                os.system("ffmpeg -i BBBvideo.mp4 -c:v libaom-av1 -minrate 500k -b:v 2000k -maxrate 2500k AV1.mp4")
                # https://trac.ffmpeg.org/wiki/Encode/AV1
                continue
            elif result == 0:  # Para salir del programa
                break
            elif result != 1 and result != 2 and result != 3 and result != 4:
                print("You must enter '1' or '2'.")
                continue

while True:  # Creo un menú para interactuar con el user
    try:
        result = int(
            input(
                "Choose one of Video Container to convert it. '1','2','3' or '4' (0=return to main menu): \n"
                "1. VP8 \n"
                "2. VP9 \n"
                "3. h265 \n"
                "4. AV1 \n"))
    except ValueError:
        print("You must to enter a number.")
        continue
    if result == 1:
        os.system("ffmpeg -i BBBvideo.mp4 -c:v libvpx -b:v 1M -c:a libvorbis VP8.webm")
        # https://trac.ffmpeg.org/wiki/Encode/VP8
        continue
    elif result == 2:
        os.system("ffmpeg -i BBBvideo.mp4 -c:v libvpx-vp9 -crf 30 -b:v 0 VP9.webm")
        # https://trac.ffmpeg.org/wiki/Encode/VP9
        continue
    elif result == 3:
        os.system("ffmpeg -i BBBvideo.mp4 -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k h265.mp4")
        # https://trac.ffmpeg.org/wiki/Encode/H.265
        continue
    elif result == 4:
        os.system("ffmpeg -i BBBvideo.mp4 -c:v libaom-av1 -minrate 500k -b:v 2000k -maxrate 2500k AV1.mp4")
        # https://trac.ffmpeg.org/wiki/Encode/AV1
        continue
    elif result == 0:  # Para salir del programa
        break
    elif result != 1 and result != 2 and result != 3 and result != 4:
        print("You must enter '1' or '2'.")
        continue
"""

while True:  # Creo un menú para interactuar con el user
    try:
        print(
            "Choose two of these codecs to visualize them. '1','2','3' or '4' (0=return to main menu): \n"
            "1. VP8 \n"
            "2. VP9 \n"
            "3. h265 \n"
            "4. AV1 \n")
        result1 = int(input("First codec: \n"))
        result2 = int(input("Second codec: \n"))
    except ValueError:
        print("You must to enter a number.")
        continue
    if result1 == 1 and result2 == 2:
        os.system("ffmpeg -i BBBvideo.mp4 -vf "movie=BBBvideo.mp4 [BBBvideo]; movie=h265.mp4 [h265]; [in][BBBvideo] overlay=0:366, [h265] overlay=592:41" combined.mp4")
        continue
    elif result1 == 1 and result2 == 3:
        os.system("")
        continue
    elif result1 == 1 and result2 == 4:
        os.system("")
        continue
    elif result1 == 2 and result2 == 1:
        os.system("")
        continue
    elif result1 == 2 and result2 == 3:
        os.system("")
        continue
    elif result1 == 2 and result2 == 4:
        os.system("")
        continue
    elif result1 == 3 and result2 == 1:
        os.system("")
        continue
    elif result1 == 3 and result2 == 2:
        os.system("")
        continue
    elif result1 == 3 and result2 == 4:
        os.system("")
        continue
    elif result1 == 4 and result2 == 1:
        os.system("")
        continue
    elif result1 == 4 and result2 == 2:
        os.system("")
        continue
    elif result1 == 4 and result2 == 3:
        os.system("")
        continue
    elif result1 == 0:  # Para salir del programa
        break
    elif result1 != 1 and result1 != 2 and result1 != 3 and result1 != 4 and result2 != 1 and result2 != 2 and result2 != 3 and result2 != 4:
        print("You must enter '1' or '2'.")
        continue
    elif result1 == result2:
        print("You must select different codecs to visualize.")
        continue

# SP3_VideoEndodingUPF

That's the third Lab of Audio and Video Encoding made by Víctor Zaldivar. The main purpose for the lab is to implement the ‘ffmpeg’ through python scripts. First thing that I did was download the BBB video from and trim it into a 10 seconds video called 'BBBvideo.mp4'.

Every task of the seminar is divided in different functions inside the SP3.py script. I created a class for the project and their methods and functions are corresponding to each task of the project. By calling the main script, you are able to run all the program and iterate between the classes and functions.

The first task consist on convert the video codec from the BBBvideo (h264) into 4 different video codecs (AV1, h265, VP8 and VP9). For that, I create a menu for the user to be able to select which video codec wants to convert it. Then, through calling 'ffmpeg' we can extract the 4 output video files.

The second task consist on join to different videos on the same screen to compare each video codec in terms of resolution. To do it, I create a menu for the user to be able to select which to videos wants to be showed on the screen. 

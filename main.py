# install moviepy using pip : pip install moviepy.

import sys 
from moviepy.editor import VideoFileClip

mp4_file = sys.argv[1] # taking input from the user as command line arguments
mp3_file = sys.argv[1].split('.')[0]+'.mp3'

vc = VideoFileClip(mp4_file) # loading the video file
ac = vc.audio # extracting the audio from the file

ac.write_audiofile(mp3_file) # writng the extracted audio to a file

ac.close() # closing the audio file
vc.close() # closing the video file

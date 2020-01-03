from moviepy.editor import *

video = VideoFileClip("video_path")
audio = video.audio
audio.write_audiofile("audio_path_to_save")
from moviepy.editor import *


def extract_audio_from_clip(video_path, new_audio_file):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(new_audio_file)
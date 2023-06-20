import moviepy.editor
from pathlib import Path

video_file = Path('my_video.mp4')

while True:
    user_input = input("Введите сообщение 'разделить': ")
    if user_input.lower() == "разделить":
        video = moviepy.editor.VideoFileClip(str(video_file))
        audio = video.audio
        audio.write_audiofile(f'{video_file.stem}.mp3')
        break
    else:
        print("Введите 'разделить' для выполнения программы.")
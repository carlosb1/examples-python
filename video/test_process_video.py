
import ffmpeg
from pydub import silence
from pydub import AudioSegment 

input_file = 'test1.mp4'
output_file = 'test1_output.mp4'

probe = ffmpeg.probe(input_file)
video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
# TODO check if exists audio
audio_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'audio'), None)
width = int(video_stream['width'])
height = int(video_stream['height'])
duration = float(video_stream['duration'])
# not for all frames
nb_frames = float(video_stream['nb_frames'])
fps = nb_frames / duration
# duration_ms = duration * 1000.

print("width : "+str(width))
print("height : "+str(height))
print("duration : "+str(duration))
print("nb_frames : "+str(nb_frames))
print("frames / sec: "+ str(fps))


#Search silence parts
song = AudioSegment.from_file(input_file)
chunks_nosilent_frames = silence.detect_nonsilent(song)
print(str(chunks_nosilent_frames))


# start and end frames

clips = []
for [start_millisec, stop_millisec] in chunks_nosilent_frames:
    print("starting for: "+str(start_millisec))
    print("stopping in: "+str(stop_millisec))
    start_sec = start_millisec / 1000.
    stop_sec = stop_millisec / 1000.
    time_in_secs = stop_sec - start_sec
    clip = ffmpeg.input(input_file, ss=start_sec, t=time_in_secs)
    v = clip.video
    a = clip.audio
    clips.append(v)
    clips.append(a)

concatenated =ffmpeg.concat(*clips, v=1, a=1)
result = concatenated.output(output_file)
result.run()

https://realpython.com/python-speech-recognition/
https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0144610
https://dsp.stackexchange.com/questions/17628/python-audio-detecting-silence-in-audio-signal
https://stackoverflow.com/questions/40776477/remove-silence-from-an-audio-input-and-then-find-the-frequencies-of-the-remainin
https://stackoverflow.com/questions/29547218/remove-silence-at-the-beginning-and-at-the-end-of-wave-files-with-pydub#29550200
https://github.com/Borda/docker_python-opencv-ffmpeg
https://stackoverflow.com/questions/19493214/synchronizing-audio-and-video-with-opencv-and-pyaudio

-> usar opencv
    -> no hay ejemplos de como usar audio
-> usar ffmpeg 
        -> ejemplo con silencio
        -> buscar manera de split y unir

https://stackoverflow.com/questions/45607882/how-to-read-video-file-in-python-with-audio-stream-on-linux!!
https://stackoverflow.com/questions/38518302/convert-numpy-array-to-audiofileclip-in-moviepy


-> extraer frames de sonido con problemas
-> seleccionar los que no nos gustan
-> elegir los frames, eliminarlos 
-> concatenar los frames


Escoger frames con 
def extract_frame(stream, frame_num):
    while isinstance(stream, ffmpeg.nodes.OutputStream):
        stream = stream.node.incoming_edges[0].upstream_node.stream()
    out, _ = (
        stream
        .filter_('select', 'gte(n,{})'.format(frame_num))
        .output('pipe:', format='rawvideo', pix_fmt='rgb24', vframes=1)
        .run(capture_stdout=True, capture_stderr=True)
    )
    return np.frombuffer(out, np.uint8).reshape([height, width, 3])


-> filter! -> buscar
-> mejorar para eliminar ruido


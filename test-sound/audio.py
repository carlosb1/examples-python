# Crear una melodía estilo Synthwave con MIDIUtil
from midiutil import MIDIFile

# Configuración general
bpm = 90
measures = 16  # duración más corta para demostración
beats_per_measure = 4
track_count = 3

midi = MIDIFile(track_count)

# Asignar tempo a cada pista
for track in range(track_count):
    midi.addTempo(track, 0, bpm)

# Bajo Synthwave - Track 0 (ostinato rítmico)
bass_pattern = [36, 36, 36, 38, 36, 36, 41, 43]  # C2 - D2 - F2 - G2
for i in range(measures * beats_per_measure):
    note = bass_pattern[i % len(bass_pattern)]
    midi.addNote(0, 0, note, i, 1, 100)

# Acordes suaves (pads) - Track 1
pad_chords = [
    [60, 64, 67],  # C major
    [62, 65, 69],  # D minor
    [59, 63, 67],  # B diminished
    [60, 64, 67],  # C major again
]
for i in range(measures):
    chord = pad_chords[i % len(pad_chords)]
    for note in chord:
        midi.addNote(1, 1, note, i * 4, 4, 60)

# Melodía estilo lead synth - Track 2
melody = [72, 74, 76, 79, 76, 74, 72, 69, 67, 69, 72]
start_time = 4  # empieza después del primer compás
for i, note in enumerate(   melody):
    midi.addNote(2, 2, note, start_time + i, 0.75, 90)

# Guardar el archivo
file_path = "synthwave_melody_loop.mid"
with open(file_path, "wb") as f:
    midi.writeFile(f)

file_path
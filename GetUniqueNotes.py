import mido
import os

midi_folder_path = os.getcwd() +os.sep+ "midi"
midi_file_path = os.listdir(os.getcwd() + os.sep + "midi")[0]

midi = mido.MidiFile(midi_folder_path + os.sep + midi_file_path)
unique_notes = set()

for track in midi.tracks:
    for msg in track:
        if msg.type in ["note_on", "note_off"]:
            unique_notes.add(msg.note)

sorted_notes = sorted(unique_notes)
print("Unique MIDI Notes:", sorted_notes)

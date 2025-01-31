import mido
import pyautogui
import time
import os
from collections import defaultdict

# Define MIDI note-to-keyboard mapping (Adjust as needed)
MIDI_TO_KEY = {
    49: '2',  # C#3 / Db3 
    50: 'w',  # D3
    51: '3',  # D#3 / Eb3 
    52: 'e',  # E3
    53: 'r',  # F3
    54: '5',  # F#3 / Gb3
    55: 't',  # G3
    56: '6',  # G#3 / Ab3
    57: 'y',  # A3 
    58: '7',  # A#3 / Bb3
    59: 'u',  # B3

    60: 'i',  # C4
    61: '9',  # C#4 
    62: 'o',  # D4 
    63: '0',  # D#4 
    64: 'p',  # E4 
    65: 'z',  # F4 
    66: 's',  # F#4 
    67: 'x',  # G4 
    68: 'd',  # G#4 
    69: 'c',  # A4

    70: 'f',  # A#4 / Bb4
    71: 'v',  # B4
    72: 'b',  # C5
    73: 'h',  # C#5 / Db5 
    74: 'n',  # D5 
    75: 'j',  # D#5 / Eb5 
    76: 'm',  # E5 
    78: 'l',  # F#5 / Gb5
    79: '.',  # G5 
    80: ';',  # G#5 / Ab5 
    82: '\'',  # A#5 / Bb5
    83: '\'',  # B5 
}

# Load MIDI file
midi_folder_path = os.getcwd() +os.sep+ "midi"
midi_file = os.listdir(os.getcwd() + os.sep + "midi")[0]
midi = mido.MidiFile(midi_folder_path + os.sep + midi_file)

# Dictionary to store key events grouped by current_time
key_events_dict = defaultdict(list)
# Track the current time in the MIDI file (relative time)
current_time = 0

# Iterate through all MIDI messages
for msg in midi:
    current_time += msg.time  # Update current time based on the message's time
    if msg.type == "note_on" and msg.velocity > 0:
        if msg.note in MIDI_TO_KEY:
            key = MIDI_TO_KEY[msg.note]
            key_events_dict[current_time].append(('down', key))

    elif msg.type == "note_off" or (msg.type == "note_on" and msg.velocity == 0):
        if msg.note in MIDI_TO_KEY:
            key = MIDI_TO_KEY[msg.note]
            key_events_dict[current_time].append(('up', key))

# Sort events by current_time
sorted_key_events = sorted(key_events_dict.items())  # [(time, [(action, key), ...])]

# Save the events to a text file
with open("midi_events.txt", "w") as file:
    for event_time, actions in sorted_key_events:
        # Separate 'down' and 'up' events
        down_keys = [key for action, key in actions if action == 'down']
        up_keys = [key for action, key in actions if action == 'up']
        
        # Write the events in the desired format
        file.write(f"{event_time:.2f} down {' '.join(down_keys)} up {' '.join(up_keys)}\n")

print("MIDI events saved to 'midi_events.txt'")
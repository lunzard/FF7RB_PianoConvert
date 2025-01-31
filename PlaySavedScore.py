import pyautogui
import time

# Initialize an empty dictionary to store the events
events_dict = {}

# Read the file and populate the dictionary
with open("midi_events.txt", "r") as file:
    for line in file:
        # Initialize default values for "down" and "up" keys
        down_keys = []
        up_keys = []
        
        # Check if the line contains "down"
        if "down" in line:
            # Split the line using "down"
            down_part = line.strip().split("down")[1]  # Take the part after "down"
            # Extract "down" keys
            down_keys = down_part.strip().split("up")[0].strip().split()
        
        # Check if the line contains "up"
        if "up" in line:
            # Split the line using "up"
            up_part = line.strip().split("up")[1]  # Take the part after "up"
            # Extract "up" keys
            up_keys = up_part.strip().split()
        
        # Extract the timestamp (assume it's always the first part of the line)
        timestamp = float(line.strip().split()[0])
        
        # Store the events in the dictionary
        events_dict[timestamp] = {
            "down": down_keys,
            "up": up_keys
        }
    # events_dict = dict(sorted(events_dict.keys()))

print("Starting MIDI Playback in 3s...")
time.sleep(3)

# Track the start time to process events at correct times
start_time = time.time()

# Process the events based on their time
for event_time, events in events_dict.items():
    sleep_time = max(0, event_time - (time.time() - start_time))
    if sleep_time > 0:
        time.sleep(sleep_time)  # Wait until the correct time
    for key_up in events['up']:
         pyautogui.keyUp(key_up)
    for key_down in events['down']:
        pyautogui.keyDown(key_down)


print("MIDI Playback Complete.")

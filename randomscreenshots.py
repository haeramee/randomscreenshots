
# %% Run in terminal
# pip install pillow
# pip install pyinstaller
# pyinstaller --onefile --name screenshot randomscreenshots.py

# %%
import time
import random
import os
from datetime import datetime
from PIL import ImageGrab


# %%
# Configuration
NUM_SCREENSHOTS = 5                # 30 
DURATION_SECONDS = 300             # 2 * 60 * 60  # 2 hours
OUTPUT_DIR = "screenshots"

# Create output folder
os.makedirs(OUTPUT_DIR, exist_ok=True)

input(f"Press Enter to start capturing {NUM_SCREENSHOTS} screenshots over {DURATION_SECONDS // 60} minutes...")

# Pick 5 random times within the 1 minute window, sorted
times = sorted(random.sample(range(DURATION_SECONDS), NUM_SCREENSHOTS))

start = time.time()
print(f"Starting at {datetime.now().strftime('%H:%M:%S')}")
print(f"Will take {NUM_SCREENSHOTS} screenshots over {DURATION_SECONDS // 60} minutes.\n")

for i, t in enumerate(times, 1):
    # Sleep until the next scheduled moment
    wait = (start + t) - time.time()
    if wait > 0:
        time.sleep(wait)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(OUTPUT_DIR, f"screenshot_{i:02d}_{timestamp}.png")

    img = ImageGrab.grab(all_screens=True)  # capture all monitors
    img.save(path)
    print(f"[{i}/{NUM_SCREENSHOTS}] Saved {path}")

input("\nDone. Press Enter to exit.")


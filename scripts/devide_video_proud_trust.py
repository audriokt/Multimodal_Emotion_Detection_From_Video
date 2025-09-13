"""
Script to divide videos eith label proud and trust into separate directories.
the purpose of this script is to create custom dataset for this two emotions only.

"""

import os
import shutil

# === Konfigurasi Path ===
VIDEO_DIR = r"C:\Users\LEGION\OneDrive\Desktop\emotion_dataset\ori_videos"
PROUD_DIR = r"C:\Users\LEGION\OneDrive\Desktop\emotion_dataset\ori_videos\proud"
TRUST_DIR = r"C:\Users\LEGION\OneDrive\Desktop\emotion_dataset\ori_videos\trust"

os.makedirs(PROUD_DIR, exist_ok=True)
os.makedirs(TRUST_DIR, exist_ok=True)

def divide_videos():
    for filename in os.listdir(VIDEO_DIR):
        print(f"Found file: {filename}")
        if not filename.endswith(".mp4"):
            print("Skipped (not .mp4)")
            continue

        if "_proud" in filename or "_Proud" in filename:
            print("Detected proud label")
            shutil.move(os.path.join(VIDEO_DIR, filename), os.path.join(PROUD_DIR, filename))
        elif "_trust" in filename or "_Trust" in filename:
            print("Detected trust label")
            shutil.move(os.path.join(VIDEO_DIR, filename), os.path.join(TRUST_DIR, filename))
        else:
            print("No matching label found")

if __name__ == "__main__":
    divide_videos()


import subprocess
import os
import re
import tkinter as tk
from tkinter import filedialog
from datetime import datetime, timedelta
import os


def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path


def get_codec(input_file):
    try:
        command = [
            'ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=codec_name', '-of',
            'default=nokey=1:noprint_wrappers=1',
            input_file
        ]

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, _ = process.communicate()

        return output.strip()

    except Exception as e:
        print(f"An error occurred while retrieving codec: {e}")
        return None


def get_total_frames(input_file):
    try:
        print("Calculating total frames, this may take a while depending on the length of the video...\n")
        command = [
            'ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0', '-show_entries', 'stream=nb_frames',
            '-of', 'default=nokey=1:noprint_wrappers=1',
            input_file
        ]

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output, _ = process.communicate()

        return int(output.strip()) if output.strip().isdigit() else None

    except Exception as e:
        print(f"An error occurred while calculating total frames: {e}")
        return None


def convert_video(input_file, output_file, codec, total_frames):
    try:
        print("Starting video conversion...")
        print(f"Using codec: {codec}\n")
        command = [
            'ffmpeg', '-i', input_file,
            '-vcodec', codec,
            '-progress', '-', '-nostats',
            output_file
        ]

        process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True)

        frame_count = 0
        start_time = datetime.now()

        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break

            if 'frame=' in output:
                frame_info = re.search(r'frame=(\s*\d+)', output)
                if frame_info:
                    frame_count = int(frame_info.group(1))
                    os.system("cls")
                    print("Encoding...\n")
                    print(f"Frames processed: {frame_count}/{total_frames} ({100 * frame_count / total_frames:.2f}%)",
                          end='\r')

        process.wait()
        print("\nConversion completed.")

    except Exception as e:
        print(f"An error occurred during video conversion: {e}")


def main():
    input_file = select_file()
    if not input_file:
        print("No file selected.")
        return

    codec = get_codec(input_file)
    if codec is None:
        print("Failed to retrieve codec.")
        return

    total_frames = get_total_frames(input_file)
    if total_frames is None:
        print("Failed to retrieve total frames.")
        return

    print(f"\nTotal frames: {total_frames}")
    print(f"Codec of the input video: {codec}\n")

    print("Select the output format:")
    print("1. H.264")
    print("2. HEVC")
    print("3. VP9")
    print("4. AV1")
    print("5. MPEG-2")
    print("6. MPEG-4")
    print("7. AVI")
    choice = input("Enter the number of your choice: ")
    codecs = {
        "1": ("libx264", "mp4"),
        "2": ("libx265", "mp4"),
        "3": ("libvpx-vp9", "webm"),
        "4": ("libaom-av1", "mp4"),
        "5": ("mpeg2video", "mpeg"),
        "6": ("mpeg4", "avi"),
        "7": ("msmpeg4v2", "avi")
    }
    codec, extension = codecs.get(choice)

    if codec is None:
        print("Invalid choice.")
        return

    file_name, file_extension = os.path.splitext(os.path.basename(input_file))
    output_file = f"{file_name}-{codec}.{extension}"
    convert_video(input_file, output_file, codec, total_frames)

    input("Press Enter to exit...")


if __name__ == "__main__":
    main()

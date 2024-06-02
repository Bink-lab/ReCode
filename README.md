# UNFINISHED

Please note that this project is still unfinished and will get updates frequently

# Video Converter

This is a simple video converter script written in Python using the FFmpeg library.


## Description

This project is a very lightweight tool that allows you to easily encode ur videos in a different codec.

This project makes use of [Nuitka](https://nuitka.net) and [FFmpeg](ffmpeg.org) libraries.

### What is [Nuitka](https://nuitka.net)?
- Nuitka can be used to convert your python code into an executable (.exe), allthough this is very handy there are some issues with the library.
- Issues: When converting python code with any library the executable files can become very big due to the fact they need to compress all the used libraries to a small .exe file.

### What is FFmpeg?
- FFmpeg is the leading multimedia framework, able to decode, encode, transcode, mux, demux, stream, filter and play pretty much anything that humans and machines have created. It supports the most obscure ancient formats up to the cutting edge. No matter if they were designed by some standards committee, the community or a corporation. It is also highly portable: FFmpeg compiles, runs, and passes our testing infrastructure FATE across Linux, Mac OS X, Microsoft Windows, the BSDs, Solaris, etc. under a wide variety of build environments, machine architectures, and configurations.

### How?
- This program uses your CPU to first extract all the frames from the video, then encode the frames with a different codec.

## Features

- Supports multiple output formats: H.264, HEVC, VP9, AV1, MPEG-2, MPEG-4, AVI
- Real-time progress tracking during conversion
- Automatic retrieval of video codec and total frame count
- User-friendly interface for selecting input file and output format

## Dependencies

- [FFmpeg](https://www.ffmpeg.org/) - A complete, cross-platform solution to record, convert, and stream audio and video.
- [tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI (Graphical User Interface) package.
- [re](https://docs.python.org/3/library/re.html) - A built-in Python module for working with regular expressions.

## Usage

1. Install the needed tools
2. Run the script `video_converter.py` or run the executable file `video_converter.exe`
3. Select the input video file.
4. Choose the desired output format by entering the corresponding number.
5. Wait for the conversion process to complete.

## Installation (.exe)

1. Install FFmpeg. You can download it
2. Ur done! Run `video_converter.exe`
## Manual (.py)

1. Make sure you have Python installed on your system. You can download it from [here](https://www.python.org/downloads/).
2. Open a cmd prompt and type this command: `pip install -r requirements.txt`
3. Ur done! Run `video_converter.py`


# Author

This project is made by a Sidney (Bink-Lab), a single developer.

For more info check [this](github.com/bink-lab) page

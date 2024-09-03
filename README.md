# ShotcutChapters2OGM
Simple script used to convert chapters created in [Shotcut](https://www.shotcut.org/) to OGM format.
The output file is created only with [MKVToolNix](MKVToolNix) in mind. It has not been tested with other tools.

## Usage
ShotcutChapters2OGM.py [-h] [-o OUTPUT] [-f FPS] input

Converts chapters exported from Shotcut (txt) to OGM format (txt).

positional arguments:
  input                 Input file.

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file.
  -f FPS, --fps FPS     Video FPS (default=30).

## How to use with Shotcut and MKVToolNix

### Create chapters in Shotcut
Place markers where you would like your chapters and name them the way you like.
Then use File -> Export -> Markers as chapters...

### Add chapters to video in MKVToolNix
When muxing your video in MKV, go into the "Target" tab. In "Chapters", "Chapter file", select the file converted with ShotcutChapters2OGM.
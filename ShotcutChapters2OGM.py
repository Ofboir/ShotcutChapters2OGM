from pathlib import Path
import io
import re
import argparse

class ShotcutChapters2OGM:

    def __init__(self, inputfile, fps, outputfile):
        self.inputfile = Path(inputfile)
        if outputfile is None:
            self.outputfile = self.inputfile.with_suffix(".ogm.txt")
        else:
            self.outputfile = Path(outputfile)
        self.fps = fps
        self.chapternumber = 1
        self.convertfile()

    def convertfile(self):
        input = io.open(self.inputfile, mode="r", encoding="utf-8")

        self.outputfile.parent.mkdir(parents = True, exist_ok = True)
        output = io.open(self.outputfile, mode="w", encoding="ansi")

        while True:
            content=input.readline()
            if not content:
                break
            output.writelines(self.convertline(content))
            self.chapternumber += 1
            
        output.close()
        input.close()

        print("File written : {}".format(self.outputfile.resolve()))
    
    def convertline(self, text):
        converted = []

        # Input format : {Timestamp} {Title}
        match = re.match("([\d:]+)\s(.+)", text, re.UNICODE)
        if (match):
            # Timestamp format is HH:MM:SS:FF (FF = frames)
            timestamp = match.group(1)
            timestampmatch = re.fullmatch("(\d+:\d{2}):(\d{2}):(\d{2})", timestamp)
            if timestampmatch:
                hhmm = timestampmatch.group(1)
                seconds = int(timestampmatch.group(2))
                frames = int(timestampmatch.group(3))
                output_seconds = seconds + frames / self.fps
                timestamp = "{}:{:012.9f}".format(hhmm, output_seconds)
            else:
                # Timestamp format is HH:MM:SS
                timestampmatch = re.fullmatch("\d{2}:\d{2}:\d{2}", timestamp)
                if timestampmatch:
                    timestamp = "{}.{:09d}".format(timestamp, 0)
                else:
                    # Timestamp format is HH:MM
                    timestampmatch = re.fullmatch("\d{2}:\d{2}", timestamp)
                    if timestampmatch:
                        timestamp = "{}:{:012.9f}".format(timestamp, 0)

            chapternumber_as_string = f'{self.chapternumber:02d}'
            converted.append("CHAPTER{}={}".format(chapternumber_as_string, timestamp))
            converted.append("\n")
            converted.append("CHAPTER{}NAME={}".format(chapternumber_as_string, match.group(2)))
            converted.append("\n")
        else:
            print("Unknown format: {}".format(text))

        return converted

###

print("ShotcutChapters2OGM")

# Arguments
parser = argparse.ArgumentParser(description="Converts chapters exported from Shotcut (txt) to OGM format (txt).")
parser.add_argument("-o", "--output", help="Output file.", type=str, required=False)
parser.add_argument("-f", "--fps", help="Video FPS (default=30).", type=int, default=30)
parser.add_argument("input", help="Input file.", type=str)
args = parser.parse_args()

ShotcutChapters2OGM(args.input, args.fps, args.output)
"""dts2flac uses python and ffmpeg to conert dts files to flac for use in kodi"""
import os, glob, re

# grab a list of .dts files from the current directory (note: case insensitive)
paths = glob.glob("*.dts")

# for each "input" .dts file, create a output string with .flac; which also informs ffmpeg of the type to convert
for input in paths:
	output = re.sub("(.+)\.dts$", "\g<1>.flac", input, flags=re.IGNORECASE)
	exectuteString:str = 'ffmpeg -i "{}" "{}"'.format(input, output)
	print("\n" + exectuteString) # prints out the ffmpeg converstion string
	os.system(exectuteString)

# wait for user confirmation
os.system("pause")

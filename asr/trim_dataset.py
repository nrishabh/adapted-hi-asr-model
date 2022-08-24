import os
import sys
import string
import random

# USAGE: python trim_dataset.py FOLDER_NAME
# EXAMPLE: python trim_dataset.py train
# EXAMPLE: python trim_dataset.py eval

AUDIO_FOLDER = os.getcwd()+r"/audio/"+sys.argv[1]+r"/"
DATA_FOLDER = os.getcwd()+r"/data/"+sys.argv[1]+r"/"

audio_files = os.listdir(AUDIO_FOLDER)
transcription_files = os.listdir(DATA_FOLDER+r"preTrimmed/")

print("Trimming dataset based on available audio files...")
for filename in transcription_files:
    data = list()
    
    with open(DATA_FOLDER+r"/preTrimmed/"+filename, mode='r', encoding='utf-8-sig') as f:
        for line in f.read().split("\n"):
            if (line[:21]+".wav") in audio_files:
                data.append(line)

    with open(DATA_FOLDER+filename, mode='w', encoding='utf-8-sig') as f:
        for line in sorted(data):
            f.write(line+"\n")
    
    print("DONE: "+filename)

with open(DATA_FOLDER+"wav.scp", mode='w', encoding='utf-8-sig') as f:
    for filename in sorted(audio_files):
        f.write(filename[:-4]+"\t"+AUDIO_FOLDER+filename+"\n")

print("DONE: wav.scp")
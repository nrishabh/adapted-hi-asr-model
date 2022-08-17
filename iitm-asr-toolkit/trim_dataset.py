import os
import sys

# USAGE: python trim_dataset.py FOLDER_NAME
# EXAMPLE: python trim_dataset.py train
# EXAMPLE: python trim_dataset.py eval

AUDIO_FOLDER = os.getcwd()+r"/audio/"+sys.argv[1]+r"/"
DATA_FOLDER = os.getcwd()+r"/data/"+sys.argv[1]+r"/"

audio_files = os.listdir(AUDIO_FOLDER)
transcription_files = os.listdir(DATA_FOLDER)
excluded_files = ["README", "wav.scp"]

print("Trimming dataset based on available audio files...")
for filename in transcription_files:
    if filename not in excluded_files:
        data = list()
        
        with open(DATA_FOLDER+filename, mode='r', encoding='utf-8-sig') as f:
            for line in f.read().split("\n"):
                if (line[:21]+".wav") in audio_files:
                    data.append(line)
        
        os.rename(DATA_FOLDER+filename, DATA_FOLDER+"preTrimmed_"+filename)

        with open(DATA_FOLDER+filename, mode='w', encoding='utf-8-sig') as f:
            for line in data[:-1]:
                f.write(line+"\n")
            f.write(data[-1])
        
        print("DONE: "+filename)

os.rename(DATA_FOLDER+"wav.scp", DATA_FOLDER+"preTrimmed_"+"wav.scp")

with open(DATA_FOLDER+"wav.scp", mode='w', encoding='utf-8-sig') as f:
    for filename in audio_files:
        f.write(filename[:-4]+"\t"+AUDIO_FOLDER+filename+"\n")

print("DONE: wav.scp")
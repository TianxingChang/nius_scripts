import sys
import subprocess
import json
# import time # for testing
import os
# import multiprocessing
# from concurrent.futures import ProcessPoolExecutor

# jsons =[f"split_300h/split_{i}.json" for i in range(1,20+1)]   # requires a new version of python

# output file directory and json file location
output_dir = "processed_wav/"
input_json = f"split_300h/split_{sys.argv[1]}.json"


def get_total_seg_num(json_file):
    index = 1
    with open(json_file) as f:
        data = json.load(f)
    for audio in data["audios"]:
        path = audio["path"]
        for segment in audio["segments"]:
            index += 1
    return index
    

def audio_convert(json_file, seg_num):
    index = 1 

    with open(json_file) as f:
        data = json.load(f)

    for audio in data["audios"]:
        path = audio["path"]
        for segment in audio["segments"]:
            begin_time = segment["begin_time"]
            end_time = segment["end_time"]
            sid = segment["sid"]

            segment_name = "{}.wav".format(sid)
            output_path = output_dir + segment_name
            if os.path.exists(output_path):
                print("Segment {} already exists at {}".format(index, output_path))
                index += 1
                continue
            
            subprocess.call(["ffmpeg", "-i", path, "-ss", str(begin_time), "-to", str(end_time),"-loglevel", "quiet", "-ac", "1", "-ar", "16000", output_path])
            
            print("pid-",os.getpid()," "f"=================<<<<<<<< {index}/{seg_num} >>>>>>>>=================")
            index += 1
    print(f"split_300h/split_{sys.argv[1]}.json split done :-)")


# def multi_process():
#     with ProcessPoolExecutor(max_workers=20) as executor:
#         executor.map(audio_convert, jsons)


if __name__ == "__main__":
    # multi_process()
    seg_num = get_total_seg_num(input_json)
    audio_convert(input_json, seg_num)

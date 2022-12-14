import os
import glob
import pandas as pd
import torch
import csv
from datetime import datetime
from datetime import timedelta
import calendar
import time


def convert_files(uid):
    # files
    lst = glob.glob("./input/UID{}/*.3gp".format(uid))
    make_dirs("./output/UID{}".format(uid))

    for file in lst:
        outputs = file.replace("input", "output")
        # convert wav to mp3
        os.system(f"""ffmpeg -i {file} -acodec pcm_u8 -ar 22050 {outputs[:-4]}.wav""")


def make_dirs(path):
    try:
        os.makedirs(path)

    except OSError:
        if not os.path.isdir(path):
            raise


def vggish(wav_file):
    model = torch.hub.load('harritaylor/torchvggish', 'vggish')
    model.eval()

    tensor_result = model.forward(wav_file)
    # print(tensor_result.shape) # [62, 128]

    result = tensor_result.tolist()  # list
    return result


def feature_extraction(uid):

    # files
    lst = glob.glob("./output/UID{}/*.wav".format(uid))
    result = pd.DataFrame()

    for outputs in lst:
        # mel spectogram
        wav_file = outputs[:-4] + ".wav"
        features = vggish(wav_file)

        info = outputs[:-4].split('\\')[1]
        uid = info.split('_')[1]

        # Unix TimeStamp
        stime = info.split('_')[2] + ' ' + info.split('_')[3]

        # KST to UTC
        temp = datetime.strptime(stime, "%Y-%m-%d %H-%M-%S.%f")
        temp = temp - timedelta(hours=9)

        # datetime to timestamp
        # unixtime = time.mktime(temp.timetuple()) * 1e3 + temp.microsecond / 1e3
        unixtime = calendar.timegm(temp.timetuple()) * 1e3 + temp.microsecond / 1e3 # GMT
        print(stime,' to ', temp, 'GMT to ', unixtime)

        data = {
            'Timestamp': unixtime,
            'uid': uid,
            'features': [features]
        }
        df = pd.DataFrame(data)
        result = pd.concat([result, df], ignore_index=True)
        # print (data)

    return result

def save_to_csv():

    for uid in range(1, 11):
        convert_files(uid)

    output = pd.DataFrame()

    for uid in range(1, 11):
        data = feature_extraction(uid)
        output = pd.concat([output, data], ignore_index=True)
        print(output)

    output.to_csv('voice_data.csv')


if __name__ == "__main__":
    save_to_csv()

    sample = pd.read_csv('voice_data.csv')
    print(sample.size)
    print(sample.shape)

  
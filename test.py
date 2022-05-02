import soundfile as sf
import IPython
import math
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

def pitch(input_signal, input_sr, output_path, pitch_factor):
    signal_pitch = librosa.effects.pitch_shift(input_signal, 1, pitch_factor) # sampling rate and pitch factor
    sf.write(output_path, signal_pitch, input_sr)

def pitch_run(file_list, file_path, output_path, pitch_factor):
    import librosa
    for i in file_list:
        try:
            signal, sr = librosa.load(file_path+i)
            pitch(signal, sr, output_path+i, pitch_factor)
        except Exception as e:
            print(e)
            continue

import os
# hard pitch
list = [1400, 1800]
file_path = "C:\\Users\\hk_le\\OneDrive\\Transfer\\cs7643finalp\\augment_pre\\wav\\"
wav_files = [f for f in os.listdir(file_path) if f[0]=='t']
#wav_files = [os.listdir(file_path)[0]]
output_path = "C:\\Users\\hk_le\\devwork\\CS7643\\updata\\rawdata\\hard_pitch\\wav\\"
pitch_factor = 14
pitch_run(wav_files, file_path, output_path, pitch_factor)

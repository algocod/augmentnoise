import math
#https://medium.com/analytics-vidhya/adding-noise-to-audio-clips-5d8cee24ccb8
#https://github.com/sleekEagle/audio_processing
import librosa
import matplotlib.pyplot as plt
import numpy as np
signal, sr = librosa.load("./mevoice.wav");
plt.plot(signal)
plt.show()

# Signal to Noise Ration SNR = log(RMS^2 signal/RMS^2noise)
# one can set the SNR to a desired ratio, lower value will mean weak augmentation while higher value will lead to higher augmentation.
SNR=.8
RMS_s = math.sqrt(np.mean(signal**2))
RMS_n =math.sqrt(RMS_s**2/(pow(10,SNR/10)))
# Additive White Noise Gaussian , generation noise with Standard deviation  =1 , the mean of the Gaussian noise is zero .
STD_n = RMS_n
noise = np.random.normal(0, STD_n,signal.shape[0]) # STD of .05 had Amplitude range of .2 and less which is the ampltitude range of the original sound
# hence this noise makes sense else a STD=1 with Ampltitude=4 overshadows the original sound.
# But using hte STD_n formula makes it relative to the sound
plt.plot(noise)
plt.show()
# analyze the frequency content
signal_noise = signal + noise
plt.plot(signal_noise)
plt.show()

adnoise, sr = librosa.load("./addednoise.wav");
# Add actual noise like background noise or something
RMS_an = math.sqrt(RMS_s ** 2 / (pow(10, SNR / 10)))

# current RMS of noise
RMS_n_current = math.sqrt(np.mean(adnoise ** 2))
adnoise = adnoise * (RMS_n / RMS_n_current)
adnoise.resize(signal.shape)
plt.plot(adnoise)
plt.show()
signal_adnoise = signal + adnoise
#signal[:len(adnoise)] += adnoise
plt.plot(signal_adnoise)
plt.show()
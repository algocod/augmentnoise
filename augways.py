import librosa
import matplotlib.pyplot as plt
import numpy as np
#https://medium.com/@makcedward/data-augmentation-for-audio-76912b01fdf6

signal, sr = librosa.load("./mevoice.wav");
plt.plot(signal)
#plt.show()

noise_factor=.01
non_gaussian_noise = np.random.randn(len(signal))
non_gaussian_signal = signal + noise_factor * non_gaussian_noise
#plt.plot(non_gaussian_signal)
#plt.show()

signal_pitch = librosa.effects.pitch_shift(signal, 1, 8) # sampling rate and pitch factor
plt.plot(signal_pitch)
plt.show()

signal_speed = librosa.effects.time_stretch(signal, .5) # speed factor of the sound , slowing with < 1 and speeding with > 1
plt.plot(signal_speed)
plt.show()

def manipulate(data, sampling_rate, shift_max, shift_direction):
    shift = np.random.randint(sampling_rate * shift_max)
    if shift_direction == 'right':
        shift = -shift
    elif shift_direction == 'both':
        direction = np.random.randint(0, 2)
        if direction == 1:
            shift = -shift
    augmented_data = np.roll(data, shift)
    # Set to silence for heading/ tailing
    if shift > 0:
        augmented_data[:shift] = 0
    else:
        augmented_data[shift:] = 0
    return augmented_data

signal_roll = manipulate(signal, 1, 2, 'right')
#plt.plot(signal_roll)
#plt.show()

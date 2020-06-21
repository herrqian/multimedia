from winsound import PlaySound, SND_FILENAME as FILE_FLAG

import numpy as np
import scipy.io.wavfile as wav


# Input:        inputSignal:    Eingangssignal
#               nDeleteFreq:    Anzahl der zu löschenden Frequenzen
#               fftLength:      Länge der FFT
#
# Output:       outputSignal:   Ausgangssignal
#
# Nützliche Befehle/Collections/Libs: numpy, ftt, scipy.io.wavfile,...
def m_fft(inputSignal, nDeleteFreq, fftLength):
    outputSignal = []
    signals_block = np.array_split(inputSignal, fftLength)
    for signal in signals_block:
        freq = np.fft.fft(signal)
        abs_arr = np.abs(freq)
        for counter in range(0, nDeleteFreq):
            current_min = np.min(abs_arr)
            index_to_delete = np.where(abs_arr == current_min)[0][0]
            abs_arr[index_to_delete] = np.inf
            freq[index_to_delete] = 0
        outputSignal.append(np.fft.ifft(freq))

    return np.concatenate(outputSignal)


def play_sound(filename):
    PlaySound(filename, FILE_FLAG)


def main():
    play_sound("ceremony.wav")
    rate, input_signal = wav.read("ceremony.wav")
    print(rate)
    print(input_signal)
    output = m_fft(input_signal, 20, 500)
    print(output)
    n_output = np.real(output).astype(np.int16)
    print(n_output)
    wav.write("new_ceremony.wav", rate, n_output)
    play_sound('new_ceremony.wav')


if __name__ == "__main__":
    main()
# from wave import open
# from winsound import PlaySound, SND_FILENAME as FILE_FLAG
# from struct import pack, unpack
# from numpy import fft, floor
# import matplotlib.pyplot as plt
#
# BLOCK_SIZE = 512
# params = ()
# frames = []
# filter_frames = []
#
#
# def read_file(filename):
#     global params, frames
#
#     wave_file = open(filename)
#     params = wave_file.getparams()
#     # print(params)
#
#     for i in range(wave_file.getnframes()):
#         frame = wave_file.readframes(1)
#         frames.append(unpack('<h', frame)[0])
#     # print(wave_file.readframes(0))
#     # print(len(frames))
#
#     wave_file.close()
#
#
# def fourier():
#     global frames
#
#     number_blocks = int((len(frames) / BLOCK_SIZE))
#
#     for block in range(number_blocks):
#         fourier = fft.fft(frames[block * BLOCK_SIZE: (block + 1) * BLOCK_SIZE])
#
#         delete_minmum(fourier)
#
#         ifourier(fourier)
#
#
# def delete_minmum(fourier):
#     # for i in range(BLOCK_SIZE):
#     # minimum = min(fourier)
#     for k in range(len(fourier)):
#         if fourier[k] == min(fourier):
#             fourier[k] = 0
#             break
#
#     return fourier
#
#
# def ifourier(fourier):
#     global filter_frames
#
#     ifourier = fft.ifft(fourier)
#     # print(len(ifourier))
#
#     for i in range(len(ifourier)):
#         tmp = pack('<i', int(floor(ifourier[i].real)))
#         filter_frames.append(tmp)
#
#
# def write_file(filename):
#     global params
#     wave_file = open(filename, 'w')
#     wave_file.setparams(params)
#
#     for filter_frame in filter_frames:
#         wave_file.writeframesraw(filter_frame)
#
#     wave_file.close()
#
#
# def play_sound(filename):
#     PlaySound(filename, FILE_FLAG)
#
#
# if __name__ == "__main__":
#     # filename = 'ceremony.wav'
#     # output = 'output.wav'
#     filename = 'itu_male1.wav'
#     output = 'output_male1.wav'
#
#     print("Spiele Ursprungs .wav File ab")
#     play_sound(filename)
#
#     read_file(filename)
#     print("Datei eingelesen")
#
#     print("Fouriertransformation")
#     fourier()
#
#     print("Schreibe neues .wav File")
#     write_file(output)
#
#     print("Spiele neues .wav File ab")
#     play_sound(output)
#
# # Datei einlesen, in Blöcke einteilen, (sortieren), Minmum suchen, auf 0 setzen, wieder zusammensetzen

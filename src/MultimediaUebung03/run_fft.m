function [out]=run_fft(in,nd,fft_length)

% function [out]=run_fft(in,nd,fft_length)
%
% in            :     Eingangssignal
% out           :     Ausgangssignal
% nd            :     Anzahl der zu l�schenden Frequenzen
% fft_length    :     L�nge der FFT
%
% n�tzliche Matlab-Befehle: fft, ifft, specgram(in,512,fs)
% abs, real
% wavread, wavwrite
% sound, soundsc
% sort, min, max

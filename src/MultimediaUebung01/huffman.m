function [c,h,w]=huffman(P)
% function [c,h,w]=huffman(P)
% 
% Huffman-Codierung
%
% p :   Auftrittswahrscheinlichkeiten
% c :   Code als Cell-Array
% h :   Entropie
% w :   mittlere Codewortl�nge
% 
% F�r den Testvektor
% P=[0.05 0.03 0.17 0.23 0.01 0.32 0.19]
% ergibt sich h=2.3378 und w=2.39.

% n�tzliche Matlab-Befehle: struct, sort



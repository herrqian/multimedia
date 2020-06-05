% Test-String
t = '/WED/WE/WEE/WEB/WET'

% Codierung
[s,table]=lzw_encode(t);
disp(s)

% Ausgabe der Codier-Tabelle
strvcat(table{257:end})

% Decodierung
[tt,table]=lzw_decode(s);
disp(tt)

% Ausgabe der Decodier-Tabelle
strvcat(table{257:end})

% Test
isOK = strcmp(t,tt)

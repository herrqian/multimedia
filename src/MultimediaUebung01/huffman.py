import math
import heapq


# Diese Funktion liest eine Textdatei im ASCII-Format
# und berechnet die relative Häufigkeit der einzelnen
# Zeichen.
#
# Input:        fname       :   Dateiname
#
# Output:       probs       :   Vektor mit den relativen Häufigkeiten
#               characters  :   Vektor mit den aufgetretenen Zeichen
#
# nützliche Tools, Collections, Befehle: open, close, read, replace, sort, Counter, numpy, matplotlib
# HINWEIS: Datenstrukturen des Skripts können abgeändert werden
#          (z.B. statt Listen Dictionarys oder Counter Objekte verwenden)
def read_text(fname):
    # probs = []
    # characters = []
    my_dict = {}
    with open(fname) as f:
        read_data = f.read()

    for s in read_data:
        if s not in my_dict:
            my_dict[s] = 1
        else:
            my_dict[s] += 1

    my_dict = {k: v / len(read_data) for k, v in my_dict.items()}

    return my_dict


# Huffman - Codierung
#
# Input:    probs           :   Auftrittswahrscheinlichkeiten
#
# Output:   code            :   Code Tabelle
#           entropy         :   Entropie
#           meanLength      :   mittlere Codewortlänge
#
# Für den Testvektor
# P = [0.05, 0.03, 0.17, 0.23, 0.01, 0.32, 0.19]
# A = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# ergibt sich entrpy = 2.3378 und meanLength = 2.39.

def huffman(probs):
    codes = {}
    entropy = 0
    meanLength = 0
    probs = {k: v for k, v in sorted(probs.items(), key=lambda item: item[1])}

    # entropy rechnen
    for k, v in probs.items():
        ig = math.log(1 / v, 2)
        entropy += v * ig
    #print('entropy is', entropy)

    hq = []
    for k, v in probs.items():
        hq.append(Huffmannode(v, k))
    heapq.heapify(hq)

    while len(hq) > 1:
        n1 = heapq.heappop(hq)
        n2 = heapq.heappop(hq)
        n3 = Huffmannode(n1.prob + n2.prob)
        n3.left = n1
        n3.right = n2
        heapq.heappush(hq, n3)

    hq[0].encoding('', codes)

    length = 0
    for k, v in codes.items():
        length += len(v) * probs[k]
    meanLength = length

    return codes, entropy, meanLength


class Huffmannode:

    def __init__(self, prob, symbol=None):
        self.symbol = symbol
        self.prob = prob
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.prob < other.prob

    def encoding(self, code, table):
        if self.left is None and self.right is None:
            table[self.symbol] = code
        else:
            self.left.encoding(code + '0', table)
            self.right.encoding(code + '1', table)


def main():
    fname = 'midsummer.txt'
    # probs, characters = read_text(fname)
    probs = read_text(fname)
    print(probs)
    codes, entropy, meanLength = huffman(probs)
    print('code table is:')
    for k,v in codes.items():
        if k == '\n':
            print('\\n', ':', v)
        else:
            print(k, ':', v)
    print('entropy is', entropy)
    print('meanlength is', meanLength)


if __name__ == '__main__':
    main()

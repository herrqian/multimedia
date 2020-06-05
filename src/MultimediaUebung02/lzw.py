# Diese Funktion liest eine Sequenz von Zeichen und codiert diese nach dem LZW Verfahren
#
# Input:        input:          Zeichensequenz
#
# Output:       output:         codierte Zeichensequenz
#               encodeDict:     Wörterbuch
def lzwEncode(input, alpha_dict: dict):
    output = ""
    encodeDict = alpha_dict
    i = 0
    s = input[i]
    while i < len(input) - 1:
        j = i + 1
        c = input[j]
        values = encodeDict.values()
        if condition_check(values, s + c):
            s += c
        else:
            output += str(get_key(encodeDict, s)) + " "
            encodeDict[len(encodeDict) + 1] = s + c
            s = c
        i = j

    output += str(get_key(encodeDict, s)) + " "

    return output, encodeDict


def condition_check(a_list, s):
    for i in a_list:
        if i.startswith(s):
            return True
    return False


def get_key(a_dict: dict, value):
    for k, v in a_dict.items():
        if v == value:
            return k


# Diese Funktion decodiert eine LZW-codierte Zeichensequenz
#
# Input:        input:          codierte Zeichensequenz
#
# Output:       output:         decodierte Zeichensequenz
#               decodeDict:     Wörterbuch
def lzwDecode(input, alpha_dict: dict):
    output = ""
    decodeDict = alpha_dict
    input_vec = input.strip().split(" ")
    i = 0
    output += decodeDict[int(input_vec[i])]
    while i < len(input_vec) - 1:
        j = i + 1
        if contain_key(decodeDict, int(input_vec[j])):
            #decodeDict[len(decodeDict.keys()) + 1] = decodeDict[int(input_vec[i])] + decodeDict[int(input_vec[j])][0]
            output += decodeDict[int(input_vec[j])]
        else:
            decodeDict[len(decodeDict.keys()) + 1] = decodeDict[int(input_vec[i])] + decodeDict[int(input_vec[i])][0]
            output += decodeDict[int(input_vec[i])] + decodeDict[int(input_vec[i])][0]
        i = j

    return output, decodeDict


def contain_key(my_dict, key):
    for k in my_dict.keys():
        if k == key:
            return True
    return False


def main():
    input_data = '/WED/WE/WEE/WEB/WET'
    #input_data = "wabba_wabba_wabba_wabba_woo_woo_woo"
    init_dict = {}
    index = 1
    for c in input_data:
        if c not in init_dict.values():
            init_dict[index] = c
            index += 1
        else:
            continue
    #init_dict = {1: '_', 2: 'a', 3: 'b', 4: 'o', 5: 'w'}
    #print(init_dict)
    test_string = "wabba_wabba_wabba_wabba_woo_woo_woo"
    compressed, enDict = lzwEncode(input_data, init_dict)
    print(enDict)
    print(compressed)
    #test_input = '5 2 3 3 2 1 6 8 10 12 9 11 7 16 5 4 4 11 21 23 4'
    # test_dict = {1:'_',2:'a',3:'b',4:'o',5:'w'}
    decompressed, deDict = lzwDecode(compressed, init_dict)
    print(deDict)
    print(decompressed)


if __name__ == "__main__":
    main()

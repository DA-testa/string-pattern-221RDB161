# python3
#Linards Tomass Beķeris 221RDB161

def read_input():
    text = input()
    patt = ""
    strn = ""

    if "F" in text:
        file = open("./tests/06", "r")
        text = file.read()
        text = text.split('\n')
        patt = text[0]
        strn = text[1]

    elif "I" in text:
        patt = input()
        strn = input()

    patt = patt.strip()
    strn = strn.strip()
    return (patt, strn)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(patt, text):
    indeksi = []
    for i in range(len(text)):
        if text[i] == patt[0] and len(patt) + i <= len(text):
            atrast = True
            for j in range(len(patt)):
                if text[i+j] != patt[j]:
                    atrast = False
            if atrast:
                indeksi.append(i)
    return indeksi

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
from cProfile import label
from goto import with_goto

class WordFrequency:
    def __init__(self, word, amount):
        self.word = word
        self.amount = amount

@with_goto
def main():
    # reading file
    string = []
    with open('text.txt', 'r') as file: string = list(file.read())

    # count file length
    stringLength = 0
    label .countStringLength
    try:
        string[stringLength]
        stringLength += 1
        goto .countStringLength
    except IndexError:
        pass

    # dividing file string into words
    words = [0]*(stringLength//3)
    words = []
    word = [0]*20
    lastSymbolIndex = 0
    i = 0

    label .dividingFileStringInWords
    if string[i] != ' ' and string[i] != '\n':
        word[lastSymbolIndex] = string[i]
        lastSymbolIndex += 1
    else:
        wordLength = 0
        label .countWordLength
        if word[wordLength]!= 0:
            wordLength += 1
            goto .countWordLength
        if wordLength > 3:
            tempWordIndex = 0
            tempWord = ""
            label .createTempWord
            tempWord += word[tempWordIndex]
            tempWordIndex += 1
            if tempWordIndex < wordLength:
                goto .createTempWord
            words.append(tempWord)

        word = [0]*20
        lastSymbolIndex = 0

    i += 1
    if i < stringLength:
        goto .dividingFileStringInWords

    

    print(words)

main()
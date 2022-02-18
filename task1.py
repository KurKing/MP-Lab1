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
    if string[i] != '\n' and string[i] != ' ' and string[i] != '.' and string[i] != ',' and string[i] != '?' and string[i] != '!':
        word[lastSymbolIndex] = string[i]
        lastSymbolIndex += 1
        if i == stringLength - 1:
            goto .addWordToTheList
    else:
        label .addWordToTheList
        wordLength = 0
        label .countWordLength
        if word[wordLength]!= 0:
            wordLength += 1
            goto .countWordLength

        if wordLength > 3:
            tempWordIndex = 0
            tempWord = ""
            label .createTempWord
            asciiCharToAd = ord(word[tempWordIndex])
            if(asciiCharToAd>64 and asciiCharToAd<91):
                asciiCharToAd+=32
            tempWord += chr(asciiCharToAd)
            tempWordIndex += 1
            if tempWordIndex < wordLength:
                goto .createTempWord
            words.append(tempWord)
        word = [0]*20
        lastSymbolIndex = 0

    i += 1
    if i < stringLength:
        goto .dividingFileStringInWords

    # count amount of words
    wordsAmount = 0
    label .countWordsAmount
    try:
        words[wordsAmount]
        wordsAmount += 1
        goto .countWordsAmount
    except IndexError:
        pass

    # wordsFrequencyArray generating
    wordsFrequencyArray = [0]*wordsAmount
    wordIndex = 0
    i = 0
    label .wordsFrequencyArrayGenerating
    if wordsFrequencyArray[i] == 0:
        wordsFrequencyArray[i] = WordFrequency(words[wordIndex], 1)
        wordIndex += 1
        if wordIndex >= wordsAmount:
            goto .endOfWordsFrequencyArrayGenerating
        i = 0
        goto .wordsFrequencyArrayGenerating
    else:
        if wordsFrequencyArray[i].word == words[wordIndex]:
            wordsFrequencyArray[i].amount += 1
            wordIndex += 1
            if wordIndex >= wordsAmount:
                goto .endOfWordsFrequencyArrayGenerating
            i = 0
            goto .wordsFrequencyArrayGenerating

        i += 1
        if i < wordsAmount:
            goto .wordsFrequencyArrayGenerating

    label .endOfWordsFrequencyArrayGenerating

    # removing zeros from array
    wordsFrequencyAmount = 0
    label .countWordsFrequency
    if wordsFrequencyArray[wordsFrequencyAmount] != 0:
        wordsFrequencyAmount += 1
        goto .countWordsFrequency

    cleanWordsFrequencyArray = [0]*wordsFrequencyAmount
    i = 0
    label .generateCleanWordsFrequencyArray
    cleanWordsFrequencyArray[i] = wordsFrequencyArray[i]
    i += 1
    if i < wordsFrequencyAmount:
        goto .generateCleanWordsFrequencyArray

    # sorting array
    i = 0
    label .bubbleSortFirstStage
    j = 0
    label .bubbleSortSecondStage
    if cleanWordsFrequencyArray[j].amount < cleanWordsFrequencyArray[j+1].amount:
        cleanWordsFrequencyArray[j], cleanWordsFrequencyArray[j+1] = cleanWordsFrequencyArray[j+1], cleanWordsFrequencyArray[j]
    j += 1
    if j < wordsFrequencyAmount-1-i:
        goto .bubbleSortSecondStage
    i += 1
    if i < wordsFrequencyAmount-1:
        goto .bubbleSortFirstStage

    # generating final string
    finalString = f"{cleanWordsFrequencyArray[0].word} - {cleanWordsFrequencyArray[0].amount}"
    index = 1
    label .generateFinalString
    finalString += f"\n{cleanWordsFrequencyArray[index].word} - {cleanWordsFrequencyArray[index].amount}"
    index += 1
    if index < wordsFrequencyAmount:
        goto .generateFinalString

    # printing result
    print(finalString)

main()
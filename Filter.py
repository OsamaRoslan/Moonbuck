# String matching algorithm - Trie Algorithm
from xmlrpc.server import list_public_methods
import array as arr
import numpy as np



class TrieNode:

    # in order to create an instance of trie node, insert the letter, eg: TrieNode("*"
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_the_end_of_word = False


class Trie:
    def __init__(self):  # creating an instance of TrieNode
        self.root = TrieNode("*")

    def add(self, word):  # a function that accepts a word and
        # also imports 'self' in this function
        curr_node = self.root
        for ch in word:
            if ch not in curr_node.children:  # if ch is not in the current node, then add it
                curr_node.children[ch] = TrieNode(ch)  # create a new trie node
            curr_node = curr_node.children[ch]
        curr_node.is_the_end_of_word = True  # when the for loop has come to an end

    def search(self, word):  # a function that searches the pattern
        if word == "":
            return True
        curr_node = self.root
        for ch in word:
            if ch not in curr_node.children:
                return False  # terminate the for loop since the pattern does not exist
            curr_node = curr_node.children[ch]
        return curr_node.is_the_end_of_word  # returns true since we have reached the end, and all words exists, thus pattern exists


# Read file
def readFile(extracted, fileName):
    with open(f'Data File\\{fileName}.txt', 'r', encoding="utf-8") as file:
        # reading each line
        for line in file:
            # reading each word
            for word in line.split(','):
                # displaying the words
                extracted.append(word)


def readPositiveWords(positiveWords):
    with open('Database\\positiveWords.txt', 'r') as file:

        # reading each line
        for line in file:

            # reading each word
            for word in line.split(','):
                # displaying the words
                positiveWords.append(word)


def readNegativeWords(negativeWords):
    with open('Database\\negativeWords.txt', 'r') as file:

        # reading each line
        for line in file:

            # reading each word
            for word in line.split(','):
                # displaying the words
                negativeWords.append(word)


def readNeutralWords(neutralWords):
    with open('Database\\neutralWords.txt', 'r') as file:

        # reading each line
        for line in file:

            # reading each word
            for word in line.split(','):
                # displaying the words
                neutralWords.append(word)


def readStopWords(stopWords):
    with open('Database\\stopWords.txt', 'r') as file:

        # reading each line
        for line in file:

            # reading each word
            for word in line.split(','):
                # displaying the words
                stopWords.append(word)


def convert(lst):
    return (lst[0].split())


def magic(lst):
    restructured = []
    for Line in lst:
        words = Line.split(" ")
        for i in range(len(words)):
            restructured.append(words[i].replace("\n", ""))

    return restructured

totalPosWord = arr.array("i", [])
totalNegWord = arr.array("i", [])
totalNeuWord = arr.array("i", [])
totalStopWord = arr.array("i", [])
PosWord = 0
NegWord = 0
NeuWord = 0
stopWords = 0

# Driver code
# Call function to read from text file


for y in range(25):
    fileName = "DATA" + str(y + 1)
    extracted = []
    positiveWords = []
    negativeWords = []
    neutralWords = []
    stopWords = []
    newAyat = []

    readFile(extracted, fileName)
    readPositiveWords(positiveWords)
    readNegativeWords(negativeWords)
    readNeutralWords(neutralWords)
    readStopWords(stopWords)

    for i in range(len(positiveWords)):
        positiveWords[i] = (positiveWords[i].replace(" ", ""))

    trieStop = Trie()
    wordsOnly = magic(extracted)

    positiveFound = []
    negativeFound = []
    neutralFound = []
    stopFound = []

    newSentence = []

    # Add stop words into the TRIE
    for i in range(len(stopWords)):
        trieStop.add(stopWords[i].lower())

    # Remove stop word
    for i in range(len(wordsOnly)):
        if trieStop.search(wordsOnly[i].lower()):
            stopFound.append(wordsOnly[i])
        else:
            newSentence.append(wordsOnly[i])

    trie = Trie()
    trieNegative = Trie()
    trieNeutral = Trie()

    # Add positive words into the TRIE
    for i in range(len(positiveWords)):
        trie.add(positiveWords[i].lower())

    # Add negative words into the TRIE
    for i in range(len(negativeWords)):
        trieNegative.add(negativeWords[i].lower())

    # Add neutral words into the TRIE
    for i in range(len(neutralWords)):
        trieNeutral.add(neutralWords[i].lower())

    for i in range(len(wordsOnly)):
        if trieNegative.search(wordsOnly[i].lower()):
            negativeFound.append(wordsOnly[i])

    for i in range(len(wordsOnly)):
        if trieNegative.search(wordsOnly[i].lower()):
            negativeFound.append(wordsOnly[i])

    # Search the word from the list of positive, negative and neutral words
    for i in range(len(newSentence)):
        if trie.search(newSentence[i].lower()):
            positiveFound.append(newSentence[i])

        elif trieNegative.search(newSentence[i].lower()):
            negativeFound.append(newSentence[i])

        elif trieNeutral.search(newSentence[i].lower()):
            neutralFound.append(newSentence[i])

    while ("" in negativeFound):
        negativeFound.remove("")

    # Write the positive words found into a text file
    f = open("List\\listPositive.txt", "a")

    for i in range(len(positiveFound)):
        f.write(positiveFound[i] + ",")

    f.close()

    # Write the negative words found into a text file
    f = open("List\\listNegative.txt", "a")

    for i in range(len(negativeFound)):
        f.write(negativeFound[i] + ",")

    f.close()

    # Write the neutral words found into a text file
    f = open("List\\listNeutral.txt", "a")

    for i in range(len(neutralFound)):
        f.write(neutralFound[i] + ",")

    if y < 5:
        PosWord += len(positiveFound)
        NegWord += len(negativeFound)
        NeuWord += len(neutralFound)
        # stopWords += len(stopFound)
        if y == 4:
            totalPosWord.append(PosWord)
            totalNegWord.append(NegWord)
            totalNeuWord.append(NeuWord)
            #totalStopWord.append(stopWords)
            PosWord = 0
            NegWord = 0
            NeuWord = 0
            #stopWords = 0

    elif y < 10:
        PosWord += len(positiveFound)
        NegWord += len(negativeFound)
        NeuWord += len(neutralFound)
        #stopWords += len(stopFound)
        if y == 9:
            totalPosWord.append(PosWord)
            totalNegWord.append(NegWord)
            totalNeuWord.append(NeuWord)
            #totalStopWord.append(stopWords)
            PosWord = 0
            NegWord = 0
            NeuWord = 0
            #stopWords = 0

    elif y < 15:
        PosWord += len(positiveFound)
        NegWord += len(negativeFound)
        NeuWord += len(neutralFound)
        #stopWords += len(stopFound)
        if y == 14:
            totalPosWord.append(PosWord)
            totalNegWord.append(NegWord)
            totalNeuWord.append(NeuWord)
            #totalStopWord.append(stopWords)
            PosWord = 0
            NegWord = 0
            NeuWord = 0
            #stopWords = 0

    elif y < 20:
        PosWord += len(positiveFound)
        NegWord += len(negativeFound)
        NeuWord += len(neutralFound)
        #stopWords += len(stopFound)
        if y == 19:
            totalPosWord.append(PosWord)
            totalNegWord.append(NegWord)
            totalNeuWord.append(NeuWord)
            #totalStopWord.append(stopWords)
            PosWord = 0
            NegWord = 0
            NeuWord = 0
            #stopWords = 0
    else:
        PosWord += len(positiveFound)
        NegWord += len(negativeFound)
        NeuWord += len(neutralFound)
        #stopWords += len(stopFound)
        if y == 24:
            totalPosWord.append(PosWord)
            totalNegWord.append(NegWord)
            totalNeuWord.append(NeuWord)
            #totalStopWord.append(stopWords)
            PosWord = 0
            NegWord = 0
            NeuWord = 0
            #stopWords = 0

    f.close()

Countries = ["USA", "JAPAN", "UAE", "CHINA", "ENGLAND"]
alltype = [totalPosWord,totalNegWord,totalNeuWord]
type_word = ["Positive", "Negative", "Neutral", "Stop"]


if __name__ == "__main__":
    import plotly.express as px

    #bar chart for all variable
    fig = px.histogram(data_frame=None, x=Countries, y=alltype, title="Histogram of Countries over Word Count")
    newnames = {'wide_variable_0':'Positive words', 'wide_variable_1': 'Negative words', 'wide_variable_2': 'Neutral words', 'wide_variable_3': 'Stop words'}
    fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                          legendgroup = newnames[t.name],
                                          hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                          )
                       )

    #fig.show()

    #bubble chart
    import plotly.graph_objects as go
    fig_bubble = go.Figure(data=[go.Scatter(
        x=Countries, y=alltype,
        mode='markers',
        marker = dict(
            color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',
                   'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
            opacity=[1, 0.8, 0.6, 0.4],
            size=[90, 80, 40, 60, 30],
        )
    )])

    # fig_bubble.show()


    #pie chart
    import plotly.graph_objects as go

    #positive word percentage of all country
    labels = ['USA','JAPAN','UAE','CHINA', 'ENGLAND']
    values = [totalPosWord[0], totalPosWord[1], totalPosWord[2], totalPosWord[3], totalPosWord[4]]
    fig2 = go.Figure(data=[go.Pie(labels=labels, values=values)])
    #fig2.show()


    #type of word for USA
    labels = ['Positive Words','Negative Word','Neutral Word']
    values = [totalPosWord[0], totalNegWord[0], totalNeuWord[0]]
    fig_USA = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig_USA.update_layout(title_text='USA all type of words', title_x=0.5)
    #fig_USA.show()

    #type of word for JAPAN
    labels = ['Positive Words','Negative Word','Neutral Word']
    values = [totalPosWord[1], totalNegWord[1], totalNeuWord[1]]
    fig_JPN = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig_JPN.update_layout(title_text='JAPAN all type of words', title_x=0.5)
    #fig_JPN.show()

    #type of word for UAE
    labels = ['Positive Words','Negative Word','Neutral Word']
    values = [totalPosWord[2], totalNegWord[2], totalNeuWord[2]]
    fig_UAE = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig_UAE.update_layout(title_text='UAE all type of words', title_x=0.5)
    #fig_UAE.show()

    #type of word for CHINA
    labels = ['Positive Words','Negative Word','Neutral Word']
    values = [totalPosWord[3], totalNegWord[3], totalNeuWord[3]]
    fig_CHN = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig_CHN.update_layout(title_text='CHINA all type of words', title_x=0.5)
    #fig_CHN.show()

    #type of word for ENGlAND
    labels = ['Positive Words','Negative Word','Neutral Word']
    values = [totalPosWord[4], totalNegWord[4], totalNeuWord[4]]
    fig_ENG = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig_ENG.update_layout(title_text='ENGLAND all type of words', title_x=0.5)
    #fig_ENG.show()
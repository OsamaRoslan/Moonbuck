# String matching algorithm - Trie Algorithm
from xmlrpc.server import list_public_methods


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
def readFile(extracted):
    with open('Data File\\USA1.txt', 'r') as file:

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
            restructured.append(words[i].replace("\n",""))

    return restructured

# Driver code
# Call function to read from text file
extracted = []
positiveWords = []
negativeWords = []
neutralWords = []
stopWords = []
newAyat = []

readFile(extracted)
readPositiveWords(positiveWords)
readNegativeWords(negativeWords)
readNeutralWords(neutralWords)
readStopWords(stopWords)
for i in range(len(positiveWords)):
    positiveWords[i] = (positiveWords[i].replace(" ", ""))

trieStop = Trie()
wordsOnly = magic(extracted)
print(wordsOnly)

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

while("" in negativeFound) :
    negativeFound.remove("")



print("Sentence: ", newSentence, "\n")
print("Positive: ", positiveFound)
print("Negative: ", negativeFound)
print("Neutral: ", neutralFound)

# Count Word
print("Positive Word: ", len(positiveFound))
print("Negative Word: ", len(negativeFound))
print("Neutral Word: ", len(neutralFound))

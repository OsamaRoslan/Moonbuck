


#######################   Calculate the probability ##########################################

from Filter import totalPosWord, totalNegWord, totalNeuWord, Countries
from dataOfCountries import USA, JPN, UAE, CHN, ENG


totalPosWordAll = sum(totalPosWord)
totalWord = sum(totalPosWord) + sum(totalNeuWord) + sum(totalNegWord)

prob_totalPosWord = totalPosWordAll/totalWord
print("Probability of positive words in 25 articles =", prob_totalPosWord)

totalPosWordAll_eachCountry = [totalPosWord[0], totalPosWord[1],totalPosWord[2],totalPosWord[3],totalPosWord[4]]

totalWord_eachCountry = [(totalPosWord[0] + totalNeuWord[0] + totalNegWord[0]),
                         (totalPosWord[1] + totalNeuWord[1] + totalNegWord[1]),
                         (totalPosWord[2] + totalNeuWord[2] + totalNegWord[2]),
                         (totalPosWord[3] + totalNeuWord[3] + totalNegWord[3]),
                         (totalPosWord[4] + totalNeuWord[4] + totalNegWord[4])]

prob_PosWords = [0] * len(Countries)

for i in range(len(Countries)):
    prob_PosWords[i] = totalPosWordAll_eachCountry[i] / totalWord_eachCountry[i]

print("\nProbability Positive Words for Each Country")
for i in range(len(Countries)):
    print(Countries[i], "=", prob_PosWords[i])

shortestDist = [len(USA.shops) - 1, len(JPN.shops) - 1, len(UAE.shops) - 1, len(CHN.shops) - 1, len(ENG.shops) - 1]

prob_shortestDist = [0] * len(Countries)

print("\nProbability Shortest Distance for Each Country")
for i in range(len(Countries)):
    prob_shortestDist[i] = shortestDist[i] / sum(shortestDist)

#To calculate the probability of shortest distance of each country

for i in range(len(Countries)):
    print(Countries[i], "=", prob_shortestDist[i])

#To calculate the probability of shortest distance of each country

highestAvePosWords = max(prob_PosWords)
lowestAveShortestDist = min(prob_shortestDist)

#To calculate the probability of the shortest distance of each country

prob = [0] * len(Countries)

for i in range(len(Countries)):
    prob[i] = (prob_PosWords[i] / sum(prob_PosWords)) * (1 - prob_shortestDist[i])

#To calculate the probability of recommended to expansion of each country

print("\nProbability of Recommended Countries to have expansion")
for i in range(len(Countries)):
    print(Countries[i], "=", prob[i])

def bubbleSort(A):
    for i in range(len(A)):
        for j in range(1, len(A)):
            if A[j - 1] < A[j]:
                temp = A[j - 1]
                A[j - 1] = A[j]
                A[j] = temp
            j=+1
        i=-1

bubbleSort(prob)

print("\nTop 5 Countries")
for i in range(len(Countries)):
    print(format(prob[i], ".3f"))

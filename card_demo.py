"""
@author: Keon Hayes
"""

#Imports the Card object
from card import Card
from fisher_yates import Fisher_Yates
from merge_sort import Merge_Sort

"""
Demonstrates the use of the Card object
"""

#List of Values
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

#List of Suits
suits = ["C", "D", "H", "S"]

#List of Cards
cards = []

index = 0 #Variable to keep track of where in the list the next card should go
for j in range(0, len(values)) : #Iterates through each value
    for k in range(0, len(suits)) : #Iterates through each suit
        cards.insert(index, Card(values[j], suits[k], j, k)) #Creates a Card object at the current index with the current value and suit
        index += 1 #Increments to the next index
print("Array created.")

for i in range(0, len(cards)) :
    print("i: ", i, " ", cards[i].get_value(), " - ", cards[i].get_suit(), sep="")

Fisher_Yates.shuffle(cards, len(cards))
print("Array shuffled.")

for i in range(0, len(cards)) :
    print(cards[i].get_value(), " - ", cards[i].get_suit(), sep="") #The value and suit of each card is printed to show that the cards were shuffled

Merge_Sort.merge_sort()





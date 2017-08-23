#!/usr/bin/python3

# A program that merges a list of sorted lists into one sorted list

from sys import stdin
from itertools import repeat

def merge(decks):
    numberOfLists = len(decks)
    heap = [] # The heap of nodes to sort
    
    result = "" # In this problem we only need to store the string of symbols,
                # normally this would be a list of the result values.
                
    indices = [] # A list of indices, one for each list
                  
    for i in range(0, numberOfLists):
        indices.append(0)
        if len(heap) == 0:
            # The heap is empty, so add the first element
            heap.append((i, decks[i][0]))
        else:
            addToHeap(heap, decks, i, indices)
    
    while len(heap) > 0: # While we have cards left to merge
        card = heap.pop(0) # Pop the card with the lowest value
        result += card[1][1]
        list = card[0] # Get the list number this card is from
        indices[list] += 1 # Proceed to the next card in this list
        if len(decks[list]) > indices[list]:
            # If this list contains more cards, add the next to the heap
            addToHeap(heap, decks, list, indices)
    
    return result

def addToHeap(heap, decks, list, indices):
    # Add the next heap element at the right position,
    # so that the heap is always sorted
    wasInserted = False
    for j in range(0, len(heap)):
        if heap[j][1][0] > decks[list][indices[list]][0]:
            heap.insert(j, (list, decks[list][indices[list]]))
            wasInserted = True
            break
    if not wasInserted:
        # If the element was not lower than the others, append it.
        heap.append((list, decks[list][indices[list]]))
                
def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))


if __name__ == "__main__":
    main()
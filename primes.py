from time import time
from Prime import Prime
from threading import Thread
from readWrite import importOptions, importCSV, exportPrimes


def sortPrimes(li: list[Prime], byComp: bool = False)->list[Prime]:
    if byComp:
        li.sort(key=lambda p : p._comp)
    else:
        li.sort(key=lambda p : p._prime)
    
    return li
    

def movePrime(list: list[Prime], p: Prime) -> list[Prime]:
    # For smaller primes, don't use binary search to save time
    if p._prime < 40:
        for i in reversed(range(len(list))):
            if list[i]._comp > p._comp:
                list.insert(i+1, p)
                break
            elif list[i] == list[0]:
                list.insert(0, p)
        return list
   
    index = binarySearch(list, 0, len(primes)-1, p._comp)
    # my guess is that this is the problem i was worried about: 
    # the prime prediction thingy isn't a solid lower bound, and it finally missed, causing the binary search to go out of bounds, returning none for the insert
    
    list.insert(index, p)
    return list

def binarySearch(list: list[Prime], low: int, high: int, x: int):
    while low <= high:
        mid = low + (high - low) // 2
        if list[mid]._comp == x:
            return mid
        elif list[mid]._comp > x:
            low = mid + 1
        else:
            high = mid - 1
    return low

def movePrimes(li: list[Prime], primes: list[Prime]) -> list[Prime]:
    """Move a list of primes back into the list"""

    needBinary: list[Prime] = []
    
    #Check for front cases, add rest of primes to new list
    for p in primes:

        if p._prime < 40:
            for i in reversed(range(len(li))):
                if li[i]._comp > p._comp:
                    li.insert(i+1, p)
                    break
                elif li[i] == li[0]:
                    li.insert(0, p)

        else:
            needBinary.append(p)
            
    
    #Multi-Binary Search for the rest
    if len(needBinary) != 0:

        #Sort primes for efficient inserts
        sortPrimes(needBinary, True)

        #send composites into function
        nbComps = [p._comp for p in needBinary]
        inds = binarySearchMany(li, 0, len(li)-1, nbComps)
        
        #do the insert
        for i in range(len(inds)-1, -1, -1):
            li.insert(inds[i], needBinary[i])
    
    return li
        

def binarySearchMany(list: list[Prime], low: int, high: int, X: list[int]):
    """Search for many indeces for insertion"""
    found = [None]*len(X) #found indeces

    #create, start, and wait for end of starting thread
    start = Thread(target=bSearchThread, args = (list, low, high, X, found))  
    start.start()
    start.join()
    return found


def bSearchThread(list: list[Prime], low: int, high: int, X: list[int], found: list[int]):
    """Threading function for Binary Search"""
    #Add checking once list gets too narrow
    if low < high:
        for i in range(len(X)):
            if list[low] == X[i]:
                found[i] = low
            elif list[high] > X[i] and list[low] < X[i]:
                found[i] = low
        
        return None


    #check if anything found at midpoint
    mid = low + (high-low)//2
    midComp = list[mid]._comp
    for i in range(len(X)):
        if X[i] == midComp:
            found[i] = mid
    
    goLeft = False
    goRight = False


    #Check which sides need further attention
    for i in range(len(X)):

        if found[i]==None: #if not found

            if X[i] < midComp: #if right of mid
                if X[i] >= list[high]._comp: #if in range

                    goRight = True
                    if goLeft:
                        break

            elif X[i] <= list[low]._comp: #elif (left of mid) in range
                goLeft = True 
                if goRight:
                    break
    
    #Thread for whichever sides need threading
    if goLeft:

        left = Thread(target=bSearchThread, args = (list, low, mid-1, X, found))
        left.start()

        if goRight:
            right = Thread(target=bSearchThread, args = (list, mid+1, high, X, found))
            right.start()
            right.join()

        left.join()

    elif goRight:

        right = Thread(target=bSearchThread, args = (list, mid+1, high, X, found))
        right.start()
        right.join()



if __name__ == "__main__":
    # Option to import previous prime values
    importPath = importOptions()
    if importPath != None:
        # Prime calculating range will begin at the max of file range
        lowRange = int(importPath.split("_")[1].split(".")[0])
        # If even, make odd so we can skip evens later
        if lowRange % 2 == 0:
            lowRange += 1
        primes = importCSV(importPath)
    else:
        # Start with 3 in the primes listaskImport
        # Skip 2 because we're skipping all even numbers
        primes = [Prime(3, 9)]
        lowRange = 5

    # The largest number you want to calculate to
    max = 3000000
    start = time()
    try:
        for num in range(lowRange, max, 2): 
            more = True
            foundFactor = False
            toBeMoved: list[Prime] = [] #list of primes that need moved back into the list
            
            # Using 'more' for loop control allows us to find multiple prime factors per number
            while more:
                if num == primes[-1]._comp: # NOT PRIME
                    primes[-1].add_comp()
                    toBeMoved.append(primes.pop())
                    # p = primes.pop()
                    # primes = movePrime(primes, p)
                    foundFactor = True
                elif not foundFactor: # PRIME
                    # f.write(f"{num}\n")
                    primes.insert(0, Prime(num, num**2))
                    more = False
                else: # NO MORE PRIME FACTORS
                    more = False

            #Insert increased composites back into the list
            if len(toBeMoved) == 1:
                primes = movePrime(primes, toBeMoved[0])
            elif len(toBeMoved) > 1:
                primes = movePrimes(primes, toBeMoved)

        print(f"Ran in {time()-start} seconds")
    except KeyboardInterrupt:
        print("\nSearch interrupted...")
    exportPrimes(primes, num)

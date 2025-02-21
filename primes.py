from time import time
from Prime import Prime
from readWrite import importOptions, importCSV, exportPrimes

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
            
            # Using 'more' for loop control allows us to find multiple prime factors per number
            while more:
                if num == primes[-1]._comp: # NOT PRIME
                    primes[-1].add_comp()
                    p = primes.pop()
                    primes = movePrime(primes, p)
                    foundFactor = True
                elif not foundFactor: # PRIME
                    # f.write(f"{num}\n")
                    primes.insert(0, Prime(num, num**2))
                    more = False
                else: # NO MORE PRIME FACTORS
                    more = False
        print(f"Ran in {time()-start} seconds")
    except KeyboardInterrupt:
        print("\nSearch interrupted...")
    exportPrimes(primes, num)
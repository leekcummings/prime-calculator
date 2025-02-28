# ---------------------------------------------------------------------------- #
#                                 Binary Search                                #
# ---------------------------------------------------------------------------- #

# ----------------------------------- Notes ---------------------------------- #

# This was initially the fastest solution we would come up with, until using a hash table
# Used binary search to insert a prime number into the list of primes

from time import time
from Prime import Prime

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
    # The largest number you want to calculate to
    max = 1000000
    start = time()
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
                primes.insert(0, Prime(num, num**2))
                more = False
            else: # NO MORE PRIME FACTORS
                more = False

    print(f"Ran in {time()-start} seconds")
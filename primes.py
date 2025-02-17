from time import time
from math import ceil, log
from Prime import Prime

def movePrime(list: list[Prime], p: Prime) -> list[Prime]:
    if p._prime < 40:
        for i in reversed(range(len(list))):
            if list[i]._comp > p._comp:
                list.insert(i+1, p)
                break
            elif list[i] == list[0]:
                list.insert(0, p)
        return list
    
    # low, high = predictRange(list, p, 64)
    # index = binarySearch(list, low, high, p._comp)

    index = binarySearch(list, 0, len(list)-1, p._comp)

    list.insert(index, p)

    return list




def binarySearch(list: list[Prime], low: int, high: int, x: int):
    while low <= high:
        mid = low + (high - low) // 2
        # Check if x is present at mid
        if list[mid]._comp == x:
            return mid
        # If x is greater, ignore left half
        elif list[mid]._comp > x:
            low = mid + 1
        # If x is smaller, ignore right half
        else:
            high = mid - 1
    return low

if __name__ == "__main__":
    # Start with 3 in the primes list
    # Skip 2 because we're skipping all even numbers
    primes = [Prime(3, 9)]

    # The largest number you want to calculate to
    max = 1000000
    #jump = 16

    f = open("primes.txt", "w")
    f.write("2\n")
    t = time()

    for num in range(5, max+1, 2): 
        more = True
        foundFactor = False
        #if num//jump > 50:
        #    jump *=2
        
        #print(*primes)
        # Using 'more' for loop control allows us to find multiple prime factors per number
        while more:
            if num == primes[-1]._comp: # NOT PRIME
                #print(f"{num} IS NOT PRIME")
                #print(f"Found factor {primes[-1]}")
                primes[-1].add_comp()
                p = primes.pop()
                primes = movePrime(primes, p)
                foundFactor = True
            elif not foundFactor: # PRIME
                #print(f"{num} IS PRIME")
                f.write(f"{num}\n")
                primes.insert(0, Prime(num, num**2))
                more = False
            else: # NO MORE PRIME FACTORS
                more = False
    
    print(f"Ran in {time()-t} seconds")
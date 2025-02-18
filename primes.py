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
    # Start with 3 in the primes list
    # Skip 2 because we're skipping all even numbers
    primes = [Prime(3, 9)]

    # The largest number you want to calculate to
    max = 10000

    f = open("primes.txt", "w")
    f.write("2\n")
    t = time()

    start = time()
    
    for num in range(5, max+1, 2): 
        more = True
        foundFactor = False
        
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
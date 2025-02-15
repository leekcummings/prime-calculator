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
    
    low, high = predictRange(list, p, 16)
    if low != high:
        index = binarySearch(list, low, high, p._comp)
    list.insert(index, p)
    return list

def predictRange(li: list[Prime], p:Prime, jump:int)->tuple[int, int]:
    prime = p._prime
    comp = p._comp
    max = len(li)-1
    min = max-ceil(0.5*prime/log(prime))
    if min < 0:
        min = 0
    elif min > max:
        min = max

    if li[min]._comp == comp:
        return min, min
    
    elif li[min]._comp < comp:
        while li[min]._comp < comp:
            if min-jump <=0:
                return 0, min
            min -= jump
        if li[min]._comp == comp:
            return min, min
        return min+1, min+jump-1
    
    else:
        while li[min]._comp > comp:
            if min+jump>=max:
                return min, max
            min+=jump
        if li[min]._comp == comp:
            return min, min
        return min-jump+1, min-1

    



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
    return mid

if __name__ == "__main__":
    # Start with 3 in the primes list
    # Skip 2 because we're skipping all even numbers
    primes = [Prime(3, 9)]

    # The largest number you want to calculate to
    max = 1000000

    f = open("primes.txt", "w")
    f.write("2\n")

    for num in range(5, max+1, 2): 
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
                f.write(f"{num}\n")
                primes.insert(0, Prime(num, 3*num))
                more = False
            else: # NO MORE PRIME FACTORS
                more = False
# ---------------------------------------------------------------------------- #
#                                 Linear Search                                #
# ---------------------------------------------------------------------------- #

# ----------------------------------- Notes ---------------------------------- #

# The first version that didn't do modular division
# Not fast--very quickly improved in v2

from time import time
from Prime import Prime

def movePrime(list: list[Prime], p: Prime) -> list[Prime]:
    # For smaller primes, don't use binary search to save time
    for i in reversed(range(len(list))):
        if list[i]._comp > p._comp:
            list.insert(i+1, p)
            break
        elif list[i] == list[0]:
            list.insert(0, p)
    return list

if __name__ == "__main__":
    primes = [Prime(3, 9)]
    lowRange = 5

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
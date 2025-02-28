from time import time
from Prime import Prime
from readWrite import importOptions, importCSV, exportPrimes

def movePrime(dict: dict, p: Prime) -> dict:
    while True:   
        if dict.get(p._comp, None) == None:
            dict[p._comp] = p
            return dict
        else:
            p.add_comp()
            
def startup():
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
        primes = {}
        p = Prime(5, 25)
        primes[p._comp] = p
        lowRange = 5
    return (primes, lowRange)

if __name__ == "__main__":
    (primes, lowRange) = startup()
    # The largest number you want to calculate to
    max = 1000000
    start = time()
    try:
        for num in range(lowRange, max, 2): # Skip even numbers for efficiency
            if primes.get(num, None) != None: # If number is composite
                p: Prime = primes[num]
                primes.pop(p._comp)
                p.add_comp() # Find next composite for prime
                primes = movePrime(primes, p) # Move to vacant location
            else: # If number is prime
                primes = movePrime(primes, Prime(num, num**2))

        print(f"Ran in {time()-start} seconds")
    except KeyboardInterrupt:
        # To allow for partial data export
        print("\nSearch interrupted...")
    exportPrimes(primes, num)

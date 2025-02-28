import os
import re

from Prime import Prime

def importOptions():
    """Import a .csv with a name of "primes_###.csv".
    If multiple importable files exist, offer to import one by one until file is selected."""
    for f in os.listdir():
        match = re.search(r"^primes_.+\.csv", f)
        
        if match != None:
            choice = None
            while choice not in ["y", "n"]:
                choice = input(f"Do you want to import file \"{match.group(0)}\" (y/n)? ").lower()
            if choice == "y":
                return (match.group(0))
    # If no files match regex, return None
    return None

def importCSV(path: str) -> dict:
    primes = {}
    with open(path, "r") as f:
        for line in f:
            prime = line.strip().split(",")
            primes[int(prime[1])] = Prime(int(prime[0]), int(prime[1]))
    f.close()
    return primes

def exportPrimes(primes: list[Prime], max: int):
    """Export current dictionary of Prime objects into an importable .csv format.
    The file format is {prime number},{next composite number}"""
    choice = None
    while choice not in ["y", "n"]:
        choice = input(f"Do you want to export objects as .csv (y/n)? ").lower()
    if choice == "y":
        with open(f"primes_{max}.csv", "w") as f:
            for p in primes:
                p = primes[p]
                f.write(f"{p._prime},{p._comp}\n")
        f.close()
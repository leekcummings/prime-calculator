# Prime Calculator

I want to figure out a way to calculate a bunch of primes, without having to do a bunch of modular division.

I did it.

## Current Version

### 🥇 [v5: Hash Table](primes.py)

Sometimes simplicity wins. The magnificent hash table was a very good choice for storing the primes we're working with. This is by far the fastest algorithm here, and extremely simple. Gold medal.

## Different Versions

> [!NOTE]
> To run previous versions of this program move into main directory.

### v0: Modular Division

This was the original! The inspiration! The worst one here! Not linked because I lost my code months ago!!

### [v1: Linear Search](./previous/v1_linearSearch.py)

I don't know who thought it would be a good idea to do a linear search
on an array of hundends of primes, but it happened. Would not recommend.

### 🥈 [v2: Binary Search](./previous/v2_bSearch.py)

This is more like it! Binary search was significantly faster than linear search (who would have guessed?). Compared to the final version, this one earns a silver medal.

### [v3: Index Prediction](./previous/v3_indexPrediction.py)

To save time on binary searching, [@cmfeltgood](https://github.com/cmfeltgood) tried to predict a better range to do the searching in using some fun math. It could closely predict the index where the prime would be inserted, but sometimes was thousands of indexes off, which is why we didn't continue on this version.

### 🥉 [v4: Threaded Binary Search](./previous/v4_bSearchThreads.py)

This was a fun one. [@cmfeltgood](https://github.com/cmfeltgood) once again tried to do something insane by implementing threading to speed up the binary search process. Any time multiple primes have the same composite number, multiple searches began simultaneously and each prime was moved to a new location. It ended up being slightly slower than v2, but I'll give it bronze.
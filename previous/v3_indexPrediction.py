# ---------------------------------------------------------------------------- #
#                    Index prediction using ~fancy calculus~                   #
# ---------------------------------------------------------------------------- #

# ----------------------------------- Notes ---------------------------------- #

#lmao worth a shot, makes it take longer tho
#idea was to get a much closer range using #primes ~= p/log(p), predicting a sum of inverse primes would maybe make this faster
#log(log(max))-log(log(p))? log(log(max)/log(p))? (using integration and prime density)

from Prime import Prime
from math import ceil, log

def predictRange(li: list[Prime], p:Prime, jump:int)->tuple[int, int]:
    comp = p._comp
    max = len(li)-1

    #The initial guess, based on probabilities of prime occurences
    guess = max-ceil(0.5*p._prime/log(p._prime))-ceil(p._prime*(log(log(li[0]._prime))-log(log(p._prime))))

    #Fit guess to range
    if guess < 0:
        guess = 0
    elif guess > max:
        guess = max

    #If guess was correct, return it exactly
    if li[guess]._comp == comp:
        return guess, guess
    
    #If the guess was too far left / too big, go right until it finds a range or an exact value
    elif li[guess]._comp < comp:
        while li[guess]._comp < comp:
            if guess-jump <=0:
                return 0, guess
            guess -= jump
        if li[guess]._comp == comp:
            return guess, guess
        return guess+1, guess+jump-1
    
    #Otherwise go left
    else:
        while li[guess]._comp > comp:
            if guess+jump>=max:
                return guess, max
            guess+=jump
        if li[guess]._comp == comp:
            return guess, guess
        return guess-jump+1, guess-1
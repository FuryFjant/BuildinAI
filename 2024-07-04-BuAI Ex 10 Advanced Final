import numpy as np

p1 = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]   # normal
p2 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]   # loaded

def roll(loaded):
    if loaded:
        print("rolling a loaded die")
        p = p2
    else:
        print("rolling a normal die")
        p = p1

    # roll the dice 10 times
    # add 1 to get dice rolls from 1 to 6 instead of 0 to 5
    sequence = np.random.choice(6, size=10, p=p) + 1 
    for roll in sequence:
        print("rolled %d" % roll)
        
    return sequence

def bayes(sequence):
    odds = 1.0           # start with odds 1:1
    for roll in sequence:
        r = 3 # Loaded die probability is 0.5 or 50% normal die probabilit is 1/6 r=P(six|loaded) / P(six|normal) = 0.5 / (1/6) = 3
        if roll == 6:
            odds = odds * r        # edit here to update the odds
    print(odds)
    if odds > 242: # one below the odds valu if hit 50% of the time 1*3*3*3*3*3 = 243
        return True
    else:
        return False

sequence = roll(False)
if bayes(sequence):
    print("I think loaded")
else:
    print("I think normal")
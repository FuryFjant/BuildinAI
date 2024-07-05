def flip(n):
    odds = 1.0         # start with 50% chance of the magic coin, which is the same as odds = 1:1
    for i in range(n):
        r = 2 # r = P(heads | magic) / P(heads | normal) = 1 / 0.5 = 2
        odds = odds * r        
    print(odds)

n = 10
flip(n)
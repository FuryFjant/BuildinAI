import math
import random             	# just for generating random mountains                                 	 

# generate random mountains                                                                               	 
w = [random.random()/3, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/6.)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]
h[0] = 0.0; h[99] = 0.0

def climb(x, h):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:
        summit = True         # stop unless there's a way up
        
        if h[x + 1] > h[x] or h[x - 1] > h[x]:
            if h[x + 1] > h[x - 1]:
                x = x + 1
            elif h[x - 1] > h[x + 1]:
                x = x - 1
            else:
                x = random.choice([x + 1, x - 1])
            summit = False
        else:
               for i in range(x-5, x+6):
                  if h[i] > h[x]:
                        h[x] = h[i]
                        summit = False
                        break      
    return x


def main(h):

    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)
   
    print("Venla started at %d and got to %d" % (x0, x))
    return x0, x

main(h)
#Example solution
#
#def climb(x):
#    # keep climbing until we've found a summit
#    summit = False
#
#    # edit here
#    while not summit:
#        summit = True
#        for x_new in range(max(0, x-5), min(99, x+5)):
#           if h[x_new] > h[x]:
#               x = x_new         # here is higher, go here 
#               summit = False    # and keep going
#   return x
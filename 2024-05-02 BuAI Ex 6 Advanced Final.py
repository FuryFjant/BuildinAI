import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import cm

N = 100     # size of the problem is N x N                                      
steps = 3000    # total number of iterations                                        
tracks = 50

# generate a landscape with multiple local optima                                          
def generator(x, y, x0=0.0, y0=0.0):
    return np.sin((x/N-x0)*np.pi)+np.sin((y/N-y0)*np.pi)+\
        .07*np.cos(12*(x/N-x0)*np.pi)+.07*np.cos(12*(y/N-y0)*np.pi)

x0 = np.random.random() - 0.5
y0 = np.random.random() - 0.5
h = np.fromfunction(np.vectorize(generator), (N, N), x0=x0, y0=y0, dtype=int)
peak_x, peak_y = np.unravel_index(np.argmax(h), h.shape)

# starting points                                                               
x = np.random.randint(0, N, tracks)
y = np.random.randint(0, N, tracks)

def main():
    global x
    global y

    for step in range(steps):
        T = max(0, ((steps - step)/steps)**3-.005) #From the hints text in the exercise
        # add a temperature schedule here
        #T = 1 commented out from the original code
        if T==0: #mamaging the temperature to be 0 and cause a division by zero error
            return x[i],y[i]
        # update solutions on each search track                                     
        for i in range(tracks):
            # try a new solution near the current one                               
            x_new = np.random.randint(max(0, x[i]-2), min(N, x[i]+2+1))
            y_new = np.random.randint(max(0, y[i]-2), min(N, y[i]+2+1))
            S_old = h[x[i], y[i]]
            S_new = h[x_new, y_new]

            if S_new > S_old:                                                        # if new score is better...
                x[i], y[i] = x_new, y_new                                            # accept the new score       
            else:                                                                    # if not
                if random.random()<(np.exp(-(S_old-S_new)/T)):                       # check if probability is greater than random num (0-1.0) meaning simulated annealing as in exercise 5
                    x[i], y[i] = x_new, y_new                                                       # accept the new score that is worse
        print(sum([x[j] == peak_x and y[j] == peak_y for j in range(tracks)]))                          # Number of tracks that found the peak
main()    

# plot the landscape and the search tracks, copied from others code and not used in the code entered for the exercise test
plt.xlim(0, N-1)
plt.ylim(0, N-1)
plt.imshow(h, cmap=cm.gist_earth)
plt.scatter([peak_y], [peak_x], color='red', marker='+', s=100)

for j in range(tracks):

    c = cm.tab20(j/tracks)    # use different colors for different tracks 
    plt.scatter([y[j]], [x[j]], color=c, s=20)

plt.show()
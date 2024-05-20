portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km
D = [
    [0,8943,8019,3652,10545],
    [8943,0,2619,6317,2078],
    [8019,2619,0,5836,4939],
    [3652,6317,5836,0,7825],
    [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)
co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them
    
def assign_smallest():
    smallest = 1000000
    return smallest
    
def assign_bestroute ():
    bestroute = [0, 0, 0, 0, 0]
    return bestroute
    
def emissions(route):
    route_emission = sum(D[route[i]][route[i+1]] for i in range(len(route)-1))*co2
    return route_emission
    
def permutations(route,ports):
    #print(ports)
    #print (route)
    # Print case: if the ports list is empty print route list with names
    if len(ports) == 0:
        #Calculate the route emission
        route_emission = emissions(route)
        #Print the route 
        #print(' '.join([portnames[i] for i in route]), f'{route_emission:.1f} kg')
        #Check if the route emission is smaller than the smallest emission
        global smallest
        if route_emission < smallest:
            smallest = route_emission
            global bestroute
            bestroute = route
            
    # Recursive case: for each element in the ports list, generate permutations
    # of the remaining elements and append the current element to each permutation
    else:
        for i in ports:
            new_route = route +[i]
            remaining_ports = ports[:]
            remaining_ports.remove(i)
            permutations(new_route, remaining_ports)
smallest = assign_smallest()
bestroute = assign_bestroute()

def main():    
    # This will start the recursion with 0 ("PAN") as the first stop        
    permutations([0],list(range(1, len(portnames))))
    
    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

# Call the main function
main()
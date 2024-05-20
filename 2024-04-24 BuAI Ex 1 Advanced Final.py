def main():
    
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    def permutations(route,ports):
        #print(ports)
        #print (route)
        # Print case: if the ports list is empty print route list with names
        if len(ports) == 0:
            #Print the route 
            print(' '.join([portnames[i] for i in route]))

        # Recursive case: for each element in the ports list, generate permutations
        # of the remaining elements and append the current element to each permutation
        else:
            for i in ports:
                new_route = route +[i]
                remaining_ports = ports[:]
                remaining_ports.remove(i)
                permutations(new_route, remaining_ports)
    
    # This will start the recursion with 0 ("PAN") as the first stop        
    permutations([0],list(range(1, len(portnames))))
    

# Call the main function
main()
def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    # Function to calculate emissions for a given route
    def calculate_emissions(route):
        # Emissions data for each leg of the journey (in kilograms)
        emissions_data = [
            [0, 400, 366, 0, 0],  # From PAN (0) to AMS (1), CAS (2), NYC (3), HEL (4)
            [400, 0, 100, 0, 0],  # From AMS (1) to PAN (0), CAS (2)
            [366, 100, 0, 88, 0], # From CAS (2) to PAN (0), AMS (1), NYC (3)
            [0, 0, 88, 0, 335],   # From NYC (3) to CAS (2), HEL (4)
            [0, 0, 0, 335, 0],    # From HEL (4) to NYC (3)
        ]
        
        # Calculate total emissions for the route
        total_emissions = sum(emissions_data[route[i]][route[i+1]] for i in range(len(route)-1))
        return total_emissions

    # Define function to generate permutations
    def permutations(route, ports):
        if not ports:
            # Calculate emissions for the route
            emissions = calculate_emissions(route)
            # Print the route and its emissions in the correct format
            print(' '.join([portnames[i] for i in route]), f'{emissions:.1f} kg')
        else:
            for port in ports:
                new_route = route + [port]
                new_ports = ports[:]
                new_ports.remove(port)
                permutations(new_route, new_ports)

    # Start the recursion with PAN (0) as the first stop
    permutations([0], list(range(1, len(portnames))))

# Call the main function
main()
def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)
    probabilities = []

    # write your solution here P(Denmark ∣ fisher)=fishers(Denmark)÷fishers(total)
    for population, fisher in zip(populations, fishers):
        probability = fisher/total_fishers
        probabilities.append(probability)

    for country, probability in zip(countries, probabilities):
       
        print("%s %.2f%%" % (country, probability*100)) # modify this to print correct results

main()
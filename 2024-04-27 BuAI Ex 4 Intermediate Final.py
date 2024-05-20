import random

def main():
    prob = 0.80
    if random.random() < prob:
        animal = "dog"
    else:
        animal = "cat"
    print(animal)

main()
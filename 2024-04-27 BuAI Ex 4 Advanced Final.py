import random

def main():
    
    dog_ratio = 0.8  # Set the ratio of getting 'dog' or 'cat' (0.5 means equal chance)
    if random.random() < dog_ratio:
        favourite = "dogs"
    elif random.random() < 0.5:
        favourite = "cats"
    else:
        favourite = "bats"
    print("I love " + favourite)  # This will print the favourite animal
   
    


main()

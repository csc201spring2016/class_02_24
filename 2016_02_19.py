import random
print(random.randint(1,10))
num_guess = int(input("Enter a number between 1 and 20: "))

low = 1
high = 20
                      
rand_num = random.randrange(low, high + 1)

if(num_guess == rand_num):
    print("Your guess ", num_guess, "was correct.")
else:
    print("Your guess ", num_guess, "was incorrect. The answer was ", rand_num)                      

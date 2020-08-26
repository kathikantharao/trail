import random
def game():
    print("Welcome to the 'Cows and Bulls' Game!")
    s = '1234567890'
    num = str(random.sample(s, 4))
    guess = input(" Guess a four digit number: ").split()
    cow, bull = 0, 0

    for element in guess:
        if element in num:
            if guess.index(element) == num.index(element):
                cow += 1
                print('cow' , element, end=' ')
            else:
                bull += 1
                print('bull', element, end=' ')


    print(f"\n {cow} cow, {bull} bull")

game()

# Increament in while loop

i = 1
while i <= 5:
    print(i* '*')
    i = i+1
print(f'Loop Done')


# Guessing game
Guess_count=0
Guess_limit=3
Secret_number=9

while Guess_count < Guess_limit:
    Guess = int(input(f' Guess the secret number '))
    Guess_count += 1
    if Guess == Secret_number:
        print(f' Brilliant')
        break
else:
    print(f' Loser')
    
# Car game
Command = ""
started = False
while True:
    Command = input(''' What do you want to do with the car?
                   you have the following options:
                   1. Start to start the car
                   2. Stop to stop the car
                   3. Terminate to end the game
                   ''')
    if Command == "start":
        if started:
            print(f'The car is already started')
        else: 
            started= True
        print(f' The car has started')
    elif Command == "stop":
        if not started:
            print(f' The car is already stopped')
        else:
            started = False
            print(f' The car has stopped')
    elif Command == "terminate":
        print(f' You have ended the game')
        break
else: 
    print( f' What the heck')
    
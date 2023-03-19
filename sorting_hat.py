hufflepuff = 0
gryffindor = 0
slytherin = 0 
ravenclaw = 0

user = (input('Welcome to the Sorting Hat! Type in your name and let\'s begin! ' ))

q1 = int(input('Question 1: Do you like Dawn or Dusk? ' 
                    '\n 1) Dawn '
                    '\n 2) Dusk '
                    '\n '))

if q1 == 1:
     gryffindor += 1
     ravenclaw += 1
elif q1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print('wrong input')

q2 = int(input('Question 2: When I\'m dead, I want people to remember me as: '
                    '\n 1) The Good'
                    '\n 2) The Great'
                    '\n 3) The Wise'
                    '\n 4) The Bold'
                    '\n '))

if q2 == 1:
    hufflepuff += 2
elif q2 == 2:
    slytherin += 2
elif q2 == 3:
    ravenclaw += 2
elif q2 == 4:
    gryffindor += 2
else:
    print('wrong input')

q3 = int(input('Question 3: Which kind of instrument most pleases your ears? '
                    '\n 1) The Violin'
                    '\n 2) The Trumpet'
                    '\n 3) The Piano'
                    '\n 4) The Drum'
                    '\n '))

if q3 == 1:
    slytherin += 4
elif q2 == 2:
    hufflepuff += 4
elif q2 == 3:
    ravenclaw += 4
elif q2 == 4:
    gryffindor += 4
else:
    print ('wrong input')


if slytherin > hufflepuff:
    if slytherin > ravenclaw:
        if slytherin > gryffindor:
            print("You are a Slytherin!")

if hufflepuff > slytherin:
    if hufflepuff > ravenclaw:
        if hufflepuff > gryffindor:
            print("You are a Hufflepuff!")

if ravenclaw > hufflepuff:
    if ravenclaw > slytherin:
        if ravenclaw > gryffindor:
            print("You are a Ravenclaw!")

if gryffindor > slytherin:
    if gryffindor > hufflepuff:
        if gryffindor > ravenclaw:
            print("You are a Gryffindor!")
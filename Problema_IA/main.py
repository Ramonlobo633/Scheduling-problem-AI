import random as r, scheduling

def random_state(nurses):
    state = ''
    for i in range(0, 21*nurses):
        state = state + str(r.randrange(0, 2))

    return state

option = 1
opt = 0

print('Scheduling nurse problem')

while option != 0:
    nurses = 10
    print('Choose a number of nurse:')
    print('1 - To define a value')
    print('2 - To a default value')
    opt = int(input())

    if opt == 1:
        nurses = int(input())
    if opt == 2:
        nurses = 10

    else:
        print('Wrong answer. Please, choose a valid option')
        option = 0

    print('Choose an option:')
    print('1 - To define an allocation')
    print('2 - To define randomly allocation')
    opt = int(input())

    if opt == 1:
        allocation = input()
    if opt == 2:
        allocation = random_state(nurses)

    else:
        print('Wrong answer. Please, choose a valid option')
        option = 0

    print('Choose a technique for scheduling:')
    print('1 - Hill Climb')
    print('2 - Best-First Search')
    print('3 - Steepest-Ascent Hill Climbing')
    print('4 - Quit')

    option = int(input())
    s = scheduling.Technique(allocation, nurses)
    if option == 1:
        print('Running Hill Climb technique')
        s.controller(1)

    elif option == 2:
        print('Running Best-First Search technique')
        s.controller(2)

    elif option == 3:
        print('Running Stochastic Hill Climbing technique')
        s.controller(3)

    elif option == 4:
        print('Exiting')
        option = 0
    else:
        print('Wrong answer. Please, choose a valid option')

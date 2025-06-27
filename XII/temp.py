print(f'{'Welcome to Python Calculator':^60}')
while True:
    print('1: Standard Calculator')
    print('2: Scientific Calculator')
    ch = int(input('Enter your choice: '))
    if 1 == ch:
        print('Standard Calculator')
    elif 2 == ch:
        print('Scientifc Calculator')
    else:
        print('Thank You...')
        break
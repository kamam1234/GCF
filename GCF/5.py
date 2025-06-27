# year = int(input('Enter year: '))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f'{year} is a leap year.')
#         else:
#             print(f'{year} is not a leap year.')
#     else:
#         print(f'{year} is a leap year.')
# else:
#     print(f'{year} is not a leap year.')

# for i in range(1, int(input('Enter a num: '))+1):
#     print(i, end='')


string = input('Enter a string: ')
# n = len(string)
# combination = (n*(n+1))//2
# score1 = 0
# score2 = 0

# for i in range(n):
#     if string[i].upper() in 'AEIUO':
#         score1 += len(string[i:])
# score2 = combination - score1

# print(score1, score2)
# Calculate the score for each substring
# For each character, calculate the substrings length
# If the character is a vowel, add the length of the substring to kevin_score
# If the character is a consonant, add the length of the substring to stuart_score
def minion_game(string):
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin_score += len(string[i:])
        else:
            stuart_score += length - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

minion_game(string)


# scores = eval(input('Enter scores: '))

# scores.sort()
# max = scores[-1]
# for i in scores[::-1]:
#     if i != max:
#         print(i)
#         break
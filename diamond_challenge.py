import sys

def print_diamond(letter):
    letter_valide = validate_input(letter)
    if letter_valide:
        a_ascii = ord('A')
        rows = ord(letter) - a_ascii + 1

        for x in list(range(rows)) + list(reversed(range(rows-1))):
            letter = chr(a_ascii+x)
            if x == 0:
                print('{: <{w1}}{letter}'.format('', w1=rows-1, letter=letter))
            else:
                print('{: <{w1}}{letter}{: <{w2}}{letter}'.format('', '', w1=rows-x-1, letter=letter, w2=x*2-1))

def validate_input(letter):
    if ord(letter) < ord('A') or ord(letter) > ord('Z'):
        print('Invalid input! Please input a capital letter (A-Z).')
        return False
    return True

print_diamond('Z')
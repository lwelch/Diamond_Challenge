import sys

def print_diamond(letter):
    """
    print_diamond takes the an input of a capital letter, and prints a diamond of letters starting with 'A' at the top
    and bottom point, and the provided letter at the right and left points. 
    
    For example, if 'D' is provided, the following will be printed:
        A
       B B
      C   C
     D     D
      C   C
       B B
        A

    If 'A' is input, a diamond cannot be generated, so a single line with 'A' is printed.
    """
    letter_valid = validate_input(letter)
    if letter_valid:
        diamond = build_diamond(letter)
        print('\n'.join(diamond))

def build_diamond(letter):
    """
    build_diamond is used to generate the list of strings needed to print the diamond structure.
    It takes a single argument of a letter (in string format), and returns a list of strings.

    This list of strings can then be printed with newline characters (using join) to output the
    diamond structure.
    """
    a_ascii = ord('A')
    rows = ord(letter) - a_ascii + 1
    diamond = []

    for x in list(range(rows)) + list(reversed(range(rows-1))):
        if x == 0:
            diamond.append('{: <{w1}}{letter}'.format('', w1=rows-1, letter=chr(a_ascii+x)))
        else:
            diamond.append('{: <{w1}}{letter}{: <{w2}}{letter}'.format('', '', w1=rows-x-1, letter=chr(a_ascii+x), w2=x*2-1))
    return diamond

def validate_input(letter):
    """
    validate_input has an input of a string. It check that the string length is 1 (a single letter)
    and verifies that the letter is capital.

    If the input is valid, validate_input returns True. Otherwise, it returns False.
    """
    if not isinstance(letter, str) or len(letter) != 1 \
    or ord(letter) < ord('A') or ord(letter) > ord('Z'):
        print("\nInvalid input! Please input a single capital letter (A-Z).\n")
        return False
    return True

# Main function starts here
if __name__ == '__main__':
    if len(sys.argv) == 2:
        base_letter = sys.argv[1] 
    else:
        if len(sys.argv) != 1:
            print("\nToo many arguments provided on the command line!\n")
        base_letter = raw_input("Enter a letter to create the diamond: ")

    print_diamond(base_letter.strip('\'').strip('\"')) #Strip off quotes if they are included.
"""
The diamond_challenge module takes a letter as an input, either on the command line, or via the
the keybord after the start of the script, and prints a diamond, starting with 'A' at the top,
and the supplied letter at the widest point.

The following is an example usage:
```
python diamond_challenge.py E
```
The script will then print out the following:
```
    A
   B B
  C   C
 D     D
E       E
 D     D
  C   C
   B B
    A
```
"""

import sys

def print_diamond(letter):
    """
    :param str letter: A capital letter, which will be used as
    the widest point of the diamond.

    print_diamond takes the an input of a capital letter, and prints a diamond of letters starting with 'A' at the top
    and bottom point, and the provided letter at the right and left points. This is the most generic
    function that calls all verificationand building functions. It is also responsible for printing
    the resulting diamond.

    For example, if 'D' is provided, the following will be printed:
    ```
       A
      B B
     C   C
    D     D
     C   C
      B B
       A
    ```

    If 'A' is input, a diamond cannot be generated, so a single line with 'A' is printed.
    """
    letter_valid = validate_input(letter)
    if letter_valid:
        diamond = build_diamond(letter)
        print('\n'.join(diamond))

def build_diamond(validated_letter):
    """
    >:param str validated_letter: A capital letter, that will be used to generate the
    list of strings needed to print out the diamond.

    >**Returns:** A list a strings that contains the correct spacing for printing
    the diamond.

    build_diamond is used to generate the list of strings needed to print the diamond structure.
    It takes a single argument of a letter (in string format), and returns a list of strings.

    This list of strings can then be printed with newline characters (using join) to output the
    diamond structure.

    """
    a_ascii = ord('A')
    rows = ord(validated_letter) - a_ascii + 1
    diamond = []

    for x in list(range(rows)) + list(reversed(range(rows-1))):
        if x == 0:
            diamond.append('{: <{w1}}{current_letter}'.format('', w1=rows-1, current_letter=chr(a_ascii+x)))
        else:
            diamond.append('{: <{w1}}{current_letter}{: <{w2}}{current_letter}'.format('', '', w1=rows-x-1, current_letter=chr(a_ascii+x), w2=x*2-1))
    return diamond

def validate_input(input_string):
    """
    :param str input_string: A string input to the program for validation
    that it will work wiht the diamond_challenge program.

    :return: *True* if the string can be used to create a diamond.
    *False* if cannot be used.

    """
    if not isinstance(input_string, str) or len(input_string) != 1 \
    or ord(input_string) < ord('A') or ord(input_string) > ord('Z'):
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
        base_letter = raw_input("Enter a capital letter to create the diamond: ")
        print("\n")

    print_diamond(base_letter.strip('\'').strip('\"')) #Strip off quotes if they are included.
# Diamond Challenge

## Table of Contents
1. Introduction
2. Functions

   2.1 print_diamond()  
   2.2 build_diamond()  
   2.3 validate_input()  
3. Unit Tests
4. Automated Test Cases

---

## 1. Introduction
The diamond_challenge module takes a letter as an input, either on the command line, or via the
the keybord after the start of the script, and prints a diamond, starting with 'A' at the top,
and the supplied letter at the widest point.

The following is an example usage for supplying a letter
on the command line:
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

Input can also be accepted at run-time. By using `python diamond_challenge.py`, the program will request an input via the following prompt:

```
    Enter a letter to create the diamond:
```
If a valid input is given, the program will print the diamond. If not, an error message will be generated, and the program will exit. This could easily be customized to handle errors the way the user wants.

---

## 2. Functions:
### **2.1 print_diamond(letter):**
>**Inputs:** *str* letter: A capital letter, which will be used as
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

---

### **2.2 build_diamond(letter):**
>**Inputs:** *str* validated_letter: A capital letter, that will be used to generate the
list of strings needed to print out the diamond.

>**Returns:** A list a strings that contains the correct spacing for printing
the diamond.

build_diamond is used to generate the list of strings needed to print the diamond structure.
It takes a single argument of a letter (in string format), and returns a list of strings.

This list of strings can then be printed with newline characters (using join) to output the
diamond structure.

---

### **2.3 validate_input(input_string):**
>**Inputs:** *str* input_string: A string input to the program for validation
that it will work wiht the diamond_challenge program.

>**Returns:** *True* if the string can be used to create a diamond.
*False* if cannot be used.

---
## 3. Unit Tests
Unit tests are provided with the program to test the functionality.
They can be run from the command line by entering:
```
python -m unittest diamond_challenge_unittest
```

---

## 4. Automated Test Cases
Automated tests cases are provided via shell and batch files which can 
be run on Unix and Windows machines repsectively. They generate an example output in the file test_output.txt
with some interesting test cases. The output of the automated test cases is provided, but will
be regnerated with each run of the shell/batch scripts.
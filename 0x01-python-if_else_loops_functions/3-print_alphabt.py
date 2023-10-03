#!/usr/bin/python3
char=97
while char < 123:
    if not  (format(chr(char)) == "q" or format(chr(char)) == "e"):
        print(format(chr(char)))
    char = char +1



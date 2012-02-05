import parser
import sys
import fileinput

for line in fileinput.input():
    print parser.parse(line)

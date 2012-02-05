import parser
import sys
import fileinput

for line in fileinput.input():
    if line == '\n':
        continue
    print line.rstrip()
    print parser.parse(line)
    print

print parser.global_symbol_table

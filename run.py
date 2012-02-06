import ITBLparser
import sys
import fileinput

for line in fileinput.input():
    if line == '\n':
        continue
    print line.rstrip()
    print ITBLparser.parse(line)
    print 

print ITBLparser.global_symbol_table

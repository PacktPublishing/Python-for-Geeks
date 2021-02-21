#multifilesread1.py
import fileinput
with fileinput.input(files = ("1.txt",'2.txt') )as f:
    for line in f:
        print(f.filename())
        print(line)
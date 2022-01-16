#!/usr/bin/env python3
import glob
import os
import re
import sys
# a = can; b = box; c = vessel; d = banana; e = tool
for filepath in glob.iglob('./**/*color.txt', recursive=True):
    with open(filepath, "r") as file:
        x = re.sub('^1 ', 'a ', file.read(), flags=re.MULTILINE)
        x = re.sub('^2 ', 'b ', x, flags=re.MULTILINE)
        x = re.sub('^2 ', 'b ', x, flags=re.MULTILINE)
        x = re.sub('^3 ', 'a ', x, flags=re.MULTILINE)
        x = re.sub('^4 ', 'c ', x, flags=re.MULTILINE)
        x = re.sub('^5 ', 'a ', x, flags=re.MULTILINE)
        x = re.sub('^6 ', 'b ', x, flags=re.MULTILINE)
        x = re.sub('^7 ', 'b ', x, flags=re.MULTILINE)
        x = re.sub('^8 ', 'a ', x, flags=re.MULTILINE)
        x = re.sub('^9 ', 'd ', x, flags=re.MULTILINE)
        x = re.sub('^10', 'c', x, flags=re.MULTILINE)
        x = re.sub('^11', 'c', x, flags=re.MULTILINE)
        x = re.sub('^12', 'c', x, flags=re.MULTILINE)
        x = re.sub('^13', 'c', x, flags=re.MULTILINE)
        x = re.sub('^14', 'e', x, flags=re.MULTILINE)
        x = re.sub('^15', 'b', x, flags=re.MULTILINE)
        x = re.sub('^16', 'e', x, flags=re.MULTILINE)
        x = re.sub('^17', 'e', x, flags=re.MULTILINE)
        x = re.sub('^18', 'e', x, flags=re.MULTILINE)
        x = re.sub('^19', 'e', x, flags=re.MULTILINE)
        x = re.sub('^20', 'b ', x, flags=re.MULTILINE)
        ###--Umrechnung auf 5 Klassen
        x = re.sub('^a', '0', x, flags=re.MULTILINE)
        x = re.sub('^b', '1', x, flags=re.MULTILINE)
        x = re.sub('^c', '2', x, flags=re.MULTILINE)
        x = re.sub('^d', '3', x, flags=re.MULTILINE)
        x = re.sub('^e', '4', x, flags=re.MULTILINE)
    file.close()
    with open(filepath, "w") as file:
        file.write(x)
    file.close()

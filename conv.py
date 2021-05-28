
from os import makedev
import sys

def makeNumberNice(number, length):
    addon = ""
    if(number[0] == '-'):
        addon = "-"
        number = number.replace("-", "")
    
    while(len(number) < length):
        number = "0" + number

    number = addon + number
    return number

if __name__=="__main__":

#quick and dirty solution to equally stupid problem

    try:
        with open(sys.argv[1], 'r') as f:
            content = f.readlines()
    except:
        print("File not found.")
        exit()

    numberLength = 6

    output = []

    for line in content:
        if(line[0] == 'X'):
            splitted = line.split('Y')
            splitted = [splitted[0].replace("X", ""), splitted[1]]
            splitted = [splitted[0].replace("\n", ""), splitted[1].replace("\n", "")]
            newLine = "X" + makeNumberNice(splitted[0], numberLength) + "Y" + makeNumberNice(splitted[1], numberLength) + "\n"
            output.append(newLine)
        else:
            output.append(line)

    splitName = sys.argv[1].split(".")

    newName = splitName[0] + "_converted." + splitName[1]

    with open(newName, 'w') as f:
        f.writelines(output)
    
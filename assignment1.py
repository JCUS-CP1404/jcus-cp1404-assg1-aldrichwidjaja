"""
Replace the contents of this module docstring with your own details
Name: Aldrich Widjaja
Date started: 25/07/2019
GitHub URL: https://github.com/JCUS-CP1404/jcus-cp1404-assg1-aldrichwidjaja/blob/master/README.md
"""

def main():
    print("Travel Tracker 1.0 - by <Aldrich Widjaja>")
    print("Welcome to my self-coded travel tracker")
    menuinput = input("""Menu:
L - List Places
A - Add new place
M - Mark a place as visited
Q - Quit""").upper()
    while menuinput != "Q":
        if menuinput == "L":
            open1()
            menuinput = input("""Menu:
L - List Places
A - Add new place
M - Mark a place as visited
Q - Quit""").upper()
        elif menuinput == "A".upper():
            add()
            menuinput = input("""Menu:
L - List Places
A - Add new place
M - Mark a place as visited
Q - Quit""").upper()
        elif menuinput == "M".upper():
            visit()
            menuinput = input("""Menu:
 L - List Places
A - Add new place
M - Mark a place as visited
Q - Quit""").upper()

def open1(): #READ CSV FILES AND DISPLAY
    import csv
    import operator
    with open('places.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        datasort = sorted(reader, key=lambda row:(row[3]))
        count = 0
        for row in datasort:
            count= count + 1
            notvis = row[3].replace('n', '*').replace('v', ' ')
            print(notvis, '{:>1}'.format(count),'{:>0}'.format('.'), '{:<20}'.format(row[0]), '{:<20}'.format(row[1]), "Priority",'{:<20}'.format(row[2]))

    csvFile.close()

def add(): #WRITE CSV FILES IN NEW LINE
    import csv
    x = str(input("Please Input city name"))
    y = str(input("Please Input country name"))
    z = int(input("Please Input priority"))
    vn = "n"
    print(x, "In", y, "Priority", z, "Has been added to travel tracker")
    newrow = [x, y, z, vn]

    with open('places.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(newrow)
    csvFile.close()

def visit():
    import csv
    x = int(input("Please choose place to visit"))

    with open('places.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        datasort = sorted(reader, key=lambda row: (row[3]))

    with open('places.csv', 'w', newline='') as csvFile1:
        writer = csv.writer(csvFile1)
        num = 0
        for row in datasort:
            num = num+1
            if num == x:
                    row[3] = "v"
                writer.writerow(row)

    csvFile.close()
    csvFile1.close()





main()




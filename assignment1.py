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
Q - Quit""")
    while menuinput != "Q".upper():
        if menuinput == "L".upper():
            open1()
            menuinput = input("""Menu:
L - List Places
A - Add new place
M - Mark a place as visited
Q - Quit""")
        elif menuinput == "A".upper():
            add()
            menuinput = input("""Menu:
L - List Places
A - Add new place
M - Mark a place as visited
Q - Quit""")

def open1():
    import csv
    with open('places.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            print(row)
    csvFile.close()

def add():
    import csv
    x = str(input("Please Input name"))
    y = str(input("Please Input name"))
    z = int(input("Please Input name"))
    print(x, "In", y, "Priority", z, "Has been added to travel tracker")
    newrow = [x, y, z]

    with open('places.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(newrow)
    csvFile.close()

def visit():
    text = open('places.csv', 'r')
    visit =

main()




"""
Replace the contents of this module docstring with your own details
Name: Aldrich Widjaja
Date started: 25/07/2019
GitHub URL: https://github.com/JCUS-CP1404/jcus-cp1404-assg1-aldrichwidjaja/blob/master/README.md
"""

def main():
    print("Travel Tracker 1.0 - by <Aldrich Widjaja>")
    print("Welcome to my self-coded travel tracker")
    readfile()
    menuinput = input("""Menu:
L - List Places
A - Add new place
M - Mark a place as visited
Q - Quit
>>>""").upper()
    while menuinput != "Q":
        if menuinput == "L":
            open1()
            menuinput = input("""Menu:
L - List Places
A - Add new place
M - Mark a place as visited
Q - Quit
>>>""").upper()
        elif menuinput == "A".upper():
            add()
            menuinput = input("""Menu:
L - List Places
A - Add new place
M - Mark a place as visited
Q - Quit
>>>""").upper()
        elif menuinput == "M".upper():
            visitplace = readfile1()
            if visitplace>0:
                visit()
                menuinput = input("""Menu:
L - List Places
A - Add new place
M - Mark a place as visited
Q - Quit
>>>""").upper()
            else:
                print("No Unvisited Place")
                menuinput = input("""Menu:
L - List Places
A - Add new place
M - Mark a place as visited
Q - Quit
>>>""").upper()
        else:
            print("Invalid Choice! Please choose menu")
            menuinput = input("""Menu:
L - List Places
A - Add new place
M - Mark a place as visited
Q - Quit
>>>""").upper()

    savefile()
    print("Have a nice day :) - Aldrich Widjaja")

def open1(): #READ CSV FILES AND DISPLAY
    import csv
    import operator
    with open('places.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        datasort = sorted(reader, key=lambda row:(row[3],(int(row[2]))))
        count = 0
        row_count = sum(1 for row in datasort)
        row_count1 = 0
        for row in datasort:
            if row[3] == 'n':
                row_count1 = row_count1 + 1
            count= count + 1
            notvis = row[3].replace('n', '*').replace('v', ' ')
            print(notvis, '{:>1}'.format(count),'{:>0}'.format('.'), '{:<10}'.format(row[0]), "in", '{:<20}'.format(row[1]), "Priority",'{:<10}'.format(row[2]))
        if row_count1 == 0:
            print(row_count, "Places, No places left to visit. Why not add a new place?")
        else:
            print(row_count, "Places, you still want to visit", row_count1, "places")

    csvFile.close()

def add(): #WRITE CSV FILES IN NEW LINE
    import csv
    while True:
        x = input("Name: ")
        if x.isalpha() or '':
            break
        print("Invalid! Input Can't be blank / input only in alphabets")
    while True:
        y = input("Country: ")
        if y.isalpha() or '':
            break
        print("Invalid! Input Can't be blank / input only in alphabets")

    class NotPositiveError(UserWarning):
        pass

    while True:
        z = input("Priority: ")
        try:
            number = int(z)
            if number <= 0:
                raise NotPositiveError
            break
        except ValueError:
            print("Invalid Input! Enter a valid number")
        except NotPositiveError:
            print("Number must be > 0")

    vn = "n" #vn = mark non-visited
    print(x, "In", y, "Priority", z, "Has been added to travel tracker")
    newrow = [x, y, z, vn]

    with open('places.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(newrow)
    csvFile.close()

def visit(): #Function to mark visited places
    import csv

    with open('places.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        datasort = sorted(reader, key=lambda row: (row[3], (int(row[2]))))

    while True:
        try:
            x = int(input("Please choose place to visit"))
            if x > sum(1 for row in datasort):
                print("Invalid place number!")
                continue
            elif x <= 0:
                print("Invalid! Number must be > 0")
                continue

        except ValueError:
            print("Invalid! Enter a valid number")
            continue
        else:
            break

    with open('places.csv', 'w', newline='') as csvFile1:
        writer = csv.writer(csvFile1)
        num = 0
        for row in datasort:
            num = num+1
            if num == x:
                if row[3] is "v":
                    print("Place is already visited")
                else:
                    row[3] = "v"
                    print(row[0], "in",row[1], "is visited")

            writer.writerow(row)

    csvFile.close()
    csvFile1.close()

def readfile():
    import csv
    with open('places.csv', 'r') as csvfile2:
        reader = csv.reader(csvfile2)
        row_count = sum(1 for row in reader)
        print(row_count,"Files loaded from places.csv")
    csvfile2.close()

def savefile():
    import csv
    with open('places.csv', 'r') as csvfile2:
        reader = csv.reader(csvfile2)
        row_count = sum(1 for row in reader)
        print(row_count,"Files saved to places.csv")
    csvfile2.close()

def readfile1():
    import csv
    with open('places.csv', 'r') as csvfile2:
        reader = csv.reader(csvfile2)
        visit = 0
        for row in reader:
            if row[3] == 'n':
                visit = visit + 1
            else:
                visit = visit
    csvfile2.close()
    return visit

main()




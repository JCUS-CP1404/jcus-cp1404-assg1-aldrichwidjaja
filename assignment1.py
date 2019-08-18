"""
Name: Aldrich Widjaja
Date started: 25/07/2019
GitHub URL: https://github.com/JCUS-CP1404/jcus-cp1404-assg1-aldrichwidjaja/blob/master/README.md
"""
def main(): #        MAIN FUNCTION - to call menu & function based on menu             #
    print("Travel Tracker 1.0 - by <Aldrich Widjaja>")
    print("Welcome to my self-coded travel tracker")
    countcsv = readfile()
    print(countcsv, "Places loaded from places.csv")
    callmenu = menu()
    while callmenu != "Q":
        if callmenu == "L":
            open1()
            callmenu = menu()
        elif callmenu == "A".upper():
            add()
            callmenu = menu()
        elif callmenu == "M".upper():
            visitplace = readfile1()
            if visitplace>0:
                open1()
                visit()
                callmenu = menu()
            else:
                print("No Unvisited Place")
                callmenu = menu()
        else:
            print("Invalid Choice! Please choose menu")
            callmenu = menu()

    print(countcsv, "Places saved in places.csv")
    print("Have a nice day :) - Aldrich Widjaja")

def menu():#        MENU FUNCTION - to display menu and input choice of menu          #
    menuinput = input("""Menu:
L - List Places
A - Add new place
M - Mark a place as visited
Q - Quit
>>>""").upper()
    return menuinput

def open1(): #        read&display csv function- open csv file and display              #
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
            notvis = row[3].replace('n', '*').replace('v', ' ') #notvis is * / none to show visit / unvisited place
            print(notvis, '{:>1}'.format(count),'{:>0}'.format('.'), '{:<10}'.format(row[0]), "in", '{:<20}'.format(row[1]), "Priority",'{:<10}'.format(row[2]))
        if row_count1 == 0:
            print(row_count, "Places, No places left to visit. Why not add a new place?")
        else:
            print(row_count, "Places, you still want to visit", row_count1, "places")

    csvFile.close()

def add():#        ADD FUNCTION - to append and add new line data in csv             #
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

def visit():#        visit FUNCTION -to mark unvisited place to visited                #
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

def readfile():#        COUNT LINES CSV FUNCTION - to sum lines in csv                    #
    import csv
    with open('places.csv', 'r') as csvfile2:
        reader = csv.reader(csvfile2)
        row_count = sum(1 for row in reader)
    return row_count
    csvfile2.close()

def readfile1():#        mark no unvisited place left function                             #
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

main() #TO START ALL THE WORK

import csv

with open('lyrics.csv') as csvfile:
    csv_f = csv.DictReader(csvfile)

    songNum = 0

    for row in csv_f:
        if row['genre'] == 'Pop':
            songNum += 1

    print(songNum)

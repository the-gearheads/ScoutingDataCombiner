import glob
import csv

path = "PUT_SCOUTING_DATA_HERE\*.csv"
fileCounter = 0
combinedCSV = []
for fname in glob.glob(path):
    with open(fname, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = []
        for row in reader:
            rows.append(row)
    if(fileCounter == 0):
        print(rows[0])
        combinedCSV.append(rows[0])
    combinedCSV.extend(rows[1:])
        
    fileCounter+=1

print(combinedCSV)
print(len(combinedCSV))

with open('combinedResults.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerows(combinedCSV)

import csv

rows = ["bcvvbcbc", "vbcbb", "hjgn", "aas", "dffds"]

csvFile = open('test.csv', 'w', newline='\n', encoding='utf-8')
for row in rows:

    csvWriter = csv.writer(csvFile)
    csvWriter.writerow([row,])
    csvFile.close()



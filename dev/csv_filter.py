from array import array
import pandas as pd
import csv
import re

# takes csv and filter
data = pd.read_csv('announce.csv')
data = data["Content"]
data.to_csv('output.csv')
toRemove = 0

# this commented code dosent fucking work and im sad because i wrote it myself
#with open('output.csv', newline='') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=',')
#    for row in spamreader:       
#       if '\nhttps:' in row[1]:
#            toRemove+1
#            print("fraudulent line")
#            spamreader.remove(toRemove)
#    print(spamreader)
# pandas adds some dumb things to the csv so you have to remove them manually with https://edit-csv.net/
pause = input("Press enter once you have removed content and numbers")
my_file_name = "output.csv"
cleaned_file_name = "cleanNVG.csv"
ONE_COLUMN = 0
remove_words = ['https:', 'http:']
# filter urls (yay)
with open(my_file_name, 'r', newline='') as infile, \
     open(cleaned_file_name, 'w',newline='') as outfile:
    writer = csv.writer(outfile)
    for row in csv.reader(infile, delimiter='|'):
        column = row[ONE_COLUMN]
        if not any(remove_word in column for remove_word in remove_words):
            writer.writerow(row)

from array import array

import pandas as pd

import csv

import re

csvanme = input("enter csv name")

finaloutput = input("enter output name")

# takes csv and filter

data = pd.read_csv(csvanme)

data = data["Content"]

data.to_csv('outputtest.csv')



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
pause = input("Press enter once you have removed content and numbers https://edit-csv.net/")

my_file_name = "outputtest.csv"

cleaned_file_name = finaloutput

csvanme = "outputtest.csv"

ONE_COLUMN = 0

remove_words = ['https:', 'http:']
# filter urls (yay)

dfghmdhjfgfhjk = input("press a key once you have remove whitenames")
pd.read_csv('outputtest.csv').dropna().to_csv('outputtest.csv', index=False)

with open(my_file_name, 'r', newline='') as infile, \
     open(cleaned_file_name, 'w',newline='') as outfile:
    writer = csv.writer(outfile)
    for row in csv.reader(infile, delimiter='|'):
        column = row[ONE_COLUMN]
        if not any(remove_word in column for remove_word in remove_words):
            writer.writerow(row)

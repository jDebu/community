#Python code:
import csv # first we need import necessary lib:csv
file=open("e:\Pizza.csv") #prepare a csv file for our example

testReader=csv.reader(file,delimiter=' ', quotechar='|')
#now the testReader is an array,so we can iterate it
for row in testReader:
    print "|".join(row)
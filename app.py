import math
import csv

with open("data.csv", newline='') as f:
    reader = csv.reader(f)
    data1 = list(reader)

filedata = data1[0]

def mean(data):
    forgotitwas = 0
    mean = 0

    for numbers in data:
        forgotitwas = forgotitwas + int(numbers)

        mean = forgotitwas/len(data)

    return mean

values = []
meanvalue = mean(filedata)

for numbers in filedata:
    a = int(numbers) - meanvalue

    a = a**2

    values.append(a)

sum = 0

for numbers in values:
    sum = sum + numbers

thisthing = sum/(len(filedata)-1)

standarddeviation = math.sqrt(thisthing)
print(standarddeviation)
    
